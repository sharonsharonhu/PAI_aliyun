import requests,json

task_request = {
    "task_name": "test-secure_xgb",
    "clients": [

            {
                "role": "main_client",
                "addr": "127.0.0.1",
                "http_port": 8377,
                "client_config": {
                    "computation_port": 8378,
                    "client_type": "secure_xgboost_main",
                    "metric_func": "auc_ks",
                    "config": {
                        "learning_rate": 0.1,
                        "sync_info": {
                            "seed": 8964
                        },
                        "max_iteration": 5,
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
                    "data_path": "Data/SecureXgb_test_data/party1"
                }
            },
            {
                "role": "feature_client",
                "addr": "127.0.0.1",
                "http_port": 8082,
                "client_config": {
                    "computation_port": 8083,
                    "client_type": "secure_xgboost_feature",
                    "data_path": "Data/SecureXgb_test_data/party2"
                }
            },

            {
                "role": "label_client",
                "addr": "127.0.0.1",
                "http_port": 8884,
                "client_config": {
                    "computation_port": 8885,
                    "client_type": "secure_xgboost_label",
                    "data_path": "Data/SecureXgb_test_data/label",
                }
            }

    ]
}


print(task_request)
resp = requests.post("http://127.0.0.1:8380/createTask", json=task_request)

print(resp.status_code, resp.text)
