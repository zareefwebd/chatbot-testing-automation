import requests
import pytest
from jsonschema import validate

# Replace with your chatbot API base url for real testing
# Example demo URL (Postman Echo): "https://postman-echo.com"
BASE_URL = "https://postman-echo.com"  # <--- change if you have real API

def test_healthcheck():
    """API health check must return 200 (demo: GET /get)"""
    # For demo echo endpoint we call /get
    url = f"{BASE_URL}/get"
    r = requests.get(url, timeout=10)
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, dict)

def test_chat_response_schema():
    """Chat endpoint should return expected JSON schema for a message (demo: /post)"""
    url = f"{BASE_URL}/post"
    payload = {"user_id": "test_user", "message": "Hello"}
    r = requests.post(url, json=payload, timeout=10)
    assert r.status_code == 200
    data = r.json()
    # Postman-echo returns a 'json' field containing the payload. We'll validate that structure.
    assert "json" in data
    schema = {
        "type": "object",
        "properties": {
            "json": {"type": "object"}
        },
        "required": ["json"]
    }
    validate(instance=data, schema=schema)

def test_chat_flow_specific_response():
    """Functional test simulated: check if reply contains expected keywords (demo)"""
    url = f"{BASE_URL}/post"
    payload = {"user_id": "user1", "message": "What are your timings?"}
    r = requests.post(url, json=payload, timeout=10)
    assert r.status_code == 200
    data = r.json()
    # In real API you would assert content of 'reply'. For demo we assert 'json' matches payload.
    assert data.get("json", {}).get("message") == payload["message"]
