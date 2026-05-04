import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("heart_disease_model.pkl", "rb"))

st.set_page_config(page_title="Heart Disease App", layout="centered")

# ---------------- RESET FLAG ----------------
if "reset_flag" not in st.session_state:
    st.session_state.reset_flag = False

# ---------------- HANDLE RESET BEFORE WIDGETS ----------------
if st.session_state.reset_flag:
    for key in ["age", "sex", "cp", "bp", "chol", "fbs", "ekg",
                "max_hr", "ex_angina", "st_dep", "slope", "vessels", "thal"]:
        st.session_state[key] = None
    st.session_state.reset_flag = False

# ---------------- UI ----------------
st.markdown("<h1 style='text-align: center;'>❤️ Heart Disease Prediction</h1>", unsafe_allow_html=True)

st.write("### Enter Patient Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 20, 100, value=None,
                          placeholder="Enter age (e.g., 55)", key="age")

    sex = st.radio("Sex", ["Male", "Female"], index=None,
                   horizontal=True, key="sex")

    cp = st.selectbox("Chest Pain Type",
                      {1: "Typical Angina",
                       2: "Atypical Angina",
                       3: "Non-anginal Pain",
                       4: "Asymptomatic"}.keys(),
                      format_func=lambda x: {
                          1: "Typical Angina",
                          2: "Atypical Angina",
                          3: "Non-anginal Pain",
                          4: "Asymptomatic"
                      }[x],
                      index=None,
                      placeholder="Select chest pain type",
                      key="cp")

    bp = st.number_input("Blood Pressure", 60, 200, value=None,
                         placeholder="Enter BP (e.g., 120)", key="bp")

    chol = st.number_input("Cholesterol", 100, 600, value=None,
                           placeholder="Enter cholesterol (e.g., 200)", key="chol")

    fbs = st.radio("Fasting Blood Sugar > 120", ["Yes", "No"],
                   index=None, horizontal=True, key="fbs")

    ekg = st.selectbox("EKG Results",
                       {0: "Normal",
                        1: "ST-T abnormality",
                        2: "Left ventricular hypertrophy"}.keys(),
                       format_func=lambda x: {
                           0: "Normal",
                           1: "ST-T abnormality",
                           2: "Left ventricular hypertrophy"
                       }[x],
                       index=None,
                       placeholder="Select EKG results",
                       key="ekg")

with col2:
    max_hr = st.number_input("Max Heart Rate", 60, 220, value=None,
                             placeholder="Enter Max HR (e.g., 150)", key="max_hr")

    ex_angina = st.radio("Exercise Angina", ["Yes", "No"],
                         index=None, horizontal=True, key="ex_angina")

    st_dep = st.number_input("ST Depression", 0.0, 6.3, value=None,
                             placeholder="Enter ST depression (e.g., 1.0)", key="st_dep")

    slope = st.selectbox("Slope of ST",
                         {1: "Upsloping",
                          2: "Flat",
                          3: "Downsloping"}.keys(),
                         format_func=lambda x: {
                             1: "Upsloping",
                             2: "Flat",
                             3: "Downsloping"
                         }[x],
                         index=None,
                         placeholder="Select slope",
                         key="slope")

    vessels = st.selectbox("Number of Vessels", [0, 1, 2, 3],
                           index=None,
                           placeholder="Select vessels",
                           key="vessels")

    thal = st.selectbox("Thallium Test",
                        {3: "Normal",
                         6: "Fixed Defect",
                         7: "Reversible Defect"}.keys(),
                        format_func=lambda x: {
                            3: "Normal",
                            6: "Fixed Defect",
                            7: "Reversible Defect"
                        }[x],
                        index=None,
                        placeholder="Select Thallium",
                        key="thal")

# ---------------- BUTTONS ----------------
col_btn1, col_btn2 = st.columns(2)

predict_clicked = col_btn1.button("Predict", use_container_width=True)
reset_clicked = col_btn2.button("Reset", use_container_width=True)

# ---------------- RESET ----------------
if reset_clicked:
    st.session_state.reset_flag = True
    st.rerun()

# ---------------- PREDICTION ----------------
if predict_clicked:

    if (
        age is None or sex is None or cp is None or bp is None or chol is None or
        fbs is None or ekg is None or max_hr is None or ex_angina is None or
        st_dep is None or slope is None or vessels is None or thal is None
    ):
        st.warning("⚠️ Please fill all fields before prediction.")

    else:
        # Convert inputs
        sex_val = 1 if sex == "Male" else 0
        fbs_val = 1 if fbs == "Yes" else 0
        ex_angina_val = 1 if ex_angina == "Yes" else 0

        input_data = pd.DataFrame({
            "Age": [age],
            "Sex": [sex_val],
            "Chest pain type": [cp],
            "BP": [bp],
            "Cholesterol": [chol],
            "FBS over 120": [fbs_val],
            "EKG results": [ekg],
            "Max HR": [max_hr],
            "Exercise angina": [ex_angina_val],
            "ST depression": [st_dep],
            "Slope of ST": [slope],
            "Number of vessels fluro": [vessels],
            "Thallium": [thal]
        })

        prediction = model.predict(input_data)[0]
        prob = model.predict_proba(input_data)[0][1]

        st.markdown("---")

        if prediction == 1:
            st.error(f"⚠️ High Risk of Heart Disease\n\nProbability: {prob:.2f}")
        else:
            st.success(f"✅ Low Risk (No Heart Disease)\n\nProbability: {1-prob:.2f}")

        st.write(f"Risk Score: {prob:.2%}")
        st.progress(int(prob * 100))


                # ---------------- RISK INTERPRETATION ----------------
        st.markdown("### 🩺 Clinical Interpretation")

        if prob > 0.7:
            st.error("🔴 High Risk: Immediate medical consultation recommended.")
        elif prob > 0.4:
            st.warning("🟠 Moderate Risk: Consider medical check-up and lifestyle changes.")
        else:
            st.success("🟢 Low Risk: Maintain a healthy lifestyle.")

        # ---------------- RECOMMENDATIONS ----------------
        st.markdown("### 💡 Recommendations")

        if prob > 0.7:
            st.write("- Consult a cardiologist immediately")
            st.write("- Undergo further diagnostic tests")
            st.write("- Monitor blood pressure and cholesterol regularly")

        elif prob > 0.4:
            st.write("- Improve diet and exercise regularly")
            st.write("- Schedule routine health checkups")
            st.write("- Reduce stress and maintain sleep schedule")

        else:
            st.write("- Maintain a balanced diet")
            st.write("- Exercise regularly")
            st.write("- Continue healthy lifestyle habits")

        # ---------------- DISCLAIMER ----------------
        st.markdown("### ⚠️ Disclaimer")
        st.warning("This prediction is for informational purposes only and should not be considered " \
        "a medical diagnosis. Please consult a qualified healthcare professional.")
