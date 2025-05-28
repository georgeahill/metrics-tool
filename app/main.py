import logging
import multiprocessing

from prometheus_client import Counter, make_asgi_app, CollectorRegistry
from fastapi import FastAPI, Request

# Create app
app = FastAPI(debug=False)

# Using multiprocess collector for registry
def make_metrics_app():
    registry = CollectorRegistry()
    multiprocessing.MultiProcessCollector(registry)
    return make_asgi_app(registry=registry)


# Add prometheus asgi middleware to route /metrics requests
metrics_app = make_metrics_app()
app.mount("/metrics", metrics_app)

@app.get("/health-check")
def healthcheck():
  return {"status": "Happy :)"}

request_metric = Counter("metrictool_request", ["ip_address", "caller"])

@app.post("/metric-instance")
async def create_metric(request: Request):
  body = await request.json()

  logging.info(body)

  request_metric.labels(**body)

  request_metric.increment()