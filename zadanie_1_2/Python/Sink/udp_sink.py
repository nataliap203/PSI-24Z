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
        "--port", type=int, default=8000, help="Server port (default 8000)"
    )
    parser.add_argument(
        "--bufsize", type=int, default=512, help="Buffer size (default 512 bytes)"
    )

    return parser.parse_args()


def Work():
    return True


def main():
    args = parse_args()

    port = args.port
    host = args.host
    bufsize = args.bufsize

    seq_bit = None

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))

        print(f"UDP server up and listening on {host}:{port}")

        while Work():
            data, address = s.recvfrom(bufsize)

            recv_seq_bit = data[0]

            print("\n")
            print("-" * 50)
            print(
                f"Datagram received from {address}",
                f"Seq bit: {recv_seq_bit}\n",
                f"Datagram: {data.rstrip(b"\0")}\n",
                sep="",
            )

            if not seq_bit or seq_bit != recv_seq_bit:
                print("New data. Updating seq bit")
                seq_bit = recv_seq_bit
            else:
                print("Data duplicated or out-of-order. Sending ACK again")

            ack_datagram = f"ACK {seq_bit}".encode().ljust(bufsize, b"\0")

            s.sendto(ack_datagram, address)
            print(f"Sent acknowledgment: {ack_datagram.rstrip(b"\0")}")
            print("-" * 50)


if __name__ == "__main__":
    main()
