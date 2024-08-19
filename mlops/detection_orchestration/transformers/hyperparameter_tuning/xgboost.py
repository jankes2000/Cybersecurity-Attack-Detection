from typing import Dict, Tuple, Union

import numpy as np
import xgboost as xgb
from pandas import Series, DataFrame
from scipy.sparse._csr import csr_matrix

from mlops.utils.logging import track_experiment
from mlops.utils.models.xgboost import build_data, tune_hyperparameters
from sklearn.preprocessing import LabelEncoder

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def hyperparameter_tuning(
    training_set: Dict[str, Union[Series, csr_matrix]],
    **kwargs,
) -> Tuple[
    Dict[str, Union[bool, float, int, str]],
    csr_matrix,
    Series,
]:
    X, X_train, X_val, y, y_train, y_val, _ = training_set['build']
    #X_train, X_val, y_train, y_val = training_set['build']
    label_encoder = LabelEncoder()
    if y_train.dtype == 'object' or isinstance(y_train.iloc[0], str):
        y_train = label_encoder.fit_transform(y_train)
        y_val = label_encoder.transform(y_val)

    y_train = DataFrame(y_train, columns=['label'])
    y_val = DataFrame(y_val, columns=['label'])


    training = build_data(X_train, y_train)
    validation = build_data(X_val, y_val)

    best_hyperparameters = tune_hyperparameters(
        training,
        validation,
        callback=lambda **opts: track_experiment(**{**opts, **kwargs}),
        **kwargs,
    )

    return best_hyperparameters, X_train, y_train, transform
