import socket
import argparse
import time


def parse_args():
    parser = argparse.ArgumentParser(description="TCP Client")
    parser.add_argument(
        "--host",
        type=str,
        default="0.0.0.0",
        help="Server IP address (default 0.0.0.0)",
    )
    parser.add_argument(
        "--port", type=int, default=8000, help="Server port (default 8000)"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    port = args.port
    host = args.host

    data_to_send = "X" * 102400
    chunk_size = 128
    total_sent = 0
    delay = 0.1

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Connected to {host}:{port}")

        for i in range(0, len(data_to_send), chunk_size):
            chunk = data_to_send[i : i + chunk_size]
            client_socket.sendall(chunk.encode("utf-8"))
            total_sent += len(chunk)

            print()
            print("-" * 50)
            print(f"Offset: {i} bytes | Sent data: {len(chunk)} bytes")
            print("-" * 50)

            time.sleep(delay)

        print()
        print(f"Sent {total_sent} bytes successfully.")


if __name__ == "__main__":
    main()
