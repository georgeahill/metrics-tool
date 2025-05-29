from prometheus_client import Counter

request_metric = Counter("metrictool_request", ["ip_address", "caller"])