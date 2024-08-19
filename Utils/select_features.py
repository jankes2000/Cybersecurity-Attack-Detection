import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split

data = pd.read_csv("../Data/train_set.csv")
categorical_cols = ["Flow ID", "Src IP", "Src Port", "Dst IP", "Dst Port", "Protocol", "Timestamp"]
X = data.drop(columns=["Label"])
y = data["Label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = ExtraTreesClassifier(random_state=42)
model.fit(X_train.select_dtypes(include=["number"]), y_train)
important_features = pd.Series(model.feature_importances_, index=X_train.select_dtypes(include=["number"]).columns).nlargest(10).index

selected_cols = list(important_features) + categorical_cols
X_selected = X[selected_cols]
X_selected["Label"] = y
X_selected.to_csv("../Data/train_set_selected.csv", index=False)


# import pandas as pd
# from sklearn.feature_selection import SelectKBest, f_classif

# def select_important_features(input_csv, output_csv, target_column, num_features):
#     df = pd.read_csv(input_csv)
#     X = df.drop(columns=[target_column])
#     y = df[target_column]
    
#     # Przekształcenie kolumn tekstowych na kategorie liczbowe lub one-hot encoding
#     X_encoded = pd.get_dummies(X, drop_first=True)

#     selector = SelectKBest(score_func=f_classif, k=num_features)
#     X_new = selector.fit_transform(X_encoded, y)
    
#     selected_features = X_encoded.columns[selector.get_support()]
#     df_new = pd.DataFrame(X_new, columns=selected_features)
#     df_new[target_column] = y
    
#     df_new.to_csv(output_csv, index=False)

# input_csv = '/mnt/c/Workspace/Cybersecurity-Attack-Detection/Data/train_set.csv'
# output_csv = '/mnt/c/Workspace/Cybersecurity-Attack-Detection/Data/train_set_selected.csv'
# target_column = 'Label'
# num_features = 10

# select_important_features(input_csv, output_csv, target_column, num_features)