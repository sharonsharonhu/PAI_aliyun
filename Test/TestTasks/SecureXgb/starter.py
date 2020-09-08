import requests
resp = requests.get("http://127.0.0.1:8380/startTask", params={"task_name": "test-secure_xgb"})
print(resp.status_code, resp.text)
