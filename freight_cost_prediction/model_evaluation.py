
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def train_linear_regression(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def train_decision_tree(X_train, y_train, max_depth=5):
    model = DecisionTreeRegressor(max_depth=max_depth, random_state=42)
    model.fit(X_train, y_train)
    return model

def train_random_forest(X_train, y_train, max_depth=6):
    model = RandomForestRegressor(max_depth=max_depth, random_state=42)
    model.fit(X_train, y_train)
    return model

# def evaluate_model(model, X_test, y_test, model_name: str) -> dict:
#     """
#     Evaluate regression model and return metrics.
#     """
#     preds = model.predict(X_test)
    
#     mae = mean_absolute_error(y_test, preds)
#     rmse = mean_squared_error(y_test, preds, squared=False)
#     r2 = r2_score(y_test, preds) * 100
    
#     print(f"{model_name}:")
#     print(f"  MAE:   {mae:.2f}")
#     print(f"  RMSE:  {rmse:.2f}")
#     print(f"  R²:    {r2:.2f}%")
#     print("-" * 40)
    
#     return {
#         "model_name": model_name,
#         "mae": mae,
#         "rmse": rmse,
#         "r2": r2
#     }

from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import pandas as pd

# def evaluate_model(model, X_test_scaled, y_test, model_name: str) -> dict:
#     """
#     Evaluate classification model and return metrics.
#     """
#     # Predictions nikalna
#     preds = model.predict(X_test)
    
#     # Metrics calculate karna
#     accuracy = accuracy_score(y_test, preds)
#     report = classification_report(y_test, preds)
    
#     # Tutorial jaisa detailed output print karna
#     print(f"{model_name} Performance:")
#     print(f"Accuracy : {accuracy:.2f}")
#     print("-" * 30)
#     print("Classification Report:")
#     print(report)
#     print("-" * 40)
    
#     return {
#         "model_name": model_name,
#         "accuracy": accuracy,
#         "report": report
#     }
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def evaluate_model(model, X_test, y_test, model_name: str) -> dict:
    """
    Evaluate regression model (Freight Cost) and return metrics.
    """
    # 1. Predictions nikalna
    preds = model.predict(X_test)
    
    # 2. Regression Metrics calculate karna
    mae = mean_absolute_error(y_test, preds)
    rmse = mean_squared_error(y_test, preds, squared=False)
    r2 = r2_score(y_test, preds) * 100
    
    # 3. Output print karna
    print(f"{model_name} Performance:")
    print(f"  Mean Absolute Error (MAE): {mae:.2f}")
    print(f"  Root Mean Squared Error (RMSE): {rmse:.2f}")
    print(f"  R² Score: {r2:.2f}%")
    print("-" * 40)
    
    return {
        "model_name": model_name,
        "mae": mae,
        "rmse": rmse,
        "r2": r2
    }
    


























