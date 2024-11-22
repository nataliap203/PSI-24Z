#!/bin/bash

DEFAULT_IP="172.21.33.31"
DEFAULT_PORT="8080"

IP=${1:-$DEFAULT_IP}
PORT=${2:-$DEFAULT_PORT}

docker run -it --network-alias z33_sink_python --network z33_network --name z33_sink_python --ip $IP z33_sink_python --host $IP --port $PORT
