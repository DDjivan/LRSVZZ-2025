#!/bin/bash

if [[ $(uname -n) == *"raspberrypi"* ]]; then
    CONFIG_PATH="/home/nous/LRSVZZ-2025/fetch-ip-auto/tunnel/client_tunnelconfig.json"
else
    CONFIG_PATH="client_tunnelconfig.json"
fi

PORT=$(jq -r '.PORT' "$CONFIG_PATH")
USERNAME=$(jq -r '.USERNAME' "$CONFIG_PATH")
ADDRESSEIP=$(jq -r '.ADDRESSEIP' "$CONFIG_PATH")

echo "Port: $PORT"
echo "Username: $USERNAME"
echo "IP Address: $ADDRESSEIP"
