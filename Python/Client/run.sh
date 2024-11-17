#!/bin/bash

DEFAULT_IP="172.21.33.21"
DEFAULT_PORT="8080"

IP=${1:-$DEFAULT_IP}
PORT=${2:-$DEFAULT_PORT}

docker run -it --rm --network-alias z33_client_python --network z33_network --name z33_client_python z33_client_python --host $IP --port $PORT
