#!/bin/bash

docker run -it --rm --network-alias z33_client_python --network z33_network --name z33_client_python z33_client_python --host 172.21.33.11 --port 8080
