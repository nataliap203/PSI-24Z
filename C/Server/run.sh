#!/bin/bash

docker run -it --network-alias z33_server_c --network z33_network --name z33_server_c --ip 172.21.33.11 z33_server_c 172.21.33.11 8080

