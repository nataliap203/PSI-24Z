#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define DEFAULT_BUFSIZE 512

int compare_format(const char* msg, int msg_length, int declared_length) {
    const char letters[] = "ABCDEFGHIJKLMNOPRSTUWXYZ";
    uint letters_len = sizeof(letters) - 1;

    char *expected_seq = (char *)malloc(declared_length - 2 + 1);
    if (!expected_seq) {
        perror("Memory allocation failed");
        exit(EXIT_FAILURE);
    }
    int i;
    for (i = 0; i < declared_length - 2; i++) {
        expected_seq[i] = letters[i % letters_len];
    }
    expected_seq[declared_length - 2] = '\0';

    int is_equal = strncmp(msg, expected_seq, msg_length);
    free(expected_seq);

    return is_equal;
}

void confirm_datagram(const char *data, int length, int bufsize, char *response) {
    if (length < 2) {
        strcpy(response, "ERROR: Datagram not long enough");
        return;
    }

    int declared_length = ((unsigned char)data[0] << 8) | (unsigned char)data[1];
    const char *msg = data + 2;
    int msg_length = length - 2;

    if (declared_length > bufsize) {
        snprintf(response, bufsize, "ERROR: Buffer size (%d bytes) exceeded. Declared datagram length: %d bytes.",
                 bufsize, declared_length);
        return;
    }

    if (declared_length - 2 != msg_length) {
        snprintf(response, bufsize, "ERROR: Incorrect message length. Declared: %d bytes, Actual: %d bytes.",
                 declared_length - 2, msg_length);
        return;
    }

    if (compare_format(msg, msg_length, declared_length) != 0) {
        strcpy(response, "ERROR: Incorrect datagram format");
        return;
    }

    snprintf(response, bufsize, "OK: Received message with length %d bytes.", msg_length);
}

int main(int argc, char *argv[]) {
    const char *host = "0.0.0.0";
    int port = 8001;
    int bufsize = DEFAULT_BUFSIZE;

    if (argc > 1) {host = argv[1];}
    if (argc > 2) port = atoi(argv[2]);
    if (argc > 3) bufsize = atoi(argv[3]);


    int sock;
    if ((sock = socket(AF_INET, SOCK_DGRAM, 0)) == -1) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    struct sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(port);
    server_addr.sin_addr.s_addr = inet_addr(host);


    if (bind(sock, (struct sockaddr *)&server_addr, sizeof(server_addr)) == -1) {
        perror("Bind failed");
        close(sock);
        exit(EXIT_FAILURE);
    }


    char *buffer = malloc(bufsize);
    if (!buffer) {
        perror("Memory allocation failed");
        close(sock);
        exit(EXIT_FAILURE);
    }


    struct sockaddr_in client_addr;
    socklen_t client_len = sizeof(client_addr);


    printf("UDP server listening on %s:%d\n", host, port);
    printf("----------------------------------------\n");

    while (1) {
        int received = recvfrom(sock, buffer, bufsize, 0, (struct sockaddr *)&client_addr, &client_len);
        if (received == -1) {
            perror("Receive failed");
            printf("----------------------------------------\n");
            continue;
        }

        buffer[received] = '\0';
        printf("Received %d bytes from client %s:%d\n", received,
               inet_ntoa(client_addr.sin_addr), ntohs(client_addr.sin_port));

        char response[DEFAULT_BUFSIZE];

        confirm_datagram(buffer, received, bufsize, response);

        printf("Sending response to client: %s\n", response);
        printf("----------------------------------------\n");

        sendto(sock, response, strlen(response), 0, (struct sockaddr *)&client_addr, client_len);
    }

    free(buffer);
    close(sock);
    return 0;
}
