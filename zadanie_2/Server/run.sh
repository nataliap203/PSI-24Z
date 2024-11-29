#!/bin/bash

DEFAULT_IP="172.21.33.21"
DEFAULT_PORT="8080"

IP=${1:-$DEFAULT_IP}
PORT=${2:-$DEFAULT_PORT}

docker run -it --network-alias z33_server_python_tcp --network z33_network --name z33_server_python_tcp --ip $IP z33_server_python_tcp --host $IP --port $PORT
