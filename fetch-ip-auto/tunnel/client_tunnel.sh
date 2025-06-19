#!/bin/bash

if [[ $(uname -n) == *"raspberrypi"* ]]; then
    CONFIG_PATH="/home/nous/LRSVZZ-2025/fetch-ip-auto/tunnel/client_tunnelconfig.json"
else
    CONFIG_PATH="client_tunnelconfig.json"
fi

PORT=$(jq -r '.PORT' "$CONFIG_PATH")
USERNAME=$(jq -r '.USERNAME' "$CONFIG_PATH")
ADDRESSEIP=$(jq -r '.ADDRESSEIP' "$CONFIG_PATH")



sleep 30

while true; do
    ssh -R 50001:localhost:22 dd@90.22.255.6 -N >> /home/nous/ssh_tunnel.log 2>&1
    sleep 10
done
