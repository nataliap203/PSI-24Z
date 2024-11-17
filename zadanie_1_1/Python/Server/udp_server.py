import socket
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="UDP Server")
    parser.add_argument(
        "--host",
        type=str,
        default="0.0.0.0",
        help="Server IP address (default 0.0.0.0)",
    )
    parser.add_argument(
        "--port", type=int, default="8000", help="Server port (default 8000)"
    )
    parser.add_argument(
        "--bufsize", type=int, default="512", help="Buffer size (default 1024)"
    )
    return parser.parse_args()


def confirm_datagram(data, bufsize):
    if len(data) < 2:
        return "ERROR: Datagram not long enough"

    datagram_length_declared = int.from_bytes(data[:2], "big")
    msg = data[2:].decode()

    if datagram_length_declared > bufsize:
        return f"ERROR: Buffer size ({bufsize} bytes) exceeded. Declared datagram length: {datagram_length_declared} bytes"

    if datagram_length_declared - 2 != len(msg):
        return f"ERROR: Incorret message length. Declared message length: {datagram_length_declared - 2} bytes, but actual {len(msg)} bytes"

    letters = 'ABCDEFGHIJKLMNOPRSTUWXYZ'
    repeat_count = (datagram_length_declared - 2) // len(letters) + 1
    expected_seq = (letters * repeat_count)[:datagram_length_declared - 2]

    if msg != expected_seq:
        return "ERROR: Incorrent datagram format"

    return f"OK: Recieved message with length {len(msg)} bytes"


def Work():
    return True


def main():
    args = parse_args()

    port = args.port
    host = args.host
    bufsize = args.bufsize

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"UDP server up and listening on {host}:{port}")
        print()
        print("-" * 50)
        while Work():
            data, address = s.recvfrom(bufsize)
            print(f"Recieved {len(data)} bytes from client {address}")

            response = confirm_datagram(data, bufsize)
            print(f"Sending response to client {address}: \"{response}\"")
            print("-" * 50)
            s.sendto(response.encode(), address)


if __name__ == "__main__":
    main()
