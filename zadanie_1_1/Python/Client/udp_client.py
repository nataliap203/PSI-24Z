import socket
import argparse

BUFSIZE = 65535


def parse_args():
    parser = argparse.ArgumentParser(description="UDP Client")
    parser.add_argument(
        "--host",
        type=str,
        default="0.0.0.0",
        help="Server IP address (default 0.0.0.0)",
    )
    parser.add_argument(
        "--port", type=int, default="8000", help="Server port (default 8000)"
    )
    return parser.parse_args()


def generate_datagram(length):
    if length < 2:
        raise ValueError("ERROR: Datagram not long enough")

    letters = 'ABCDEFGHIJKLMNOPRSTUWXYZ'
    repeat_count = (length - 2) // len(letters) + 1
    msg = (letters * repeat_count)[:length - 2]
    datagram = length.to_bytes(2, "big") + msg.encode()

    return datagram


def main():
    args = parse_args()

    port = args.port
    host = args.host

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        print("-" * 50)
        for datagram_size in range(1, BUFSIZE + 100, 100):
            try:
                data = generate_datagram(datagram_size)

                print(f"Sending datagram with length {datagram_size} bytes to server {host}:{port}.")

                s.sendto(data, (host, port))
                response = s.recv(BUFSIZE)

                print(f"Received response from server {host}:{port}: \"{response.decode()}\".")
                print("-" * 50)

            except ValueError as ve:
                print(ve)
                print("-" * 50)
            except OverflowError:
                print(f"ERROR: Cannot write {datagram_size} on two bytes")
                print("-" * 50)
                break
            except OSError:
                print(f"ERROR: Maximum OS datagram size exceeded. Declared datagram length: {datagram_size} bytes")
                print("-" * 50)
                print()
                print("Looking for maximum OS datagram size...")
                print()
                print("-" * 50)
                break

        for size in range(datagram_size-1, 1, -1):
            try:
                data = generate_datagram(size)
                print(f"Trying to send {size} bytes.")
                s.sendto(data, (host, port))
                print(f"Datagram with length {size} bytes accepted")
                print("-" * 50)
                break
            except ValueError as e:
                print(e)
                print("-" * 50)
            except OverflowError:
                print(f"ERROR: Cannot write {size} on two bytes")
                print("-" * 50)
            except OSError:
                print(f"ERROR: Maximum OS datagram size exceeded. Declared datagram length: {size} bytes")
                print("-" * 50)

        print()
        print(f"Found maximum OS datagram size: {size} bytes.")


if __name__ == "__main__":
    main()
