import requests, json

task_request = {
    "task_name": "test_secure_xgb",
    "clients": [

        {
            "role": "main_client",
            "addr": "127.0.0.1",
            "http_port": 8377,
            "client_config": {
                "computation_port": 8378,
                "client_type": "secure_xgboost_main",
                "metric": "metrics_pack2",
                "config": {
                    "learning_rate": 0.1,
                    "sync_info": {
                        "seed": 8964
                    },
                    "max_iteration": 8,
                    "max_depth": 4,
                    "reg_lambda": 1,
                    "gamma": 0.,
                    "col_sample_ratio": 0.8,
                    "row_sample_ratio": 1.,
                    "batch_size": None,
                    "test_batch_size": None
                }
            }
        },
        {
            "role": "feature_client",
            "addr": "127.0.0.1",
            "http_port": 8084,
            "client_config": {
                "computation_port": 8085,
                "client_type": "secure_xgboost_feature",
                "data_path": "test-f1"
            }
        },
        {
            "role": "feature_client",
            "addr": "127.0.0.1",
            "http_port": 8082,
            "client_config": {
                "computation_port": 8083,
                "client_type": "secure_xgboost_feature",
                "data_path": "test-f2"
            }
        },
        {
            "role": "crypto_producer",
            "addr": "127.0.0.1",
            "http_port": 6666,
            "client_config": {
                "client_type": "triplet_producer",
                "computation_port": 6699,
                "listen_clients": [2, 3]
            }
        },

        {
            "role": "label_client",
            "addr": "127.0.0.1",
            "http_port": 8884,
            "client_config": {
                "computation_port": 8885,
                "client_type": "secure_xgboost_label",
                "data_path": "test-l",
                "metric": "metrics_pack2",

            }
        }

    ]
}

print(task_request)
resp = requests.post("http://127.0.0.1:8380/createTask", json=task_request)
# resp = requests.post("http://101.133.214.221:8380/createTask", json=task_request)
print(resp.status_code, resp.text)


