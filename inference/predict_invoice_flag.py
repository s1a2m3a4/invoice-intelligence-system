
# import pandas as pd
# import joblib
# import os

# def predict_invoice_flag(input_df):
#     # 1. Model aur Scaler ke sahi paths (Absolute paths use karein)
#     model_path = r'C:\Users\samay\Downloads\invoice_intelligence_system\models\predict_flag_invoice.pkl'
#     scaler_path = r'C:\Users\samay\Downloads\invoice_intelligence_system\models\scaler.pkl'

#     # 2. Check karein ki files exist karti hain
#     if not os.path.exists(model_path) or not os.path.exists(scaler_path):
#         return "Error: Model or Scaler file not found at the specified path."

#     # 3. Load Model and Scaler
#     # model = joblib.load(model_path)
#     # scaler = joblib.load(scaler_path)

#     model = joblib.load(model_path)
#     scaler = joblib.load(scaler_path)

#     print("Scaler trained on features:")
#     print(scaler.feature_names_in_)

#     features = [
#     'invoice_quantity', 
#     'invoice_dollars', 
#     'Freight', 
#     'total_item_quantity', 
#     'total_item_dollars'
# ]

#     # 5. Data ko Scale karein (Training ki tarah)
#     # Ensure input_df has all these columns
#     input_scaled = scaler.transform(input_df[features])

#     # 6. Prediction karein
#     prediction = model.predict(input_scaled)
    
#     # 7. Result return karein
#     input_df['Predicted_Flag'] = prediction
#     return input_df


import pandas as pd
import joblib
import os

def predict_invoice_flag(input_df):

    # Project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Model paths
    model_path = os.path.join(BASE_DIR, "models", "predict_flag_invoice.pkl")
    scaler_path = os.path.join(BASE_DIR, "models", "scaler.pkl")

    # Check files exist
    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        return "Error: Model or Scaler file not found at the specified path."

    # Load model and scaler
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    features = [
        'invoice_quantity', 
        'invoice_dollars', 
        'Freight', 
        'total_item_quantity', 
        'total_item_dollars'
    ]

    # Scale input
    input_scaled = scaler.transform(input_df[features])

    # Prediction
    prediction = model.predict(input_scaled)

    # Return result
    input_df['Predicted_Flag'] = prediction
    return input_df


