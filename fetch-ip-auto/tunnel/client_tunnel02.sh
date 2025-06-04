#!/bin/bash

HOSTNAME=$(hostname)

if [[ HOSTNAME == "raspberrypi-client"* ]]; then
    CONFIG_PATH="/home/nous/LRSVZZ-2025/fetch-ip-auto/tunnel/client_tunnel02config.json"
else
    CONFIG_PATH="client_tunnel02config.json"
fi

if jq -e ".\"$HOSTNAME\"" "$CONFIG_PATH" > /dev/null; then
  echo "FOUND: Tunnel configuration for hostname: $HOSTNAME"
else
  echo "No tunnel configuration found for hostname: $HOSTNAME"
  echo "Using default configuration."
  HOSTNAME="default"
fi

USERNAME=$(jq -r '.server_USERNAME' "$CONFIG_PATH")
ADDRESSEIP=$(jq -r '.server_IP' "$CONFIG_PATH")

LOCAL_PORT=$(jq -r ".\"$HOSTNAME\".PORT_LOCAL" "$CONFIG_PATH")
REMOTE_PORT=$(jq -r ".\"$HOSTNAME\".PORT_REMOTE" "$CONFIG_PATH")

sleep 1
echo ""

while true; do
    echo $ ssh -N -R $REMOTE_PORT:localhost:$LOCAL_PORT $USERNAME@$ADDRESSEIP
    ssh -N -R $REMOTE_PORT:localhost:$LOCAL_PORT $USERNAME@$ADDRESSEIP
    sleep 10
done
