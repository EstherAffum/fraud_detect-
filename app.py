import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

model = joblib.load("C:/Users/Hi/Desktop/DESKTOP/BOOT CAMPS/Because She Can/Final Project/fraud_detection_pipeline.pkl")

if "fraud_alerts" not in st.session_state:
    st.session_state.fraud_alerts = []

st.title("Fraud Detection Prediction App")
st.markdown("Please enter the transaction details and use the predict button")
st.divider()

col_form, col_alerts = st.columns([2, 1])

with col_form:
    transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
    amount = st.number_input("Amount", min_value=0.0, value=1000.0)

    oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)
    newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
    oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
    newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

    if st.button("Predict"):
        input_data = pd.DataFrame([{
            "type": transaction_type,
            "amount": amount,
            "oldbalanceOrg": oldbalanceOrg,
            "newbalanceOrig": newbalanceOrig,
            "oldbalanceDest": oldbalanceDest,
            "newbalanceDest": newbalanceDest
        }])

        prediction = model.predict(input_data)[0]

        st.subheader(f"Prediction: '{int(prediction)}'")

        if prediction == 1:
            st.error("This transaction can be fraud")
            st.toast("Fraudulent transaction detected!", icon="🚨")
            st.session_state.fraud_alerts.insert(0, {
                "Time": datetime.now().strftime("%H:%M:%S"),
                "Type": transaction_type,
                "Amount": amount,
                "Sender Old Bal": oldbalanceOrg,
                "Sender New Bal": newbalanceOrig,
            })
        else:
            st.success("This transaction looks legit")

with col_alerts:
    st.subheader("🚨 Fraud Alerts")
    alert_count = len(st.session_state.fraud_alerts)
    st.metric("Flagged this session", alert_count)

    if alert_count == 0:
        st.info("No fraudulent transactions detected yet.")
    else:
        for alert in st.session_state.fraud_alerts:
            st.warning(
                f"**{alert['Time']}** — {alert['Type']} of "
                f"${alert['Amount']:,.2f} flagged as fraud"
            )
        if st.button("Clear alerts"):
            st.session_state.fraud_alerts = []
            st.rerun()
