import requests
resp = requests.get("http://127.0.0.1:8380/startTask", params={"task_name": "test_secure_xgb"})
# resp = requests.get("http://101.133.214.221:8380/startTask", params={"task_name": "test-secure_xgb_1"})
print(resp.status_code, resp.text)
