import logging

from prometheus_client import make_asgi_app
from fastapi import FastAPI, Request

from .metrics import request_metric

# Create app
app = FastAPI(debug=False)

# Add prometheus asgi middleware to route /metrics requests
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

@app.get("/health-check")
def healthcheck():
  return {"status": "Happy :)"}



@app.post("/metric-instance")
async def create_metric(request: Request):
  body = await request.json()

  logging.info(body)

  request_metric.labels(**body).inc()