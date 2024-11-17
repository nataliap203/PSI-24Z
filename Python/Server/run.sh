#!/bin/bash

docker run -it --network-alias z33_server_python --network z33_network --name z33_server_python --ip 172.21.33.21 z33_server_python --host 172.21.33.21 --port 8080 
