import logging

from prometheus_client import Counter, make_asgi_app
from fastapi import FastAPI, Request

# Create app
app = FastAPI(debug=False)

# Add prometheus asgi middleware to route /metrics requests
metrics_app = make_asgi_app()
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