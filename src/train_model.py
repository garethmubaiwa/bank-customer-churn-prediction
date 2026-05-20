#model training logic
# This module contains functions for training a machine learning model for customer churn prediction.
# The training process includes:
# 1. Loading the cleaned data from a CSV file.
# 2. Splitting the data into features and target variable.
# 3. Performing a train-test split to create training and testing datasets.
# 4. Training a Random Forest Classifier on the training data.
# 5. Evaluating the model's performance on the test data and printing the classification report

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

def train_model(model_type: str) -> None:
    """
    Train a Random Forest Classifier on the cleaned data and save the model to disk.
    
    Parameters:
    data_path (str): The path to the cleaned data CSV file.
    model_path (str): The path where the trained model will be saved.
    """
    # Load the cleaned data
    print(f"Loading data from data/processed/cleaned_churn_data.csv...")
    df = pd.read_csv("data/processed/cleaned_churn_data.csv")
    
    # Split data into features and target variable
    X = df.drop('Exited', axis=1)  # Features
    y = df['Exited']  # Target variable
    
    # Perform train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model_type = model_type.lower()
    if model_type == "xgboost":
        print("Training the XGBoost Classifier...")
        scale_pos_weight = (y_train == 0).sum() / (y_train == 1).sum()
        model = XGBClassifier(n_estimators=100, random_state=42, scale_pos_weight=scale_pos_weight)
    elif model_type == "random_forest":
        # Train a Random Forest Classifier
        print("Training the Random Forest Classifier...")
        model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
    else:
        raise ValueError("Invalid model type. Choose 'random_forest' or 'xgboost'.")
    model.fit(X_train, y_train)
    
    # Make predictions on the test set
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # Evaluate the model's performance
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print(f"Accuracy: {accuracy*100:.2f}%")
    
    # Save the trained model to disk
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, f"models/churn_{model_type}_model.joblib")
    print(f"Model saved to models/churn_{model_type}_model.joblib")
    joblib.dump(list(X.columns), f"models/churn_{model_type}_model_features.joblib")
    print(f"Model features saved to models/churn_{model_type}_model_features.joblib")
    print("Model training completed successfully.")

if __name__ == "__main__":
    train_model("random_forest")  # Can be changed to "xgboost" to train the XGBoost model instead

