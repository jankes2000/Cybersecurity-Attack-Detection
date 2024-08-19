from typing import Dict, List, Tuple, Union
import mlflow.xgboost

from sklearn.feature_extraction import DictVectorizer
from xgboost import Booster
from sklearn.preprocessing import LabelEncoder

from mlops.utils.data_preparation.feature_engineering import combine_features
from mlops.utils.models.xgboost import build_data

import mlflow
from mlflow import MlflowClient

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom

DEFAULT_INPUTS = [
    {
        'Protocol': 6,
        'FIN Flag Cnt': 0,
        'Init Bwd Win Byts': -1,
        'SYN Flag Cnt': 0,
        'Down/Up Ratio': 0,
        'Src Port': 80,
        'Dst Port': 443,
        'ACK Flag Cnt': 1,
        'Bwd Header Len': 64,
        'Fwd Pkt Len Min': 0,
        'Flow ID': '192.168.20.133-205.196.120.6-55200-443-6',
        'Src IP': '205.196.120.6',
        'Dst IP': '192.168.20.133',
        'Timestamp': '5/2/2020 12:33'
    },
    {
        'Protocol': 6,
        'FIN Flag Cnt': 1,
        'Init Bwd Win Byts': 63,
        'SYN Flag Cnt': 0,
        'Down/Up Ratio': 0,
        'Src Port': 80,
        'Dst Port': 43678,
        'ACK Flag Cnt': 1,
        'Bwd Header Len': 64,
        'Fwd Pkt Len Min': 0,
        'Flow ID': '192.168.3.130-200.175.2.130-80-43678-6',
        'Src IP': '192.168.3.130',
        'Dst IP': '200.175.2.130',
        'Timestamp': '9/1/2020 16:33'
    },
]

DEFAULT_MODEL_NAME = "Booster"

def get_best_model_version(model_name: str = DEFAULT_MODEL_NAME) -> Tuple[str, float]:
    mlflow.set_tracking_uri('http://mlflow:5000')

    client = MlflowClient()
    # Get all versions of the model
    model_versions = client.search_model_versions(f"name='{model_name}'")
    

    models = client.search_registered_models()
    for model in models:
        print(f"Model Name: {model.name}, Description: {model.description}")
    
    best_version = None
    best_rmse = float('inf')  # Assuming lower RMSE is better

    for version in model_versions:
        # Get the run ID associated with the model version
        run_id = version.run_id
        
        # Fetch metrics from the run
        metrics = client.get_run(run_id).data.metrics
        rmse = metrics.get('rmse', float('inf'))  # Change 'rmse' if needed
        
        if rmse < best_rmse:
            best_rmse = rmse
            best_version = version.version
    
    return best_version, best_rmse


def load_best_model(model_name: str, version: str) -> mlflow.pyfunc.PythonModel:
    #model_uri = f"models/{model_name}/versions/{version}"
    model_uri = "mlflow-artifacts:/0/2a76b0b39ce14da195c34f24ae8b667d/artifacts/models"
    model = mlflow.xgboost.load_model(model_uri)
    return model

@custom
def predict(
    model_settings: Dict[str, Tuple[Booster, DictVectorizer, LabelEncoder]],
    **kwargs,
) -> List[float]:
    inputs: List[Dict[str, Union[float, int, str]]] = kwargs.get('inputs', DEFAULT_INPUTS)
    #inputs = combine_features(inputs)

    Protocol = kwargs.get('Protocol')
    FIN_Flag_Cnt = kwargs.get('FIN Flag Cnt')
    Init_Bwd_Win_Byts = kwargs.get('Init Bwd Win Byts')
    SYN_Flag_Cnt = kwargs.get('SYN Flag Cnt')
    Down_Up_Ratio = kwargs.get('Down/Up Ratio')
    Src_Port = kwargs.get('Src Port')
    Dst_Port = kwargs.get('Dst Port')
    ACK_Flag_Cnt = kwargs.get('ACK Flag Cnt')
    Bwd_Header_Len = kwargs.get('Bwd Header Len')
    Fwd_Pkt_Len_Min = kwargs.get('Fwd Pkt Len Min')
    Flow_ID = kwargs.get('Flow ID')
    Src_IP = kwargs.get('Src IP')
    Dst_IP = kwargs.get('Dst IP')
    Timestamp = kwargs.get('Timestamp')

    if any(v is not None for v in [Protocol, FIN_Flag_Cnt, Init_Bwd_Win_Byts, SYN_Flag_Cnt, Down_Up_Ratio, Src_Port, Dst_Port, ACK_Flag_Cnt, Bwd_Header_Len, Fwd_Pkt_Len_Min, Flow_ID, Src_IP, Dst_IP, Timestamp]):
        inputs = [
            {
                'Protocol': Protocol,
                'FIN Flag Cnt': FIN_Flag_Cnt,
                'Init Bwd Win Byts': Init_Bwd_Win_Byts,
                'SYN Flag Cnt': SYN_Flag_Cnt,
                'Down/Up Ratio': Down_Up_Ratio,
                'Src Port': Src_Port,
                'Dst Port': Dst_Port,
                'ACK Flag Cnt': ACK_Flag_Cnt,
                'Bwd Header Len': Bwd_Header_Len,
                'Fwd Pkt Len Min': Fwd_Pkt_Len_Min,
                'Flow ID': Flow_ID,
                'Src IP': Src_IP,
                'Dst IP': Dst_IP,
                'Timestamp': Timestamp,
            },
        ]

    model, vectorizer, label_encoder = model_settings['xgboost']

    best_version, best_rmse = get_best_model_version()

    model_mlflow = load_best_model(DEFAULT_MODEL_NAME, best_version)

    vectors = vectorizer.transform(inputs)


    predictions = model.predict(build_data(vectors))

  
    decoded_predictions = label_encoder.inverse_transform(predictions.round().astype(int))

    for idx, input_feature in enumerate(inputs):
        print(f'Prediction using these features: {decoded_predictions[idx]}')
        for key, value in input_feature.items():
            print(f'\t{key}: {value}')

    return decoded_predictions.tolist()
