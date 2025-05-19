# 🩺 Multiple Disease Prediction Web App

A user-friendly **Machine Learning web application** built with **Streamlit**, enabling early prediction of **Diabetes**, **Heart Disease**, and **Parkinson’s Disease** based on key clinical parameters.

> 🔬 Designed for educational purposes and quick health assessments — not a substitute for professional medical advice.


## 🧠 Technologies Used

- **Python**
- **Streamlit**
- **Scikit-learn**
- **Pandas**
- **NumPy**
- **Git & GitHub**



## ⚙️ Features

- 🔍 **Disease Prediction**  
  - **Diabetes** – Based on metrics like glucose, BMI, pregnancies, etc.  
  - **Heart Disease** – Based on cholesterol, blood pressure, chest pain type, etc.  
  - **Parkinson’s Disease** – Based on voice frequency, jitter, etc.

- 📊 **ML Models Used**
  - **Support Vector Classifier (SVC)**
  - **Logistic Regression**
  - **Random Forest (Optional, extendable)**

- 💡 **User Input Interface**  
  Easy-to-use sidebar forms to enter clinical data for prediction.

- ✅ **Real-time Results**  
  Predictions are made instantly upon submission.



## 📁 Project Structure
```
Multiple-disease-prediction/
│
├── diabetes_model.sav # Trained Diabetes prediction model
├── heart_model.sav # Trained Heart disease prediction model
├── parkinsons_model.sav # Trained Parkinson's prediction model
├── multiple_disease_prediction.py # Main Streamlit application
├── requirements.txt # Required Python packages
└── README.md # Project documentation
```



## 🚀 How to Run Locally

1. **Clone the repository**  
   ```
   git clone https://github.com/Sindhubodapati/Multiple-disease-prediction.git
   cd Multiple-disease-prediction


2. **Create a virtual environment (optional but recommended)**
```
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```
pip install -r requirements.txt

```
4. **Run the app**

```
streamlit run multiple_disease_prediction.py

```
