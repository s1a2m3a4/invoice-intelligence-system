# import joblib
# import pandas as pd

# MODEL_PATH="models/predict_flag_invoice.pkl"

# def load_model(model_path: str=MODEL_PATH):
#     """
#     LOAD trained classifier model.
#     """
#     with open(model_path,"rb") as f:
#         model=joblib.load(f)

#     return model

# def predict_invoice_flag(input_data):
#     """
#     predict freight cost for new vendor invoices.

#     Parameter
#     -------------
#     input_data:dict

#     Returns 
#     --------------
#     pd.Dataframe with predicted flag
#     """

#     model=load_model()
#     input_df=pd.DataFrame(input_data)

#     features_used_in_training = [
#         'invoice_quantity', 'invoice_dollars', 'Freight', 
#         'days_po_to_invoice', 'days_to_pay', 'total_brands', 
#         'total_item_quantity', 'total_item_dollars', 'avg_receiving_delay'
#     ]

#     for col in features_used_in_training:
#         if col not in input_df.columns:
#             input_df[col] = 0  # Missing columns ko 0 se fill karein
            
#     # Columns ka order wahi rakhein jo training mein tha
#     input_df = input_df[features_used_in_training]

#     input_df['Predicted_Flag']=model.predict(input_df).round()
#     return input_df

# if __name__ == "__main__":

#     sample_data={
#         "Dollars":[19500,4000,1000,600]
#     }
#     prediction=predict_invoice_flag(sample_data)
#     print(prediction)

# import joblib
# import pandas as pd
# import os

# # Path ko sahi se handle karne ke liye
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# MODEL_PATH = os.path.join(BASE_DIR, "models", "predict_flag_invoice.pkl")

# def load_model(model_path: str = MODEL_PATH):
#     """
#     LOAD trained classifier model.
#     """
#     if not os.path.exists(model_path):
#         raise FileNotFoundError(f"Model file nahi mili: {model_path}")
    
#     with open(model_path, "rb") as f:
#         model = joblib.load(f)
#     return model

# def predict_invoice_flag(input_data):
#     """
#     Predict risk flag for invoices.
#     """
#     model = load_model()
#     input_df = pd.DataFrame(input_data)

#     # TRAINING ke waqt use huye exact 9 features
#     features_used_in_training = [
#         'invoice_quantity', 'invoice_dollars', 'Freight', 
#         'days_po_to_invoice', 'days_to_pay', 'total_brands', 
#         'total_item_quantity', 'total_item_dollars', 'avg_receiving_delay'
#     ]

#     # 1. Missing columns ko handle karein
#     for col in features_used_in_training:
#         if col not in input_df.columns:
#             input_df[col] = 0  # Default value 0

#     # 2. Columns ka ORDER wahi rakhein jo training mein tha (V. Important)
#     input_df = input_df[features_used_in_training]

#     # 3. Prediction (Classifier ke liye round() ki zaroorat nahi hoti)
#     input_df['Predicted_Flag'] = model.predict(input_df)
    
#     return input_df

# if __name__ == "__main__":
#     # SAMPLE DATA ko features ke hisaab se update kiya
#     sample_data = {
#         "invoice_quantity": [50, 100],
#         "invoice_dollars": [1500, 4000],
#         "Freight": [10, 50],
#         "total_item_quantity": [45, 110],
#         "total_item_dollars": [1450, 4200]
#         # Baki 4 columns automatically 0 ho jayenge logic se
#     }
    
#     try:
#         prediction = predict_invoice_flag(sample_data)
#         print("--- Prediction Result ---")
#         print(prediction)
#     except Exception as e:
#         print(f"Error: {e}")




# import joblib
# import pandas as pd
# import os

# def predict_invoice_flag(input_data):
#     # Sahi model load karein
#     model_path = "models/predict_flag_invoice.pkl"
#     model = joblib.load(model_path)
    
#     input_df = pd.DataFrame(input_data)
    
#     # Ye wahi 9 features hain jo aapne training mein use kiye the
#     features = [
#         'invoice_quantity', 'invoice_dollars', 'Freight', 
#         'days_po_to_invoice', 'days_to_pay', 'total_brands', 
#         'total_item_quantity', 'total_item_dollars', 'avg_receiving_delay'
#     ]
    
#     # Missing columns ko 0 se bharo
#     for col in features:
#         if col not in input_df.columns:
#             input_df[col] = 0
            
#     # Sirf wahi columns bhejo jo model ko chahiye
#     input_df = input_df[features]
    
#     input_df['Predicted_Flag'] = model.predict(input_df)
#     return input_df


import pandas as pd
import joblib
import os

def predict_invoice_flag(input_df):
    # 1. Model aur Scaler ke sahi paths (Absolute paths use karein)
    model_path = r'C:\Users\samay\Downloads\invoice_intelligence_system\models\predict_flag_invoice.pkl'
    scaler_path = r'C:\Users\samay\Downloads\invoice_intelligence_system\models\scaler.pkl'

    # 2. Check karein ki files exist karti hain
    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        return "Error: Model or Scaler file not found at the specified path."

    # 3. Load Model and Scaler
    # model = joblib.load(model_path)
    # scaler = joblib.load(scaler_path)

    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    print("Scaler trained on features:")
    print(scaler.feature_names_in_)

    features = [
    'invoice_quantity', 
    'invoice_dollars', 
    'Freight', 
    'total_item_quantity', 
    'total_item_dollars'
]

    # 4. Features ki list jo model training ke waqt use hui thi (Exactly 9 features)
#     features = [
#     'invoice_quantity', 
#     'invoice_dollars', 
#     'Freight', 
#     'total_item_quantity', 
#     'total_item_dollars', 
#     'days_po_to_invoice',  # In charo ko dhyan se dekho
#     'days_to_pay', 
#     'total_brands', 
#     'avg_receiving_delay'
# ]

    # 5. Data ko Scale karein (Training ki tarah)
    # Ensure input_df has all these columns
    input_scaled = scaler.transform(input_df[features])

    # 6. Prediction karein
    prediction = model.predict(input_scaled)
    
    # 7. Result return karein
    input_df['Predicted_Flag'] = prediction
    return input_df





