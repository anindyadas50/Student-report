# 🎓 Early Warning System for Student Performance

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B)](https://streamlit.io/)
[![Machine Learning](https://img.shields.io/badge/Model-Random%20Forest-green)](https://scikit-learn.org/)

## 📌 1. Project Context
Developed for an EdTech company, this **Early Warning System (EWS)** utilizes Machine Learning to identify students at risk of academic failure. By analyzing academic and behavioral attributes, the system enables educators to perform timely interventions, potentially improving graduation rates and student success.

## 🎯 2. Objectives
* **Predict:** Classify students as Pass (1) or Fail (0).
* **Analyze:** Identify the most influential factors behind student performance.
* **Deploy:** Provide a user-friendly interface for teachers to input student data and get instant risk assessments.

## 📊 3. Dataset Overview
The dataset contains 1,000 student records with the following features:
* **Study_Hours:** Number of hours spent studying daily.
* **Attendance:** Percentage of classes attended.
* **Previous_Marks:** Average marks from previous semesters.
* **Assignment_Score:** Current score in assignments.
* **Sleep_Hours:** Average daily sleep duration.
* **Internet_Usage:** Categorical level (Low, Medium, High).
* **Extra_Coaching:** Binary (0 = No, 1 = Yes).
* **Pass (Target):** Predicted outcome (0 = Fail, 1 = Pass).

## 🛠️ 4. Tech Stack
* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
* **Deployment:** Streamlit
* **Model Persistence:** Joblib

## 🚀 5. Installation & Setup
To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/anindyadas50/Student-report.git](https://github.com/anindyadas50/Student-report.git)
   cd Student-report
Install requirements:Bashpip install streamlit pandas numpy scikit-learn joblib matplotlib seaborn
Run the application:Bashstreamlit run app.py
📈 6. Model EvaluationThe system compares multiple models. The Random Forest Classifier was selected as the final model due to its high accuracy and robustness.MetricLogistic RegressionRandom ForestAccuracy~92%~98%Precision0.910.98Recall0.900.97💡 7. Key Insights & RecommendationsAttendance Matters: Attendance is the strongest predictor of success. Students below 65% attendance are categorized as "High Risk."Sleep Impact: A correlation was found between sleep hours and performance. Passing students averaged 6.61 hours, while failing students averaged 6.47 hours.Intervention: It is recommended that the institution provides mandatory extra coaching for any student whose predicted probability of passing falls below 50%.📂 8. Repository StructurePlaintext├── app.py                   # Streamlit Web Application
├── student_model.pkl        # Trained Random Forest Model
├── scaler.pkl               # Feature Scaler for Preprocessing
├── requirements.txt         # List of dependencies
└── README.md                # Project Documentation
📜 9. LicenseThis project is developed for the Situated Learning Assignment (BTEEZC512).
---

### **Don't forget the Requirements file!**
To make your repository "complete," you should also create a file named `requirements.txt` and paste this inside:

```text
streamlit
pandas
numpy
scikit-learn
joblib
matplotlib
seaborn
