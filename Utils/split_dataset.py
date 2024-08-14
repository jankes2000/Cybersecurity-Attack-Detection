import pandas as pd
from sklearn.model_selection import train_test_split

def split_dataset(csv_file, train_size, output_train_file, output_test_file, class_column):
    df = pd.read_csv(csv_file)
    
    if class_column not in df.columns:
        raise ValueError(f"Kolumna '{class_column}' nie istnieje w datasetcie.")

    classes = df[class_column]

    features = df.drop(columns=[class_column])

    X_train, X_test, y_train, y_test = train_test_split(
        features, classes, 
        train_size=train_size, 
        stratify=classes, 
        random_state=42 
    )
    
    train_df = X_train.copy()
    train_df[class_column] = y_train.values
    
    test_df = X_test.copy()
    test_df[class_column] = y_test.values
    
    train_df.to_csv(output_train_file, index=False)
    test_df.to_csv(output_test_file, index=False)
    
    print(f"Zbiór treningowy zapisany w: {output_train_file}")
    print(f"Zbiór testowy zapisany w: {output_test_file}")

csv_file = '/mnt/c/Workspace/Cybersecurity-Attack-Detection/Data/InSDN-Dataset.csv'
train_size = 0.03
output_train_file = 'train_set.csv'
output_test_file = 'test_set.csv'
class_column = 'Label'

split_dataset(csv_file, train_size, output_train_file, output_test_file, class_column)
