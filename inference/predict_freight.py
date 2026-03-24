# import joblib
# import pandas as pd

# MODEL_PATH="models/predict_freight_model.pkl"
# def load_model(model_path: str=MODEL_PATH):
#     """
#     LOAD trained freight cost prediction model
#     """
#     with open(model_path,"rb") as f:
#         model=joblib.load(f)

#     return model

# def predict_freight_cost(input_data):
#     """
#     predict freight cost for new vendor invoices.

#     Parameter
#     -------------
#     input_data:dict

#     Returns 
#     --------------
#     pd.Dataframe with predicted freight cost
#     """

#     model=load_model()
#     input_df=pd.DataFrame(input_data)
    
#     required_columns = ["Dollars"] # Agar model sirf ispe train hua hai
#     input_df = input_df[required_columns]

#     input_df['Predicted_Freight']=model.predict(input_df).round()
#     return input_df

# if __name__ == "__main__":

#     sample_data={
#         "Dollars":[18500,9000,3000,200]
#     }
#     prediction=predict_freight_cost(sample_data)
#     print(prediction)



import joblib
import pandas as pd
import os

# Base directory (project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Model path
MODEL_PATH = os.path.join(BASE_DIR, "models", "predict_freight_model.pkl")

def load_model(model_path: str = MODEL_PATH):
    """
    LOAD trained freight cost prediction model
    """
    with open(model_path, "rb") as f:
        model = joblib.load(f)

    return model


def predict_freight_cost(input_data):
    """
    predict freight cost for new vendor invoices.
    """

    model = load_model()
    input_df = pd.DataFrame(input_data)

    required_columns = ["Dollars"]
    input_df = input_df[required_columns]

    input_df['Predicted_Freight'] = model.predict(input_df).round()
    return input_df


if __name__ == "__main__":
    sample_data = {
        "Dollars": [18500, 9000, 3000, 200]
    }
    prediction = predict_freight_cost(sample_data)
    print(prediction)













    
    