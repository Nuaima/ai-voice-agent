import requests

BASE_URL = "http://127.0.0.1:8000"
def post_json(endpoint, payload):
    url = f"{BASE_URL}{endpoint}"
    try:
        resp = requests.post(url, json=payload, timeout=10)
        try:
            data = resp.json()
        except ValueError:
            print(f"Response is not JSON from {endpoint}:")
            print(resp.text)
            return resp.status_code, None
        return resp.status_code, data
    except requests.exceptions.RequestException as e:
        print(f"Error calling {endpoint}: {e}")
        return None, None

# -------------------------
# Test /start-call
# -------------------------
start_call_payload = {
    "driver_name": "John Doe",
    "phone_number": "123-456-7890",
    "load_number": "LOAD123"
}
status, data = post_json("/start-call", start_call_payload)
print("----- /start-call -----")
print(status, data)

# -------------------------
# Test /retell-webhook
# -------------------------
retell_payload = {
    "speech_text": "Hi, I have a question about my delivery schedule."
}
status, data = post_json("/retell-webhook", retell_payload)
print("----- /retell-webhook -----")
print(status, data)

# -------------------------
# Test /post-call
# -------------------------
post_call_payload = {
    "driver_name": "John Doe",
    "load_number": "LOAD123",
    "transcript": "Driver: I will be late by 30 minutes. Agent: Noted, please update."
}
status, data = post_json("/post-call", post_call_payload)
print("----- /post-call -----")
print(status, data)
