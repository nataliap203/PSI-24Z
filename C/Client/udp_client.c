#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <time.h>

#define BUFSIZE 65535

#define DATAGRAM_LEN_ERROR -1
#define OVERFLOW_ERROR -2


int generate_datagram(char *datagram, int length) {
    if (length < 2) return DATAGRAM_LEN_ERROR;

    if (length > BUFSIZE) return OVERFLOW_ERROR;


    datagram[0] = (length >> 8) & 0xFF;
    datagram[1] = length & 0xFF;

    const char letters[] = "ABCDEFGHIJKLMNOPRSTUWXYZ";
    uint letters_len = sizeof(letters) - 1;
    int i;
    for (i = 2; i < length; i++) {
        datagram[i] = letters[(i - 2) % letters_len];
    }
    return 0;
}

int main(int argc, char *argv[]) {
    const char *host = "0.0.0.0";
    int port = 8001;

    if (argc > 1) host = argv[1];
    if (argc > 2) port = atoi(argv[2]);


    int sock;
    if ((sock = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }


    struct sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(port);
    server_addr.sin_addr.s_addr = inet_addr(host);


    char *datagram = malloc(BUFSIZE);
    char *response = malloc(BUFSIZE);
    if (!datagram || !response) {
        perror("Memory allocation failed");
        exit(EXIT_FAILURE);
    }

    printf("--------------------------------------------------\n");

    int datagram_size;
    for (datagram_size = 1; datagram_size <= BUFSIZE + 100; datagram_size += 100) {
        int ok = generate_datagram(datagram, datagram_size);

        if (ok == DATAGRAM_LEN_ERROR) {
            fprintf(stderr, "ERROR: Datagram not long enough.\n");
            printf("--------------------------------------------------\n");
            continue;
        };

        if (ok == OVERFLOW_ERROR) {
            fprintf(stderr, "ERROR: Cannot write %d on two bytes.\n", datagram_size);
            printf("--------------------------------------------------\n");
            break;;
        }

        printf("Sending datagram with length %d bytes to server %s:%d\n", datagram_size, host, port);

        if (sendto(sock, datagram, datagram_size, 0, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
            fprintf(stderr, "Maximum OS datagram size exceeded. Declared datagram length: %d bytes.", datagram_size);
            printf("--------------------------------------------------\n");
            printf("Looking for maximum OS datagram size...\n");
            printf("--------------------------------------------------\n");
            break;
        }

        socklen_t server_len = sizeof(server_addr);
        int received = recvfrom(sock, response, BUFSIZE, 0, (struct sockaddr *)&server_addr, &server_len);
        if (received > 0) {
            response[received] = '\0';
            printf("Received response from server: \"%s\"\n", response);
        } else {
            perror("No response from server");
        }

        printf("--------------------------------------------------\n");
    }

    int size;
    for (size = datagram_size - 1; size > 1; size--) {

        if (generate_datagram(datagram, size) == OVERFLOW_ERROR) {
            fprintf(stderr, "ERROR: Cannot write %d on two bytes.\n", datagram_size);
            printf("--------------------------------------------------\n");
            continue;;
        }

        printf("Trying to send %d bytes.\n", size);

        if (sendto(sock, datagram, size, 0, (struct sockaddr *)&server_addr, sizeof(server_addr)) >= 0) {
            printf("Datagram with length %d bytes accepted\n", size);
            printf("--------------------------------------------------\n");
            break;
        } else {
            fprintf(stderr, "Maximum OS datagram size exceeded. Declared datagram length: %d bytes.\n", size);
            printf("--------------------------------------------------\n");
        }
    }

    printf("\nFound maximum OS datagram size: %d bytes\n",  size);

    free(datagram);
    free(response);
    close(sock);
    return 0;
}
