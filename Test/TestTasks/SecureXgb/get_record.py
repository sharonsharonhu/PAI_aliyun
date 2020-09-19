import requests
# resp = requests.get("http://127.0.0.1:8380/queryRecord", params={"query": "record","task_name": "test_secure_xgb",
#             "client_id":-1})
resp = requests.get("http://127.0.0.1:8380/queryTask", params={"task_name": "test_secure_xgb","query": "record",
            "client":-1})

print(resp.status_code, resp.text)