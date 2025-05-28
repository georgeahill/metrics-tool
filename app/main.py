from prometheus_client import Counter, make_asgi_app
import random,time
from fastapi import FastAPI

# Create app
app = FastAPI(debug=False)

# Add prometheus asgi middleware to route /metrics requests
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

@app.get("/health-check")
def healthcheck():
  return {"status": "Happy :)"}

@app.post("/metric-instance")
def create_metric(body):
  request_metric = Counter("metrictool_request", body.keys())

  request_metric.labels(**body)

  request_metric.increment()