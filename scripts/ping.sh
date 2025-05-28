#!/bin/bash
set -e

IP_ADDRESS=$(curl -s -S https://ipinfo.io/ip)

echo "Logging from $IP_ADDRESS"

REQ_BODY=$(jq -n --arg ip "$IP_ADDRESS" --arg service "raspi-ping" '{ip_address: $ip, caller: $service}')

set +e
echo $(curl -s -S -X POST -H "Content-Type: application/json" "http://localhost:8000/metric-instance" --data-raw "$REQ_BODY")
echo $(curl -s -S -X POST -H "Content-Type: application/json" "http://192.168.178.21:8000/metric-instance" --data-raw "$REQ_BODY")
echo $(curl -s -S -X POST -H "Content-Type: application/json" "http://data.georgehill.xyz/metric-instance" --data-raw "$REQ_BODY")
echo $(curl -s -S -X POST -H "Content-Type: application/json" "http://135.181.89.0:8080/metric-instance" --data-raw "$REQ_BODY")