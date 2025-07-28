import pandas as pd
import joblib
from voice import sitara_response
import time

def preprocess(df):
    df = df.drop(["Name", "Ticket", "Cabin"], axis=1)
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
    df["Embarked"] = df["Embarked"].map({"C": 0, "Q": 1, "S": 2})
    df = df.fillna(df.median(numeric_only=True))
    return df

def predict_csv(file_path):
    model = joblib.load("../titanic_model.pkl")
    data = pd.read_csv(file_path)
    names = data["Name"]
    X = preprocess(data)
    
    predictions = model.predict(X)
    
    for name, pred in zip(names, predictions):
        sitara_response(name.split(",")[0], pred)
        time.sleep(1.5)  # Pause for 1 second between responses

if __name__ == "__main__":
    predict_csv("../data/test.csv")