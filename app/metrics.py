from prometheus_client import Counter

request_metric = Counter("metrictool_request", "requests", ["ip_address", "caller"])