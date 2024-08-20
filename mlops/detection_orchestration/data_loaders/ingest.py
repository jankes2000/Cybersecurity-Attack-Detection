import os
import requests
from io import BytesIO
from typing import List

import pandas as pd

if "data_loader" not in globals():
    from mage_ai.data_preparation.decorators import data_loader


@data_loader
def ingest_files(**kwargs) -> pd.DataFrame:
    dfs: List[pd.DataFrame] = []

    base_dir = "/home/src/Data"
    filename = "train_set_selected.csv"
    file_path = os.path.join(base_dir, filename)

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File {file_path} not found.")

    df = pd.read_csv(file_path)
    dfs.append(df)

    return pd.concat(dfs, ignore_index=True)
