from data_preprocessing import load_invoice_data,split_data,scale_features,apply_labels
from modeling_evaluation import train_random_forest,evaluate_classifier
import joblib

FEATURES=[
    "invoice_quantity",
    "invoice_dollars",
    "Freight",
    "total_item_dollars"
]
TARGET="flag_invoice"

def main():
    df=load_invoice_data()
    df=apply_labels(df)

    X_train, X_test, y_train, y_test =split_data(df,FEATURES ,TARGET)
    X_train_scaled,X_test_scaled=scale_features(
        X_train,X_test,'models/scaler.pkl'
    )

    
    grid_search=train_random_forest(X_train_scaled,y_train)
    evaluate_classifier(

        grid_search.best_estimator_,
        X_train_scaled,
        y_test,
        "Random Forest Classifier"
    )
    joblib.dump(grid_search.best_estimator_,'models/predict_flag_invoice.pkl')

if __name__ == "__main__":
    main()

# import joblib
# from pathlib import Path
# # Apne folder ke hisaab se import check karlein
# from data_preprocessing import load_invoice_data, apply_labels, split_data, scale_features
# from modeling_evaluation import train_random_forest, evaluate_classifier

# def main():
#     # 1. Folder Setup
#     model_dir = Path("models")
#     model_dir.mkdir(exist_ok=True)

#     # 2. Data Load aur Prepare karein
#     df = load_invoice_data()
#     df = apply_labels(df)

#     # Features aur Target define karein
#     FEATURES = ['invoice_quantity', 'invoice_dollars', 'Freight', 
#                 'days_po_to_invoice', 'days_to_pay', 'total_brands', 
#                 'total_item_quantity', 'total_item_dollars', 'avg_receiving_delay']
#     TARGET = 'flag_invoice'

#     # 3. Split aur Scale
#     # Yaad rahe pichhli baar yahan y = df[target] sahi kiya tha humne
#     X_train, X_test, y_train, y_test = split_data(df, FEATURES, TARGET)
#     X_train_scaled, X_test_scaled = scale_features(X_train, X_test, "models/scaler.pkl")

#     # 4. Train Model (Grid Search wala)
#     print("Starting Grid Search training... Please wait.")
#     # Yahan variable ka naam 'grid_result' rakha hai
#     grid_result = train_random_forest(X_train_scaled, y_train)

#     # 5. Evaluate (Best Estimator use karein)
#     best_model = grid_result.best_estimator_
#     evaluate_classifier(best_model, X_test_scaled, y_test, "Random Forest (Optimized)")

#     # 6. Save (Yahan NameError nahi aayegi ab)
#     model_path = model_dir / "predict_flag_invoice.pkl"
#     joblib.dump(best_model, model_path)
    
#     print(f"\nBest Parameters Found: {grid_result.best_params_}")
#     print(f"Model saved successfully at: {model_path}")

# if __name__ == "__main__":
#     main()