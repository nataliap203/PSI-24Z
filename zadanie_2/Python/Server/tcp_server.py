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

def main():
    args = parse_args()

    port = args.port
    host = args.host
    buffer_size = 1024
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"The server is listening at {host}:{port}...")
        
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connection from {addr}")
            complete_data = b""
            while True:
                data = conn.recv(buffer_size)
                if not data:
                    break
                complete_data += data
                print(f"Recieved: {data.decode('utf-8', errors='ignore')} which means: {len(data)} bytes")
            
            print(f"Size of recieved data: {len(complete_data)} bytes.")


if __name__ == "__main__":
    main()
