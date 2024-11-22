#!/bin/bash

docker exec z33_source_python tc qdisc add dev eth0 root netem delay 1000ms 500ms loss 50%
