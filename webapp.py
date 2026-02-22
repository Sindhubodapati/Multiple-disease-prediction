import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pytesseract

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Set the Tesseract-OCR path if needed
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
diabetes_model = pickle.load(open('C:\\Users\\sindh\\OneDrive\\Desktop\\diseases-prediction\\disease prediction\\diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('C:\\Users\\sindh\\OneDrive\\Desktop\\diseases-prediction\\disease prediction\\heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('C:\\Users\\sindh\\OneDrive\\Desktop\\diseases-prediction\\disease prediction\\parkinsons_model.sav', 'rb'))

def display_made_by():
    st.markdown("""
        <h5 style='text-align: left; color: black;'>
            Made by Sindhu &hearts; 
        </h5>
    """, unsafe_allow_html=True)

display_made_by()
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)
    




# Function to perform OCR on uploaded images
def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    sndhu=sindhu
    renuka=renuka
    return text

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    # Option to upload an image or enter data manually
    input_method = st.radio("Choose input method:", ("Upload Image", "Enter Data Manually"))

    if input_method == "Upload Image":
        uploaded_file = st.file_uploader("Upload a scanned medical report", type=["jpg", "png", "jpeg", "pdf"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', use_column_width=True)

            # Extract text using OCR
            extracted_text = extract_text_from_image(image)
            st.write("Extracted Data:")
            st.text(extracted_text)

            # Display extracted data for users to confirm or edit
            st.write("Please review and adjust the extracted values if needed:")
            Pregnancies = st.text_input('Number of Pregnancies', value="0")
            Glucose = st.text_input('Glucose Level', value="0")
            BloodPressure = st.text_input('Blood Pressure value', value="0")
            SkinThickness = st.text_input('Skin Thickness value', value="0")
            Insulin = st.text_input('Insulin Level', value="0")
            BMI = st.text_input('BMI value', value="0")
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', value="0")
            Age = st.text_input('Age of the Person', value="0")
        else:
            st.warning("Please upload an image")

    if input_method == "Enter Data Manually":
        # Getting the input data from the user
        col1, col2, col3 = st.columns(3)

        with col1:
            Pregnancies = st.text_input('Number of Pregnancies')

        with col2:
            Glucose = st.text_input('Glucose Level')

        with col3:
            BloodPressure = st.text_input('Blood Pressure value')

        with col1:
            SkinThickness = st.text_input('Skin Thickness value')

        with col2:
            Insulin = st.text_input('Insulin Level')

        with col3:
            BMI = st.text_input('BMI value')

        with col1:
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

        with col2:
            Age = st.text_input('Age of the Person')

    # Code for prediction
    diab_diagnosis = ''

    # Creating a button for prediction
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)


# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    # Option to upload an image or enter data manually
    input_method = st.radio("Choose input method:", ("Upload Image", "Enter Data Manually"))

    if input_method == "Upload Image":
        uploaded_file = st.file_uploader("Upload a scanned medical report", type=["jpg", "png", "jpeg", "pdf"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', use_column_width=True)

            # Extract text using OCR
            extracted_text = extract_text_from_image(image)
            st.write("Extracted Data:")
            st.text(extracted_text)

            # Display extracted data for users to confirm or edit
            st.write("Please review and adjust the extracted values if needed:")
            age = st.text_input('Age', value="0")
            sex = st.text_input('Sex', value="0")
            cp = st.text_input('Chest Pain types', value="0")
            trestbps = st.text_input('Resting Blood Pressure', value="0")
            chol = st.text_input('Serum Cholestoral in mg/dl', value="0")
            fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl', value="0")
            restecg = st.text_input('Resting Electrocardiographic results', value="0")
            thalach = st.text_input('Maximum Heart Rate achieved', value="0")
            exang = st.text_input('Exercise Induced Angina', value="0")
            oldpeak = st.text_input('ST depression induced by exercise', value="0")
            slope = st.text_input('Slope of the peak exercise ST segment', value="0")
            ca = st.text_input('Major vessels colored by flourosopy', value="0")
            thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', value="0")
        else:
            st.warning("Please upload an image")

    if input_method == "Enter Data Manually":
        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.text_input('Age')

        with col2:
            sex = st.text_input('Sex')

        with col3:
            cp = st.text_input('Chest Pain types')

        with col1:
            trestbps = st.text_input('Resting Blood Pressure')

        with col2:
            chol = st.text_input('Serum Cholestoral in mg/dl')

        with col3:
            fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

        with col1:
            restecg = st.text_input('Resting Electrocardiographic results')

        with col2:
            thalach = st.text_input('Maximum Heart Rate achieved')

        with col3:
            exang = st.text_input('Exercise Induced Angina')

        with col1:
            oldpeak = st.text_input('ST depression induced by exercise')

        with col2:
            slope = st.text_input('Slope of the peak exercise ST segment')

        with col3:
            ca = st.text_input('Major vessels colored by flourosopy')

        with col1:
            thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # Code for prediction
    heart_diagnosis = ''

    # Creating a button for prediction
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)


# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    # Option to upload an image or enter data manually
    input_method = st.radio("Choose input method:", ("Upload Image", "Enter Data Manually"))

    if input_method == "Upload Image":
        uploaded_file = st.file_uploader("Upload a scanned medical report", type=["jpg", "png", "jpeg", "pdf"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', use_column_width=True)

            # Extract text using OCR
            extracted_text = extract_text_from_image(image)
            st.write("Extracted Data:")
            st.text(extracted_text)

            # Display extracted data for users to confirm or edit
            fo = st.text_input('MDVP:Fo(Hz)', value="0")
            fhi = st.text_input('MDVP:Fhi(Hz)', value="0")
            flo = st.text_input('MDVP:Flo(Hz)', value="0")
            Jitter_percent = st.text_input('MDVP:Jitter(%)', value="0")
            Jitter_Abs = st.text_input('MDVP:Jitter(Abs)', value="0")
            RAP = st.text_input('MDVP:RAP', value="0")
            PPQ = st.text_input('MDVP:PPQ', value="0")
            DDP = st.text_input('Jitter:DDP', value="0")
            Shimmer = st.text_input('MDVP:Shimmer', value="0")
            Shimmer_dB = st.text_input('MDVP:Shimmer(dB)', value="0")
            APQ3 = st.text_input('Shimmer:APQ3', value="0")
            APQ5 = st.text_input('Shimmer:APQ5', value="0")
            APQ = st.text_input('MDVP:APQ', value="0")
            DDA = st.text_input('Shimmer:DDA', value="0")
        else:
            st.warning("Please upload an image")

    if input_method == "Enter Data Manually":
        col1, col2, col3 = st.columns(3)

        with col1:
            fo = st.text_input('MDVP:Fo(Hz)')

        with col2:
            fhi = st.text_input('MDVP:Fhi(Hz)')

        with col3:
            flo = st.text_input('MDVP:Flo(Hz)')

        with col1:
            Jitter_percent = st.text_input('MDVP:Jitter(%)')

        with col2:
            Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

        with col3:
            RAP = st.text_input('MDVP:RAP')

        with col1:
            PPQ = st.text_input('MDVP:PPQ')

        with col2:
            DDP = st.text_input('Jitter:DDP')

        with col3:
            Shimmer = st.text_input('MDVP:Shimmer')

        with col1:
            Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

        with col2:
            APQ3 = st.text_input('Shimmer:APQ3')

        with col3:
            APQ5 = st.text_input('Shimmer:APQ5')

        with col1:
            APQ = st.text_input('MDVP:APQ')

        with col2:
            DDA = st.text_input('Shimmer:DDA')

    # Code for prediction
    parkinsons_diagnosis = ''

    # Creating a button for prediction
    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer,
                      Shimmer_dB, APQ3, APQ5, APQ, DDA]
        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)


