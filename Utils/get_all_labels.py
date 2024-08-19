import pandas as pd
from pathlib import Path


folder_obok = Path(__file__).parent.parent / 'Data'
plik = folder_obok / 'InSDN-Dataset.csv'
df = pd.read_csv(plik)

unique_labels = df['Label'].unique()

print("Unikalne wartości w kolumnie 'Label':")
for label in unique_labels:
    print(label)
