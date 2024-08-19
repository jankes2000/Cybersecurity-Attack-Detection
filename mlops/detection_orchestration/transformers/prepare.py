from typing import Tuple

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel

from mlops.utils.data_preparation.cleaning import clean
from mlops.utils.data_preparation.feature_engineering import combine_features
from mlops.utils.data_preparation.feature_selector import select_features
from mlops.utils.data_preparation.splitters import split_on_ratio



if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def transform(
    df: pd.DataFrame, **kwargs
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    split_on_feature = kwargs.get('split_on_feature')
    split_on_feature_value = kwargs.get('split_on_feature_value')
    target = kwargs.get('target')
    train_size = kwargs.get('train_size')

    #df = clean(df)
    #df = combine_features(df)
    #print(target)
    classes = df[target]
    features = df.drop(columns=[target])

    
    df_train, df_val = split_on_ratio(
        df,
        0.3
    )


    #   X_train, X_val, dv = vectorize_features(
    #     select_features(df_train),
    #     select_features(df_val),
    # )

    # df_train, df_val = train_test_split(
    #     features, classes, 
    #     train_size=train_size, 
    #     stratify=classes, 
    #     random_state=42 
    # )

    # df_train = df
    # df_val = df




    return df, df_train, df_val
