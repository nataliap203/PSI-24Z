#!/bin/bash

DEFAULT_IP="172.21.33.11"
DEFAULT_PORT="8080"

IP=${1:-$DEFAULT_IP}
PORT=${2:-$DEFAULT_PORT}

docker run -it --network-alias z33_client_c --network z33_network --name z33_client_c z33_client_c $IP $PORT
