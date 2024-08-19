from typing import Dict, List, Tuple, Union

from sklearn.feature_extraction import DictVectorizer
from xgboost import Booster

from mlops.utils.data_preparation.feature_engineering import combine_features
from mlops.utils.models.xgboost import build_data

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

    if 'Label' in inputs[0]:
        label_values = [input_data['Label'] for input_data in inputs]
        encoded_labels = label_encoder.transform(label_values)
        for idx, input_data in enumerate(inputs):
        input_data['Label'] = encoded_labels[idx]

    vectors = vectorizer.transform(inputs)
    predictions = model.predict(build_data(vectors))

    for idx, input_feature in enumerate(inputs):
        print(f'Prediction using these features: {predictions[idx]}')
        for key, value in input_feature.items():
            print(f'\t{key}: {value}')

    return predictions.tolist()
