#!/bin/bash
exec > /tmp/client_tunnel.log 2>&1
echo "Starting client_tunnel.sh at $(date)"

if [[ $(uname -n) == *"raspberrypi"* ]]; then
    source /home/nous/LRSVZZ-2025/fetch-ip-auto/tunnel/client_tunnelconfig.cfg
else
    source ./client_tunnelconfig.cfg
fi

while true; do
    ssh -R $PORT:localhost:22 $USERNAME@$ADDRESSEIP
    sleep 10
done
