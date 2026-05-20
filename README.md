# Bank Customer Churn — End-to-End ML Pipeline

A production-structured machine learning pipeline that predicts whether a bank customer will churn. The project demonstrates solid software engineering practices including modular ETL, multi-model training, serialised state management, and an interactive Streamlit dashboard for real-time inference.

---

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Overview

Customer attrition (churn) is one of the most critical metrics for any service-oriented business. Acquiring a new customer is often significantly more expensive than retaining an existing one, making early identification of at-risk customers a high-value objective.

This project implements an industry-standard ML solution to identify bank customers at high risk of churning. By leveraging demographic and financial data — including credit score, age, account balance, and tenure — the system outputs a probability score that retention teams can use to trigger targeted interventions before a customer exits.

**Key capabilities:**

- **Automated Data Pipeline (ETL):** Robust cleaning and one-hot encoding with native handling of the dummy variable trap.
- **Multi-Model Architecture:** Support for Random Forest and XGBoost, selectable at both training and inference time.
- **State Persistence:** Model artefacts and feature lists are serialised together via `joblib`, preventing feature-mismatch errors during inference.
- **Real-Time Inference UI:** A Streamlit dashboard allowing non-technical stakeholders to input customer parameters and receive an instant churn probability.

---

## Project Structure

```
bank-customer-churn-pipeline/
├── data/
│   ├── raw/                  # Original, immutable source data (e.g., Kaggle CSV)
│   └── processed/            # Cleaned data ready for model consumption
├── models/                   # Serialised .joblib model and feature configuration files
├── app.py                    # Streamlit dashboard application
├── etl.py                    # Extract, Transform, Load pipeline
├── train_model.py            # Model training and evaluation
├── requirements.txt          # Pinned project dependencies
└── README.md
```

---

## Dataset
The project uses the **Bank Customer Churn** dataset (available on Kaggle). Place `Customer-Churn-Records.csv` in `data/raw/` before running the pipeline.

| Feature | Description |
|---|---|
| `CreditScore`      | Customer credit score (300–900) |
| `Geography`        | Country of residence (France, Spain, Germany) |
| `Gender`           | Customer gender |
| `Age`              | Customer age |
| `Tenure`           | Years as a bank customer |
| `Balance`          | Account balance |
| `NumOfProducts`    | Number of bank products held |
| `HasCrCard`        | Credit card holder flag (0/1) |
| `IsActiveMember`   | Active member flag (0/1) |
| `EstimatedSalary`  | Estimated annual salary |
| `Card Type`        | Card tier (Diamond, Gold, Platinum, Silver) |
| `Exited`           | **Target** — churned (1) or retained (0) |

---

## Tech Stack

| Component             | Technology |
| Language              | Python 3.9+ |
| Data Engineering      | Pandas |
| Machine Learning      | Scikit-Learn, XGBoost |
| Model Serialisation   | joblib |
| Dashboard             | Streamlit |

---

## Installation
**Prerequisites:** Python 3.9 or higher.

1. Clone the repository:
   ```bash
   git clone https://github.com/garethmubaiwa/bank-customer-churn-prediction.git
   cd bank-customer-churn-prediction
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate        # macOS/Linux
   venv\Scripts\activate           # Windows
   ```

3. Install all dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download the dataset from Kaggle and place it at `data/raw/Customer-Churn-Records.csv`.

---

## Usage
peline must be executed in order: ETL first, then model training, then the dashboard.

### Step 1 — Data Processing (ETL)
Loads the raw CSV, drops identifier columns (`RowNumber`, `CustomerId`, `Surname`), and applies one-hot encoding to categorical features (`Geography`, `Gender`, `Card Type`). The cleaned dataset is saved to `data/processed/`.

```bash
python etl.py
```
Output: `data/processed/cleaned_churn_data.csv`

### Step 2 — Model Training
Trains the selected classifier, prints a full classification report, and serialises the model and its feature list to `models/`. Switch between architectures by editing the final line of `train_model.py`.

```bash
python train_model.py
```
Output: `models/churn_{model_type}_model.joblib` and `models/churn_{model_type}_model_features.joblib`
Both models can be trained independently and will coexist in the `models/` directory.

### Step 3 — Interactive Dashboard

```bash
streamlit run app.py
```
Opens a local server at `http://localhost:8501`. Select a trained model from the sidebar, enter customer parameters, and receive an instant churn probability.

---

## Model Performance

Models are evaluated primarily on **F1-Score** and **Recall** for the positive class (Churn = 1), as failing to identify a churner (false negative) carries significantly higher business cost than a false alarm.

| Model           | Accuracy  | Precision (Churn)  | Recall (Churn)  | F1-Score (Churn)   |
| XGBoost         | 84.40%    | 0.60               | 0.64            | 0.62               |
| Random Forest   | 86.45%    | 0.77               | 0.44            | 0.56               |

> Metrics are evaluated on a held-out test set (20% of data, `random_state=42`). Results may vary slightly with different seeds.

---

## Future Improvements

- **Hyperparameter Tuning:** Implement `GridSearchCV` or Optuna to optimise XGBoost parameters (learning rate, max depth, subsampling ratio).
- **Class Imbalance Handling:** Integrate SMOTE (Synthetic Minority Over-sampling Technique) or use XGBoost's `scale_pos_weight` parameter to improve Recall on the minority churn class.
- **Feature Engineering:** Derive features such as `Balance_to_Salary_Ratio` or discretise `Age` into meaningful cohort bins to expose non-linear relationships.
- **Model Explainability:** Integrate SHAP (SHapley Additive exPlanations) visualisations into the Streamlit dashboard to surface the key drivers behind individual predictions.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.