import os
import requests
from io import BytesIO
from typing import List

import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader


@data_loader
def ingest_files(**kwargs) -> pd.DataFrame:
    dfs: List[pd.DataFrame] = []

    # Ścieżka do katalogu, w którym znajduje się plik CSV
    base_dir = '/home/src/Data'  # Zaktualizuj tę ścieżkę
    filename = 'train_set.csv'  # Stała nazwa pliku CSV
    file_path = os.path.join(base_dir, filename)
    
    # Sprawdź, czy plik istnieje
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Plik {file_path} nie istnieje.")
    
    # Wczytaj dane CSV do DataFrame
    df = pd.read_csv(file_path)
    dfs.append(df)
    
    # Połącz wszystkie DataFrame'y (w tym przypadku tylko jeden)
    return pd.concat(dfs, ignore_index=True)
