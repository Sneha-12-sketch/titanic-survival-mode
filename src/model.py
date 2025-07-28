import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def preprocess(df):
    df = df.drop(["Name", "Ticket", "Cabin"], axis=1)
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
    df["Embarked"] = df["Embarked"].map({"C": 0, "Q": 1, "S": 2})
    df = df.fillna(df.median(numeric_only=True))
    return df

def train_model():
    data = pd.read_csv("../data/train.csv")
    y = data["Survived"]
    X = data.drop("Survived", axis=1)
    X = preprocess(X)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    joblib.dump(model, "../titanic_model.pkl")
    print("✅ Model trained and saved as titanic_model.pkl")

if __name__ == "__main__":
    train_model()