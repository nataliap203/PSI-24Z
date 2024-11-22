import socket
import argparse
import time


def parse_args():
    parser = argparse.ArgumentParser(description="UDP Server")
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
        "--bufsize", type=int, default=512, help="Buffer size (default 512 bytes)"
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=1.0,
        help="Timeout for ACK (default 1.0 second)",
    )
    return parser.parse_args()


def work():
    return True


def generate_datagram(no: int, length: int, seq_bit: bool):
    payload = (
        f"Message no. {no} with length {length} bytes and seq_bit {seq_bit}".encode()
    )

    datagram = seq_bit.to_bytes(1, "big") + payload.ljust(length - 1, b"\0")

    return datagram


def main():
    args = parse_args()

    host = args.host
    port = args.port
    bufsize = args.bufsize
    timeout = args.timeout

    no = 1
    seq_bit = 0
    ack_recv = True

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(timeout)

        while work():
            if ack_recv:
                datagram = generate_datagram(no, bufsize, seq_bit)

            print("-" * 50)
            print(f"Sending \"{datagram.rstrip(b"\0")}\" to server {host}:{port}")

            s.sendto(datagram, (host, port))

            try:
                response, server = s.recvfrom(bufsize)
                response = response.rstrip(b"\0").decode()

                if response == f"ACK {seq_bit}":
                    print(
                        f"Received ACK for \"{datagram.rstrip(b"\0")}\" from server {server}"
                    )
                    seq_bit = 1 - seq_bit
                    no += 1
                    ack_recv = True
                else:
                    print(
                        f"Received incorrect ACK for \"{datagram.rstrip(b"\0")}\" from server {server}",
                        f"Expected {seq_bit}, received {not seq_bit}",
                        "Retrying...",
                    )
                    ack_recv = False

            except TimeoutError:
                print(
                    f"No ACK received for \"{datagram.rstrip(b"\0")}\"",
                    "Retrying...",
                )
                ack_recv = False

            print("-" * 50, "\n")

            time.sleep(1)


if __name__ == "__main__":
    main()
