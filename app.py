import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. Load the saved model and scaler
model = joblib.load('student_model.pkl')
scaler = joblib.load('scaler.pkl')

# 2. Set up the UI Title and Description
st.set_page_config(page_title="Student Early Warning System", layout="centered")
st.title("🎓 Student Performance Prediction System")
st.write("""
This app predicts if a student is likely to **Pass** or **Fail** based on academic and behavioral data.
Use the sidebar to input student details.
""")

st.divider()

# 3. Sidebar for User Input
st.sidebar.header("Student Attributes")

def user_input_features():
    study_hours = st.sidebar.slider("Study Hours (Daily)", 1, 10, 5)
    attendance = st.sidebar.slider("Attendance %", 40, 100, 75)
    prev_marks = st.sidebar.slider("Previous Marks", 30, 100, 65)
    assignment_score = st.sidebar.slider("Assignment Score", 30, 100, 65)
    sleep_hours = st.sidebar.slider("Sleep Hours", 4, 10, 7)
    
    internet_usage = st.sidebar.selectbox("Internet Usage", ("Low", "Medium", "High"))
    # Map internet usage back to the same encoding used in training
    usage_map = {'Low': 0, 'Medium': 1, 'High': 2}
    internet_encoded = usage_map[internet_usage]
    
    extra_coaching = st.sidebar.radio("Extra Coaching?", ("Yes", "No"))
    coaching_encoded = 1 if extra_coaching == "Yes" else 0

    # Arrange data into a dictionary/dataframe (must match the order of training features)
    data = {
        'Study_Hours': study_hours,
        'Attendance': attendance,
        'Previous_Marks': prev_marks,
        'Assignment_Score': assignment_score,
        'Sleep_Hours': sleep_hours,
        'Internet_Usage': internet_encoded,
        'Extra_Coaching': coaching_encoded
    }
    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

# 4. Display Input Summary
st.subheader("Input Parameters Summary")
st.table(input_df)

# 5. Prediction Logic
# Scaling the input data using the loaded scaler
input_scaled = scaler.transform(input_df)

if st.button("Predict Performance"):
    prediction = model.predict(input_scaled)
    prediction_proba = model.predict_proba(input_scaled)

    st.subheader("Prediction Result")
    
    if prediction[0] == 1:
        st.success("✅ Prediction: This student is likely to **PASS**.")
    else:
        st.error("⚠️ Prediction: This student is **AT RISK** of failing.")
    
    # Confidence Score
    confidence = np.max(prediction_proba) * 100
    st.info(f"Model Confidence: {confidence:.2f}%")

# 6. Add contextual advice based on input
if input_df['Attendance'][0] < 60:
    st.warning("Recommendation: Low attendance is a high risk factor. Schedule a mentoring session.")