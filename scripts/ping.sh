set -e

IP_ADDRESS=$(curl -s -S https://ipinfo.io/ip)

echo "Logging from $IP_ADDRESS"

REQ_BODY=$(jq -n --arg ip "$IP_ADDRESS" --arg service "raspi-ping" '{ip_addresss: $ip, caller: $service}')

unset -e
curl -s -S -X POST "http://localhost:8000/metric-instance" --data-raw "$REQ_BODY"
curl -s -S -X POST "http://192.168.178.21:8000/metric-instance" --data-raw "$REQ_BODY"
curl -s -S -X POST "http://data.georgehill.xyz/metric-instance" --data-raw "$REQ_BODY"