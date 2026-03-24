# import streamlit as st
# import pandas as pd
# import numpy as np
# from inference.predict_freight import predict_freight_cost
# from inference.predict_invoice_flag import predict_invoice_flag

# #---------------------------------------------------------------
# # Page Configuration
# #--------------------------------------------------------------

# st.set_page_config(
# page_title="Vendor Invoice Intelligence Portal", page_icon="",
# layout="wide"
# )

# #----------------------------------------------------------
# # Header Section
# #---------------------------------------------------------

# st.markdown("""
# # Vendor Invoice Intelligence Portal
# ### AI-Driven Freight Cost Prediction & Invoice Risk Flagging

# This internal analytics portal leverages machine learning
# - **Forecast freight costs accurately**
# - **Detect risky or abnormal vendor invoices**
# - **Reduce financial leakage and manual workload**
# """)

# st.divider()
# #------------------------------------------------------------------
# # Sidebar
# #-------------------------------------------------------------------
# st.sidebar.title(" Model Selection")
# selected_model = st.sidebar.radio(
#     "Choose Prediction Module",
#     [
#         "Freight Cost Prediction",
#          "Invoice Manual Approval Flag"
#     ]

# )

# st.sidebar.markdown("""
# ---
# *Business Impact**
# - Improved cost forecasting
# - Reduced invoice fraud & anomalies
# - Faster finance operations
# """)

# #-----------------------------------------------------
# # Freignt cost Prediction
# #---------------------------------------------

# if selected_model == "Freight Cost Prediction":
#     st.subheader(" Freight Cost Prediction")
    
#     st.markdown("""
#     **0bjective:**
#     Predict freight cost for a vendor invoice using **Quantity** and **Invoice Dollars* to support budgeting,
#     forecasting, and vendor negotiations.""")
    
#     with st.form("freight_form"):
#         col1, col2 = st.columns(2)
        
#         with col1:
#             quantity = st.number_input(
#                 " Quantity",
#                 min_value=1,
#                 value=1200

#             )   
#         with col2:
#             dollars = st.number_input(
#                 " Invoice Dollars",
#                 min_value=1.0,
#                 value=18500.0

#             )  

#         submit_freight = st.form_submit_button(" Predict Freight Cost")
        
#     if submit_freight:
#         input_data = {
#             "Quantity": [quantity],
#             "Dollars": [dollars]
#         }
        
#         prediction = predict_freight_cost(input_data) ['Predicted_Freight']
#         st.success ("Prediction completed successfully.")
#         st.metric(
#             label=" Estimated Freight Cost",
#             value=f"${prediction[0]:,.2f}"
#         )
# #---------------------------------------------------------------------
# # Invoice Flag Prediction
# #---------------------------------------------------------------------

# else:
#     st.subheader(" Invoice Manual Approval Prediction")
#     st.markdown("""
#     **0bjective:**
#     Predict whether a vendor invoice should be **flagged for manual approval*
#     based on abnormal cost, freight, or delivery patterns.
#     """)

#     with st.form("invoice flag form"):
#         col1, col2, col3 = st.columns(3)
        
#         with col1:
#             invoice_quantity = st.number_input(
#                 "Invoice Quantity",
#                 min_value=1,
#                 value=50
#             )
#             freight = st.number_input(
#                 "Freight Cost",
#                 min_value=0.0,
#                 value=1.73
#             )


#         with col2:
#             invoice_dollars = st.number_input(
#                 "Invoice dollars",
#                 min_value=1.0,
#                 value=352.95
#             )
#             total_item_quantity= st.number_input(
#                 "Total Item Quantity",
#                 min_value=1
#                 value=162
#             )
        

#         with col3:
#             total_item_dollars= st.number_input(
#                 "Total Item Dollars",
#                 min_value=1.0,
#                 value=2476.0
#             )

#         submit_flag=st.form_submit_button("Evaluate Invoice Risk")

#     if submit_flag:
#         input_data = {
#             "invoice_quantity": [invoice_quantity],
#             "invoice_dollars": [invoice_dollars],
#             "Freight": [freight],
#             "total_item_quantity": [total_item_quantity],
#             "total_item_dollars": [total_item_dollars]
# }
#         flag_prediction = predict_invoice_flag(input_data) ['Predicted_Flag']
#         is_flagged = bool(flag_prediction [0])
        
#         if is_flagged:
#             st.error(" Invoice requires **MANUAL APPROVAL**")
#         else:
#             st.suķcess(" Invoice is **SAFE for Auto-Approval**")








# import streamlit as st
# import pandas as pd
# from inference.predict_freight import predict_freight_cost
# from inference.predict_invoice_flag import predict_invoice_flag

# st.set_page_config(
#     page_title="Vendor Invoice Intelligence Portal",
#     page_icon="📦",
#     layout="wide")


# st.markdown("""
# # 📦Vendor Invoice Intelligence Portal
# ### AI-Driven Freight Cost Prediction & Invoice Risk Flagging

# This internal analytics portal leverages machine learning
# - **Forecast freight costs accurately**
# - **Detect risky or abnormal vendor invoices**
# - **Reduce financial leakage and manual workload**
# """)

# st.divider()

# selected_model = st.sidebar.radio(
#     "Choose Prediction Module",
#     ["Freight Cost Prediction", "Invoice Manual Approval Flag"]
# )

# st.sidebar.markdown("""
# ---
# *Business Impact**
# - Improved cost forecasting
# - Reduced invoice fraud & anomalies
# - Faster finance operations
# """)

# # --- Freight Cost Prediction Module ---
# if selected_model == "Freight Cost Prediction":
#     st.subheader("Freight Cost Prediction")
#     with st.form("freight_form"):
#         col1, col2 = st.columns(2)
#         with col1:
#             quantity = st.number_input("Quantity", min_value=1, value=1200)
#         with col2:
#             dollars = st.number_input("Invoice Dollars", min_value=1.0, value=18500.0)
#         submit_freight = st.form_submit_button("Predict Freight Cost")

#     if submit_freight:
#         # Convert to DataFrame before sending to inference
#         input_data = pd.DataFrame({"Quantity": [quantity], "Dollars": [dollars]})
#         res_df = predict_freight_cost(input_data)
#         prediction = res_df['Predicted_Freight'].iloc[0]
#         st.success(f"Estimated Freight Cost: ${prediction:,.2f}")

# # --- Invoice Flag Prediction Module ---
# else:
#     st.subheader("Invoice Manual Approval Prediction")
#     with st.form("invoice_flag_form"):
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             inv_qty = st.number_input("Invoice Quantity", min_value=1, value=50)
#             freight = st.number_input("Freight Cost", min_value=0.0, value=1.73)
#         with col2:
#             inv_dlrs = st.number_input("Invoice Dollars", min_value=1.0, value=352.95)
#             item_qty = st.number_input("Total Item Quantity", min_value=1, value=162)
#         with col3:
#             item_dlrs = st.number_input("Total Item Dollars", min_value=1.0, value=2476.0)
        
#         submit_flag = st.form_submit_button("Evaluate Invoice Risk")

#     if submit_flag:
#         # Dictionary ko DataFrame mein convert kiya taaki Scaler transform kar sake
#         input_data = pd.DataFrame({
#         "invoice_quantity": [inv_qty], 
#         "invoice_dollars": [inv_dlrs],
#         "Freight": [freight], 
#         "total_item_quantity": [item_qty],
#         "total_item_dollars": [item_dlrs]
#      })
        
#         # Inference call
#         res_flag_df = predict_invoice_flag(input_data)
        
#         # Result display
#         is_flagged = bool(res_flag_df['Predicted_Flag'].iloc[0])
        
#         if is_flagged:
#             st.error("⚠️ Invoice requires MANUAL APPROVAL")
#         else:
#             st.success("✅ Invoice is SAFE for Auto-Approval")
        
#         # Optional: Full output dikhane ke liye
#         st.write("Detailed Features:", res_flag_df)



import streamlit as st
import pandas as pd
from inference.predict_freight import predict_freight_cost
from inference.predict_invoice_flag import predict_invoice_flag

st.set_page_config(
    page_title="Vendor Invoice Intelligence Portal",
    page_icon="📦",
    layout="wide"
)
st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(120deg, #0f2027, #203a43, #2c5364);
}

/* Header animation */
.header-box {
    animation: fadeIn 2s ease-in;
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(-20px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Card style */
.card {
    background-color: #1C1F26;
    padding: 20px;
    border-radius: 12px;
    transition: 0.3s;
    border: 1px solid #2c5364;
}

.card:hover {
    transform: scale(1.03);
    box-shadow: 0px 4px 20px rgba(0,0,0,0.5);
}

/* Button glow */
.stButton>button {
    background-color: #00C2A8;
    color: white;
    border-radius: 8px;
    height: 45px;
    width: 100%;
    font-size: 16px;
    border: none;
}

.stButton>button:hover {
    box-shadow: 0px 0px 15px #00C2A8;
    transition: 0.3s;
}

/* Input boxes */
.stNumberInput input {
    background-color: #0E1117;
    color: white;
    border-radius: 8px;
}

</style>
""", unsafe_allow_html=True)



# ---------- HEADER ----------
st.caption("Machine Learning Powered Finance Analytics Dashboard")
st.markdown("""
<div class="header-box" style="
background: linear-gradient(90deg, #141E30, #243B55);
padding: 30px;
border-radius: 15px;
box-shadow: 0px 4px 20px rgba(0,0,0,0.4);">

<h1 style="color:#00E5FF; font-size:44px;">
📦 Vendor Invoice Intelligence Portal
</h1>

<p style="color:#CFD8DC; font-size:20px;">
AI-Driven Freight Cost Prediction & Invoice Risk Flagging
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""
This internal analytics portal leverages machine learning to:
- **Forecast freight costs accurately**
- **Detect risky or abnormal vendor invoices**
- **Reduce financial leakage and manual workload**
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card"><h3>Invoices Processed</h3><h2>12,540</h2></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><h3>Flagged Invoices</h3><h2>342</h2></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card"><h3>Avg Freight Cost</h3><h2>$182</h2></div>', unsafe_allow_html=True)


st.divider()

# ---------- SIDEBAR ----------

st.sidebar.markdown("""
<h2 style='color:#00E5FF;'>📊 Dashboard Menu</h2>
""", unsafe_allow_html=True)



selected_model = st.sidebar.radio(
    "Selected Model",
    ["🚚 Freight Cost Prediction", "📋 Invoice Manual Approval Flag"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")

st.sidebar.markdown("""
### 📈 Business Impact
- Improved cost forecasting
- Reduced invoice fraud & anomalies
- Faster finance operations
""")

st.sidebar.markdown("---")

st.sidebar.markdown("""
### 🧠 ML Models Used
- Freight Cost Prediction (Regression)
- Invoice Risk Detection (Classification)
""")

st.sidebar.markdown("---")

st.sidebar.markdown("""
<center>
<p style='color:lightgray; font-size:13px;'>
Vendor Invoice Intelligence System<br>
Built with Machine Learning & Streamlit
</p>
</center>
""", unsafe_allow_html=True)

# ---------- FREIGHT PREDICTION ----------
if selected_model == "🚚 Freight Cost Prediction":
    st.markdown("""
<h1 style='font-size:40px; color:#00C853;'>
🚚 Freight Cost Prediction
</h1>
""", unsafe_allow_html=True)
    with st.form("freight_form"):
        col1, col2 = st.columns(2)
        with col1:
            quantity = st.number_input("Quantity", min_value=1, value=1200)
        with col2:
            dollars = st.number_input("Invoice Dollars", min_value=1.0, value=18500.0)

        submit_freight = st.form_submit_button("Predict Freight Cost")

    if submit_freight:
        input_data = pd.DataFrame({"Quantity": [quantity], "Dollars": [dollars]})
        res_df = predict_freight_cost(input_data)
        prediction = res_df['Predicted_Freight'].iloc[0]

        st.markdown(
            f'<p class="result-safe">Estimated Freight Cost: ${prediction:,.2f}</p>',
            unsafe_allow_html=True
        )

# ---------- INVOICE FLAG ----------
# ---------- INVOICE FLAG ----------
else:
    st.markdown("""
<h2 style='font-size:32px; color:#00E5FF; margin-top:10px;'>
📊 Invoice Manual Approval Prediction
</h2>
""", unsafe_allow_html=True)

    with st.form("invoice_flag_form"):
        col1, col2, col3 = st.columns(3)

        with col1:
            inv_qty = st.number_input("Invoice Quantity", min_value=1, value=50)
            freight = st.number_input("Freight Cost", min_value=0.0, value=1.73)

        with col2:
            inv_dlrs = st.number_input("Invoice Dollars", min_value=1.0, value=352.95)
            item_qty = st.number_input("Total Item Quantity", min_value=1, value=162)

        with col3:
            item_dlrs = st.number_input("Total Item Dollars", min_value=1.0, value=2476.0)

        submit_flag = st.form_submit_button("Evaluate Invoice Risk")

    if submit_flag:
        input_data = pd.DataFrame({
            "invoice_quantity": [inv_qty],
            "invoice_dollars": [inv_dlrs],
            "Freight": [freight],
            "total_item_quantity": [item_qty],
            "total_item_dollars": [item_dlrs]
        })

        res_flag_df = predict_invoice_flag(input_data)

        is_flagged = False

        if isinstance(res_flag_df, str):
            st.error(res_flag_df)
        else:
            is_flagged = bool(res_flag_df['Predicted_Flag'].iloc[0])

            if is_flagged:
                st.error("⚠️ High Risk Invoice")
            else:
                st.success("✅ Vendor is Normal-Approved for Auto Processing")

            if is_flagged:
                st.markdown(
                    '<p class="result-risk">⚠️ Invoice requires MANUAL APPROVAL</p>',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    '<p class="result-safe">✅ Invoice is SAFE for Auto-Approval</p>',
                    unsafe_allow_html=True
                )

            st.write("Detailed Features:", res_flag_df)





















