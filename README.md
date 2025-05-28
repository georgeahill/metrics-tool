# MetricsTool

Receive metrics from third-party services, then post to (Grafana? Prometheus? Something else?)

## Endpoints

GET /metrics

prometheus

POST /metric-instance
```json
{
  "source": "raspi",
  "ip": 123.123.123.123
}
```

## Usage

Log a bunch of information. Send it to Prometheus 

<!-- On start, we pull artifact from GitHub, re-run :) -->
<!-- Restart periodically? -->