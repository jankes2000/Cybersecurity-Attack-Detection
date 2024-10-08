# Sample online inference

    curl --location 'http://localhost:6789/api/runs' \
    --header 'Authorization: Bearer ef46ef6d89f44853b3d31ef771991bc5' \
    --header 'Content-Type: application/json' \
    --header 'Cookie: lng=en' \
    --data '{
        "run": {
            "pipeline_uuid": "predict",
            "block_uuid": "inference",
            "variables": {
                "inputs": [
                    {
                        "Protocol": 6,
                        "FIN Flag Cnt": 0,
                        "Init Bwd Win Byts": -1,
                        "SYN Flag Cnt": 0,
                        "Down/Up Ratio": 0,
                        "Src Port": 80,
                        "Dst Port": 443,
                        "ACK Flag Cnt": 1,
                        "Bwd Header Len": 64,
                        "Fwd Pkt Len Min": 0,
                        "Flow ID": "192.168.20.133-205.196.120.6-55200-443-6",
                        "Src IP": "205.196.120.6",
                        "Dst IP": "192.168.20.133",
                        "Timestamp": "5/2/2020 12:33"
                    },
                    {
                        "Protocol": 6,
                        "FIN Flag Cnt": 1,
                        "Init Bwd Win Byts": 63,
                        "SYN Flag Cnt": 0,
                        "Down/Up Ratio": 0,
                        "Src Port": 80,
                        "Dst Port": 43678,
                        "ACK Flag Cnt": 1,
                        "Bwd Header Len": 64,
                        "Fwd Pkt Len Min": 0,
                        "Flow ID": "192.168.3.130-200.175.2.130-80-43678-6",
                        "Src IP": "192.168.3.130",
                        "Dst IP": "200.175.2.130",
                        "Timestamp": "9/1/2020 16:33"
                    }
                ]
            }
        }
    }'


## Note

The `Authorization` header is using this pipeline’s API trigger’s token value.
The token value is set to `fire` for this project.
If you create a new trigger, that token will change.
Only use a fixed token for testing or demonstration purposes.