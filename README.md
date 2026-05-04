# ❤️ Heart Disease Prediction Using Machine Learning

 **Live App:** https://heart-disease-prediction-using-machine-learning-app.streamlit.app/
 **GitHub Repo:** https://github.com/Aswini-Dileep/Heart-Disease-Prediction-App

---

## Project Overview

This project is an **end-to-end machine learning application** that predicts the likelihood of heart disease based on patient clinical data.

The system is designed not only to generate predictions but also to provide:

* Risk interpretation
* Clinical recommendations
* A user-friendly interface for healthcare scenarios

The application is built using **Streamlit** and deployed on the cloud for real-time usage.

---

## Objective

The main objective of this project is to:

* Build a machine learning model to predict heart disease risk
* Develop a user-friendly web application
* Provide meaningful interpretation of predictions
* Simulate a **clinical decision support system**

---

## Real-World Use Case

This system can be used in:

* Hospital OPD (Outpatient Department)
* Telemedicine platforms
* Health screening camps

### Example Scenario:

A nurse inputs patient details → The system predicts risk → High-risk patients are prioritized for doctor consultation

---

## Dataset Description

The dataset contains **630,000 records** with 15 features including:

* Age
* Sex
* Chest Pain Type
* Blood Pressure
* Cholesterol
* FBS over 120
* EKG results
* Max Heart Rate
* ST Depression
* Exercise angina
* Slope of ST
* Number of vessels fluro	
* Thallium Test
* Heart Disease (Target)

The dataset is structured and contains both categorical and numerical features.

---

## Project Workflow

### 1. Data Understanding

* Explored dataset structure, data types, and feature meanings
* Identified categorical and numerical variables

---

### 2. Exploratory Data Analysis (EDA)

Performed:

* Statistical summary analysis
* Distribution plots (Age, BP, Cholesterol)
* Count plots (Sex, Chest Pain Type)
* Correlation heatmap
* Age distribution plot
* Cholesterol distribution plot
* Correlation heatmap

---

### 3. Data Preprocessing

* Encoded categorical variables
* Verified no missing values
* Handled feature scaling where required

---

### 4. Feature Importance Analysis

Used tree-based models to identify key features:

Top contributing features:

* Thallium
* Chest Pain Type
* Max Heart Rate
* ST Depression
* Feature importance chart

---

### 5. Model Building

Trained multiple models:

* Logistic Regression
* Random Forest
* XGBoost
* Decision Tree

---

### 6. Model Evaluation

Evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score

### Results:

| Model               | Accuracy  | Precision | Recall    | F1 Score  |
| ------------------- | --------- | --------- | --------- | --------- |
| Logistic Regression | ~0.88     | ~0.87     | ~0.85     | ~0.86     |
| Random Forest       | ~0.88     | ~0.87     | ~0.86     | ~0.86     |
| **XGBoost**         | **~0.89** | **~0.88** | **~0.86** | **~0.87** |
| Decision Tree       | ~0.82     | ~0.80     | ~0.80     | ~0.80     |

 **XGBoost was selected as the final model**

---

### 7. Cross Validation

* Applied 5-fold cross-validation
* Mean F1-score: ~0.87

This confirms the model generalizes well.

---

##  Final Model

* Algorithm: XGBoost
* Output:

  * Prediction (Presence / Absence)
  * Probability score

---

##  Web Application (Streamlit)

The application includes:

### Features:

* Input form for patient details
* Validation for missing inputs
* Real-time prediction
* Risk score visualization
* Clinical interpretation
* Personalized recommendations
* Reset functionality
* Input form UI
* Prediction output
* Risk interpretation section

---

##  Clinical Interpretation Logic

The model output is categorized as:

* 🔴 High Risk (Probability > 0.7)
* 🟠 Moderate Risk (0.4 – 0.7)
* 🟢 Low Risk (< 0.4)

This makes the system more usable in real-world scenarios.

---

##  Recommendation System

Recommendations are dynamically generated based on:

* Model prediction
* Patient input values (BP, Cholesterol)

Example:

* High risk → immediate consultation
* Moderate risk → lifestyle changes
* Low risk → maintain healthy habits

---

##  Challenges Faced

* Understanding encoded categorical values
* Handling model convergence issues
* Designing user-friendly UI
* Managing Streamlit session state for reset functionality
* Interpreting model predictions meaningfully

---

##  Key Learnings

* End-to-end ML workflow
* Importance of feature importance
* Model evaluation beyond accuracy
* Building real-world ML applications
* UI/UX considerations in data science

---

##  Deployment

* Deployed using **Streamlit Community Cloud**
* Publicly accessible via web

---

##  Disclaimer

This application is intended for **educational and decision-support purposes only**.
It should not be used as a substitute for professional medical diagnosis.

---

##  Future Improvements

* Add explainable AI 
* Add PDF report generation
* Integrate with hospital systems
* Improve UI dashboard design

---

##  Tech Stack

* Python
* Pandas
* Scikit-learn
* XGBoost
* Streamlit


---

##  Conclusion

This project demonstrates a complete machine learning pipeline from data analysis to deployment. It highlights how machine learning can be applied in healthcare for early risk detection and decision support.

The system successfully combines prediction, interpretation, and usability, making it a practical real-world application.

---

## 👩‍💻 Author

**Aswini Dileep** aswinidileep91@gmail.com


