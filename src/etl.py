#ETL logic
# This module contains functions for loading, cleaning, and transforming data for the customer churn prediction project.
# The ETL process includes:
# 1. Loading data from a CSV file into a pandas DataFrame.
# 2. Cleaning the data by dropping unnecessary columns and encoding categorical variables.
# 3. Returning the cleaned DataFrame for further analysis or modeling.


from typing import Optional
import pandas as pd
import os 

print(os.path.exists(r"data\raw\Customer-Churn-Records.csv"))

def load_data(file_path: str) -> Optional[pd.DataFrame]:
    """
    Load data from a CSV file into a pandas DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    Optional[pd.DataFrame]: The loaded data as a DataFrame or None if loading fails.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
    
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the DataFrame by dropping unnecessary columns and encoding categorical variables.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to be cleaned.
    
    Returns:
    pd.DataFrame: The cleaned DataFrame.
    """
    # Drop unnecessary columns
    df = df.drop(['RowNumber', 'CustomerId', 'Surname', 'Complain'], axis=1)
    
    # Convert categorical variables using One-Hot Encoding
    df = pd.get_dummies(df, columns=['Geography', 'Gender', 'Card Type'], drop_first=True)
    
    return df

def run_etl() -> Optional[pd.DataFrame]:
    """
    Run the ETL process: load data, clean it, and return the cleaned DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    Optional[pd.DataFrame]: The cleaned DataFrame or None if loading fails.
    """
    print("Starting ETL process...")
    raw_path = os.path.join("data", "raw", "Customer-Churn-Records.csv")
    processed_path = os.path.join("data", "processed", "cleaned_churn_data.csv")

    if not os.path.exists(raw_path):
        print(f"Error: No dataset found at {raw_path}. Please download the Kaggle dataset and place it there.")
        return

    df = load_data(raw_path)
    if df is None:
        print("ETL aborted due to failed data loading.")
        return None

    clean_df = clean_data(df)
    
    # Save processed data
    os.makedirs("data/processed", exist_ok=True)
    clean_df.to_csv(processed_path, index=False)
    print(f"ETL complete. Data saved to {processed_path}")
    return clean_df

if __name__ == "__main__":
    run_etl()


