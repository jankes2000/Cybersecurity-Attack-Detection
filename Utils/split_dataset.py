import pandas as pd
from sklearn.model_selection import train_test_split

def split_dataset(csv_file, train_size, output_train_file, output_test_file, class_column):
    # Wczytaj dataset
    df = pd.read_csv(csv_file)
    
    # Sprawdź, czy kolumna klas istnieje
    if class_column not in df.columns:
        raise ValueError(f"Kolumna '{class_column}' nie istnieje w datasetcie.")
    
    # Wydziel kolumnę klas
    classes = df[class_column]
    
    # Wydziel cechy (wszystkie kolumny oprócz kolumny klas)
    features = df.drop(columns=[class_column])
    
    # Wykonaj split z zachowaniem proporcji klas
    X_train, X_test, y_train, y_test = train_test_split(
        features, classes, 
        train_size=train_size, 
        stratify=classes, 
        random_state=42  # Ustal seed dla powtarzalności wyników
    )
    
    # Upewnij się, że dane są poprawnie scalane
    train_df = X_train.copy()
    train_df[class_column] = y_train.values  # Używamy .values dla pewności
    
    test_df = X_test.copy()
    test_df[class_column] = y_test.values  # Używamy .values dla pewności
    
    # Zapisz wyniki do plików CSV
    train_df.to_csv(output_train_file, index=False)
    test_df.to_csv(output_test_file, index=False)
    
    print(f"Zbiór treningowy zapisany w: {output_train_file}")
    print(f"Zbiór testowy zapisany w: {output_test_file}")

# Przykład użycia
csv_file = '/mnt/c/Workspace/Cybersecurity-Attack-Detection/Data/InSDN-Dataset.csv'  # Ścieżka do pliku CSV
train_size = 0.03  # Proporcja danych do zbioru treningowego (np. 80%)
output_train_file = 'train_set.csv'  # Ścieżka do pliku wynikowego dla zbioru treningowego
output_test_file = 'test_set.csv'    # Ścieżka do pliku wynikowego dla zbioru testowego
class_column = 'Label'  # Nazwa kolumny zawierającej etykiety klas

split_dataset(csv_file, train_size, output_train_file, output_test_file, class_column)
