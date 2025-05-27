from prometheus_client import Counter, make_asgi_app
import random,time
from fastapi import FastAPI

app = FastAPI()

def make_metrics_app():
  registry = CollectorRegistry()
  multiprocess.MultiProcessCollector(registry)
  return make_asgi_app(registry=registry)

metrics_app = make_metrics_app()
app.mount("/metrics", metrics_app)

@app.get("/health-check")
def healthcheck():
  return {"status": "Happy :)"}

@app.post("/metric-instance")
def create_metric(body):
  request_metric = Counter("metrictool_request")

  request_metric.labels()

  request_metric.increment()
  

# metric = Counter('metric_request_total', 'Decsription')

# def generate_metric():
#   return {"a": 1, "b": "aaa"}

# if __name__ == '__main__':
#   start_http_server(8000)

#   while True:
#     m = generate_metric()
#     print(f'metric is {m}')
#     metric.increment(m)

#     time.sleep(30)