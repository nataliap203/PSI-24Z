#!/bin/bash

docker run -it --network-alias z33_client_c --network z33_network --name z33_client_c z33_client_c 172.21.33.11 8080
