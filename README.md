# Fraud Detection System for Financial Transactions

## 📌 Project Overview

This project develops a **machine learning-based fraud detection system** designed to identify potentially fraudulent mobile money transactions. The project combines exploratory data analysis, feature engineering, machine learning, and a **Streamlit web application** to demonstrate how transaction-level fraud detection can be applied in a practical setting.

The project approaches fraud detection as a cybersecurity and financial-risk problem, where the goal is not only to identify fraudulent transactions but also to minimize missed fraud while managing false-positive alerts.

---

## 🚨 Problem Statement

The increasing use of mobile money and digital financial services has created a growing need for effective fraud detection mechanisms. Fraudulent transactions represent a very small proportion of total transactions, making fraud detection a highly **imbalanced classification problem**.

The analysis found that fraud is particularly concentrated around **TRANSFER and CASH_OUT transactions**. The challenge is therefore to build a model that can identify fraudulent transactions with high sensitivity while avoiding an overwhelming number of false alerts.

The key question addressed by this project is:

> **How can machine learning be used to identify potentially fraudulent mobile money transactions early enough to support intervention while reducing unnecessary alerts on legitimate transactions?**

---

## 🎯 Project Objectives

* Identify transaction patterns associated with fraudulent activity.
* Explore the distribution of fraud across transaction types and amounts.
* Identify suspicious account balance behaviours.
* Engineer meaningful features for fraud detection.
* Develop a machine learning classification model for fraud detection.
* Evaluate the model using fraud-focused performance metrics.
* Deploy the trained model through an interactive Streamlit application.
* Recommend improvements for future production deployment.

---

## 📊 Dataset

The project uses the **AIML Dataset.csv**, containing simulated mobile money transaction records.

Key variables used in the analysis include:

| Feature          | Description                                       |
| ---------------- | ------------------------------------------------- |
| `step`           | Time-step indicator                               |
| `type`           | Type of transaction                               |
| `amount`         | Transaction amount                                |
| `oldbalanceOrg`  | Sender's balance before transaction               |
| `newbalanceOrig` | Sender's balance after transaction                |
| `oldbalanceDest` | Recipient's balance before transaction            |
| `newbalanceDest` | Recipient's balance after transaction             |
| `isFraud`        | Target variable indicating fraudulent transaction |
| `isFlaggedFraud` | Existing system fraud flag                        |
| `nameOrig`       | Sender account identifier                         |
| `nameDest`       | Recipient account identifier                      |

The analysis identified a severe imbalance between fraudulent and legitimate transactions, making appropriate model evaluation particularly important.

---

## 🔎 Exploratory Data Analysis

The project explored:

* Transaction type distribution
* Fraud rate by transaction type
* Transaction amount distribution
* Fraudulent vs. legitimate transaction amounts
* High-risk `TRANSFER` and `CASH_OUT` transactions
* Correlations between numerical variables
* Suspicious account balance patterns

### Key Findings

1. **Fraud is concentrated in specific transaction types**, particularly `TRANSFER` and `CASH_OUT`.

2. **Transaction amounts are highly skewed**, with the log-transformed distribution showing two distinct transaction-size groups.

3. **Balance-drain behaviour is a significant suspicious pattern**, particularly when an account with a positive balance is completely depleted following a transfer or cash-out.

4. The dataset has **severe class imbalance**, making recall and precision more informative than accuracy alone. 

---

## 🛠️ Feature Engineering

Two behavioural features were created:

### `balanceDiffOrig`

```text
oldbalanceOrg - newbalanceOrig
```

This represents the amount that leaves the sender's account.

### `balanceDiffDest`

```text
newbalanceDest - oldbalanceDest
```

This represents the amount received by the destination account.

These features provide additional information about **how money moves during a transaction**, rather than relying only on the account balances themselves.

---

## 🤖 Machine Learning Model

The project uses a **Logistic Regression** classifier implemented through a Scikit-learn Pipeline.

### Pipeline

```text
Raw Data
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Train/Test Split
   ↓
Numerical Scaling
   ↓
Categorical Encoding
   ↓
Balanced Logistic Regression
   ↓
Fraud Prediction
```

### Model Configuration

* **Algorithm:** Logistic Regression
* **Class balancing:** `class_weight="balanced"`
* **Maximum iterations:** `1000`
* **Train/Test Split:** 70/30
* **Sampling:** Stratified
* **Numerical preprocessing:** StandardScaler
* **Categorical preprocessing:** OneHotEncoder

The balanced class weighting was used to ensure that the model gives greater importance to the minority fraud class. 

---

## 📈 Model Performance

The model produced the following results on the test dataset:

| Metric    | Not Fraud |    Fraud |
| --------- | --------: | -------: |
| Precision |      1.00 | **0.02** |
| Recall    |      0.93 | **0.99** |
| F1-Score  |      0.97 | **0.03** |

### Confusion Matrix

```text
[[293325, 20905],
 [     5,   338]]
```

### Key Interpretation

The model successfully detected **338 of 343 actual fraudulent transactions**, giving it approximately **99% recall**.

However, it also incorrectly classified **20,905 legitimate transactions as fraudulent**, resulting in only **2% precision** for the fraud class.

Therefore, although the model is highly sensitive to fraud, it generates a large number of false-positive alerts. 

---

## 💡 Solution

The proposed solution is a **machine learning-powered fraud alerting system** rather than a fully automated transaction-blocking system.

The system can:

1. Receive transaction information.
2. Process and transform the input.
3. Apply the trained fraud detection model.
4. Generate a fraud prediction.
5. Provide the result through a **Streamlit interface**.
6. Support analysts in identifying transactions that require further investigation.

The trained model pipeline is saved using `joblib` and can be integrated into a web application for real-time prediction. 

---

## 🌐 Streamlit Application

The model was showcased through a **Streamlit web application**, providing an interactive interface for entering transaction information and obtaining a fraud prediction.

The application demonstrates how the machine learning model can move beyond notebook-based analysis into a practical user-facing fraud detection tool.

### Proposed Workflow

```text
Transaction Details
        ↓
Streamlit Application
        ↓
Preprocessing Pipeline
        ↓
Fraud Detection Model
        ↓
Fraud Prediction
        ↓
Investigation / Review
```

---

## ⚠️ Key Limitation

The major limitation of the current model is its **very low precision**.

With approximately **20,905 false positives**, deploying the model as an automatic transaction blocker could result in many legitimate transactions being incorrectly stopped.

Therefore:

> **The current model is better suited for fraud detection, alerting and analyst triage than automatic transaction blocking.**

---

## 🚀 Recommendations

### 1. Threshold Tuning

The default classification threshold should be adjusted to find a better balance between precision and recall.

### 2. Test Alternative Models

Future versions should evaluate models such as:

* Random Forest
* XGBoost
* Other tree-based ensemble methods
* Anomaly detection techniques

### 3. Cost-Sensitive Evaluation

The evaluation should consider the actual financial cost of:

* Missing a fraudulent transaction
* Incorrectly flagging a legitimate transaction

### 4. Additional Behavioural Features

Future versions could incorporate transaction-frequency and customer-behaviour features to improve fraud detection.

### 5. Human-in-the-Loop Detection

High-risk transactions should be routed to fraud analysts rather than automatically blocked.

### 6. Continuous Monitoring

Fraud patterns can change over time, so model performance should be continuously monitored and periodically retrained.

The original project report also recommends threshold tuning, alternative models, cost-sensitive evaluation and a human-in-the-loop workflow before production deployment. 

---

## 🧰 Tools & Technologies

### Programming & Analysis

* **Python**
* **Jupyter Notebook**
* **Pandas**
* **NumPy**

### Data Visualization

* **Matplotlib**
* **Seaborn**

### Machine Learning

* **Scikit-learn**
* Logistic Regression
* StandardScaler
* OneHotEncoder
* Classification Report
* Confusion Matrix

### Model Deployment

* **Streamlit**
* **Joblib**

### Version Control

* **Git**
* **GitHub**

---

## 📁 Suggested Project Structure

```text
Fraud-Detection-Model/
│
├── data/
│   └── AIML Dataset.csv
│
├── notebooks/
│   └── FraudDetectionModel.ipynb
│
├── app/
│   └── app.py
│
├── model/
│   └── fraud_detection_pipeline.pkl
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

## 📌 Conclusion

This project demonstrates how **data analytics and machine learning can be applied to financial fraud detection**. The model achieved very high fraud recall, successfully identifying almost all fraudulent transactions in the test set. However, its low precision highlights the challenge of false positives in highly imbalanced fraud datasets.

The project therefore recommends using the model as an **early-warning and fraud-triage tool**, supported by business rules and human investigation, while further improving precision before considering automated transaction blocking.


> **An AI-powered Streamlit fraud detection system that identifies high-risk mobile money transactions in real time, helping financial institutions detect fraud earlier and make better-informed intervention decisions.**
