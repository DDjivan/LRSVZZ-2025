#!/bin/bash

HOSTNAME=$(hostname)
name_CONFIG="client_tunnel02config.json"

if [[ "$HOSTNAME" == "raspberrypi-client"* ]]; then
    path_BASE="/home/nous/LRSVZZ-2025/fetch-ip-auto/tunnel"
    path_CONFIG="$path_BASE/$name_CONFIG"
else
    path_CONFIG="$name_CONFIG"
fi

if [[ ! -f "$path_CONFIG" ]]; then
    echo "ERROR: Configuration file not found: $path_CONFIG"
    exit 1
else
    echo "INFO: Found configuration file: $path_CONFIG"
fi

if jq -e ".\"$HOSTNAME\"" "$path_CONFIG" > /dev/null; then
  echo "INFO: Found tunnel configuration for hostname: $HOSTNAME"
else
  echo "WARN: No tunnel configuration found for hostname: $HOSTNAME"
  echo "INFO: Using default configuration."
  HOSTNAME="default"
fi

USERNAME=$(jq -r '.server_USERNAME' "$path_CONFIG")
ADDRESSEIP=$(jq -r '.server_IP' "$path_CONFIG")

LOCAL_PORT=$(jq -r ".\"$HOSTNAME\".PORT_LOCAL" "$path_CONFIG")
REMOTE_PORT=$(jq -r ".\"$HOSTNAME\".PORT_REMOTE" "$path_CONFIG")

sleep 1
echo ""

while true; do
    echo "INFO: Running $ ssh -N -R $REMOTE_PORT:localhost:$LOCAL_PORT $USERNAME@$ADDRESSEIP"
    ssh -N -R $REMOTE_PORT:localhost:$LOCAL_PORT $USERNAME@$ADDRESSEIP
    sleep 10
done
