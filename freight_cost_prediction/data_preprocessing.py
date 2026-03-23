import sqlite3
from sklearn.model_selection import train_test_split
import pandas as pd

# def load_vendor_invoice_data(db_path: str):
#     """
#     Load vendor invoice data from CSV (since DB table missing).
#     """
#     import os

#     # Correct absolute path (your Data folder is in C:\Users\samay)
#     csv_path = r"C:\Users\samay\Data\vendor_invoice.csv"

#     # Optional: Check if file exists (helpful for debugging)
#     if not os.path.exists(csv_path):
#         raise FileNotFoundError(
#             f"CSV file not found at: {csv_path}\n"
#             f"Current working directory: {os.getcwd()}\n"
#             f"Tip: File is in C:\\Users\\samay\\Data folder"
#         )

#     df = pd.read_csv(csv_path)
#     print(f"Successfully loaded {len(df)} rows from {csv_path}")
#     return df

def load_vendor_invoice_data(db_path: str = None):
    """
    Load vendor invoice data from CSV using the fixed absolute path.
    """
    import os
    import pandas as pd

    # Aapka bataya hua shortcut path
    csv_path = r"C:\Users\samay\Downloads\invoice_intelligence_system\data\vendor_invoice.csv"

    # Check if file exists
    if not os.path.exists(csv_path):
        raise FileNotFoundError(
            f"CSV file nahi mili! Is path par check karein: {csv_path}\n"
            f"Tip: Pakka karlein ki 'data' folder ke andar 'vendor_invoice.csv' file maujood hai."
        )

    # File read karna
    df = pd.read_csv(csv_path)
    print(f"Successfully loaded {len(df)} rows from {csv_path}")
    
    return df

def prepare_features (df: pd.DataFrame):
    """
    Select features and target variable.
    """
    X = df [["Dollars"]]
    y = df ["Freight"]
    return X, y

def split_data(X, y, test_size=0.2, random_state=42):
    """
    Split dataset into train and test sets.
    """
    return train_test_split( 
        X, y, test_size=test_size, random_state=random_state

)