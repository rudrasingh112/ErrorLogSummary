import requests

url = "http://127.0.0.1:8000/ingest"
data = {
  "level": "ERROR",
  "service_name": "payment-processor",
  "message": "External API Error: Stripe API returned a 503 Service Unavailable.",
  "metadata": {
    "provider": "Stripe",
    "retry_count": 2,
    "request_id": "req_zA92kL1"
  }
}

response = requests.post(url, json=data)
print(response)