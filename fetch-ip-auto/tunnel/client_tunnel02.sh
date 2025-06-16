#!/bin/bash

HOSTNAME=$(hostname)
name_CONFIG="client_tunnel02config.json"

echoT() {
    echo "$(date '+%Y-%m-%d %H:%M:%S.%6N') — $*"
}

if [[ "$HOSTNAME" == "raspberrypi-client"* ]]; then
    path_BASE="/home/nous/LRSVZZ-2025/fetch-ip-auto/tunnel"
    path_CONFIG="$path_BASE/$name_CONFIG"
else
    path_CONFIG="$name_CONFIG"
fi

if [[ ! -f "$path_CONFIG" ]]; then
    echoT "ERROR: Configuration file not found: $path_CONFIG"
    exit 1
else
    echoT "INFO: Found configuration file: $path_CONFIG"
fi

if jq -e ".\"$HOSTNAME\"" "$path_CONFIG" > /dev/null; then
  echoT "INFO: Found tunnel configuration for hostname: $HOSTNAME"
else
  echoT "WARN: No tunnel configuration found for hostname: $HOSTNAME"
  echoT "INFO: Using default configuration."
  HOSTNAME="default"
fi

USERNAME=$(jq -r '.server_USERNAME' "$path_CONFIG")
ADDRESSEIP=$(jq -r '.server_IP' "$path_CONFIG")

LOCAL_PORT=$(jq -r ".\"$HOSTNAME\".PORT_LOCAL" "$path_CONFIG")
REMOTE_PORT=$(jq -r ".\"$HOSTNAME\".PORT_REMOTE" "$path_CONFIG")



while true; do
    sleep 2
    echo ""
    echoT "INFO: Running $ ssh -N -R $REMOTE_PORT:localhost:$LOCAL_PORT $USERNAME@$ADDRESSEIP"
    ssh -N -R $REMOTE_PORT:localhost:$LOCAL_PORT $USERNAME@$ADDRESSEIP
    sleep 8
done

# END #