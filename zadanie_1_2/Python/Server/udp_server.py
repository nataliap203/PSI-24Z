import socket
import argparse
import random


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
        "--drop_rate",
        type=float,
        default=0.1,
        help="Simulated packet drop rate (default 0.1)",
    )
    return parser.parse_args()


def confirm_datagram(data):
    """Check datagram format and sequence correctness."""
    if len(data) != 512:
        return "ERROR: Datagram size mismatch", None

    seq_bit = data[0]  # Sequence bit
    payload = data[1:].rstrip(b"\x00")  # Remove padding

    if len(payload) == 0:
        return "ERROR: Empty payload", seq_bit

    # Example payload validation (optional)
    if not payload.isascii():
        return "ERROR: Payload contains non-ASCII characters", seq_bit

    return f"OK: Received payload with length {len(payload)} bytes", seq_bit


def should_drop_packet(drop_rate):
    """Simulate packet loss based on drop rate."""
    return random.random() < drop_rate


def Work():
    return True


def main():
    args = parse_args()

    port = args.port
    host = args.host
    bufsize = args.bufsize
    drop_rate = args.drop_rate

    seq_bit = None

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"UDP server up and listening on {host}:{port}\n")
        # print("-" * 50)

        while Work():
            data, address = s.recvfrom(bufsize)

            recv_seq_bit = data[0]

            if not seq_bit or seq_bit != recv_seq_bit:
                seq_bit = recv_seq_bit

            ack_datagram = f"ACK {seq_bit}".encode().ljust(bufsize, b"\0")

            s.sendto(ack_datagram, address)


if __name__ == "__main__":
    main()
