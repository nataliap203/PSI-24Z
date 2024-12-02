import socket
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="TCP Server")
    parser.add_argument(
        "--host",
        type=str,
        default="0.0.0.0",
        help="Server IP address (default 0.0.0.0)",
    )
    parser.add_argument(
        "--port", type=int, default=8000, help="Server port (default 8000)"
    )
    parser.add_argument(
        "--bufsize", type=int, default=512, help="Buffer size (default 512)"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    port = args.port
    host = args.host
    bufsize = args.bufsize

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"TCP server up and listening on {host}:{port}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connection from {addr}")
            complete_data = b""
            while True:
                data = conn.recv(bufsize)
                if not data:
                    break
                complete_data += data
                print()
                print("-" * 50)
                print(
                    f"Recieved {len(data)} bytes that means \"{data.decode('utf-8')}\""
                )
                print()
                print(f"Total data length: {len(complete_data)} bytes")
                print("-" * 50)

            print("\n")
            print(f"Size of recieved data: {len(complete_data)} bytes.")


if __name__ == "__main__":
    main()
