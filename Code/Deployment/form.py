import streamlit as st
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from imblearn.over_sampling import SMOTE
import joblib 



pickle_in = open("/Users/nouhailanigrou/Desktop/ID/ID2/S3/ML/ASD/classification.pkl", "rb")
classifier = joblib.load(pickle_in)

p2 = open('/Users/nouhailanigrou/Desktop/ID/ID2/S3/ML/ASD/scaling_model.pkl', "rb")
scaling_model = joblib.load(p2)

p3 = open('/Users/nouhailanigrou/Desktop/ID/ID2/S3/ML/ASD/label_encoder.pkl', "rb")
label_encoder = joblib.load(p3) 

def main():
    def preprocess_input(input_data, scaler):
        df = pd.DataFrame([input_data], index=[0])
        df['gender'] = label_encoder.fit_transform(df['gender'])
        df['jaundice'] = label_encoder.fit_transform(df['jaundice'])
        df['autism'] = label_encoder.fit_transform(df['autism'])
        df['ethnicity'] = label_encoder.fit_transform(df['ethnicity'])
        df['relation'] = label_encoder.fit_transform(df['relation'])
        df = df.drop(["country_of_res", "used_app_before"], axis=1)
        X_std = scaling_model.transform(df)
        return X_std

    def predict_autism(input_data, svm_model, scaler):
        if any(value == '' for value in input_data.values()):
            st.warning('Please fill in all the fields.')
            return None, None

        input_data = {
            'A1_Score': int(input_data['A1_Score']),
            'A2_Score': int(input_data['A2_Score']),
            'A3_Score': int(input_data['A3_Score']),
            'A4_Score': int(input_data['A4_Score']),
            'A5_Score': int(input_data['A5_Score']),
            'A6_Score': int(input_data['A6_Score']),
            'A7_Score': int(input_data['A7_Score']),
            'A8_Score': int(input_data['A8_Score']),
            'A9_Score': int(input_data['A9_Score']),
            'A10_Score': int(input_data['A10_Score']),
            'age': float(input_data['age']),
            'gender': input_data['gender'],
            'ethnicity': input_data['ethnicity'],
            'jaundice': input_data['jaundice'],
            'autism': input_data['autism'],
            'country_of_res': input_data['country_of_res'],
            'used_app_before': input_data['used_app_before'],
            'relation': input_data['relation']
        }

        X_std = preprocess_input(input_data, scaling_model)
        probability = classifier.predict_proba(X_std)[:, 1]
        prediction = classifier.predict(X_std)
        return prediction, probability

    st.title(":bookmark_tabs: :blue[Autism Spectrum Disorder Evaluation]")
    st.write("---")
    st.write("Fill the form below to check if you are suffering from ASD ")
    st.write("SCORING: Only 1 point can be scored for each question. Score 1 point for Definitely or Slightly Agree on each of items 1, 7, 8, and 10. Score 1 point for Definitely or Slightly Disagree on each of items 2, 3, 4, 5, 6, and 9. ")


    A = ["f", "m"]
    B = ["Yes", "No"]
    C = ["Yes", "No"]
    D = ["Yes", "No"]
    E = ["Self", "Parent", "Health Care Professional", "Others", "Unknown"]
    F = ['United States', 'Australia', 'United Kingdom', 'New Zealand',
         'Italy', 'Nicaragua', 'Canada', 'United Arab Emirates',
         'Netherlands', 'Sri Lanka', 'India', 'Armenia', 'Sierra Leone',
         'Argentina', 'Azerbaijan', 'Iceland', 'Egypt', 'Serbia',
         'Afghanistan', 'Costa Rica', 'Jordan', 'Angola', 'Pakistan',
         'Brazil', 'Ireland', 'Kazakhstan', 'Viet Nam', 'Ethiopia',
         'Austria', 'Finland', 'France', 'Malaysia', 'Japan', 'Spain',
         'Philippines', 'Iran', 'Czech Republic', 'Russia', 'Romania',
         'Mexico', 'Belgium', 'Aruba', 'Uruguay', 'Indonesia', 'Ukraine',
         'AmericanSamoa', 'Germany', 'China', 'Iraq', 'Tonga',
         'South Africa', 'Saudi Arabia', 'Hong Kong', 'Bahamas', 'Ecuador',
         'Cyprus', 'Bangladesh', 'Oman', 'Bolivia', 'Sweden', 'Niger',
         'Burundi', 'Lebanon', 'Chile', 'Portugal', 'Turkey', 'Nepal']
    G = ['White-European', 'South Asian', 'Black', 'Asian',
         'Middle Eastern ', 'Unknown', 'others', 'Latino', 'Turkish', 'Others',
         'Hispanic', 'Pasifika']

    # Collect input from the user
    A1_Score = st.slider('I often notice small sounds when others do not', 0, 1)
    A2_Score = st.slider('I usually concentrate more on the whole picture, rather than the small details', 0, 1)
    A3_Score = st.slider('I find it easy to do more than one thing at one', 0, 1)
    A4_Score = st.slider('If there is an interruption, I can switch back to what I was doing very quickly', 0, 1)
    A5_Score = st.slider('I find it easy to read between the lines when someone is talking to me', 0, 1)
    A6_Score = st.slider('I know how to tell if someone listening to me is getting bored', 0, 1)
    A7_Score = st.slider('When I m reading a story, I find it difficult to work out the characters intentions', 0, 1)
    A8_Score = st.slider('I like to collect information about categories of things (e.g. types of car, types of bird etc', 0, 1)
    A9_Score = st.slider('I find it easy to work out what someone is thinking or feeling just by looking at their face', 0, 1)
    A10_Score = st.slider('I find it difficult to work out people s intentions', 0, 1)
    age = st.text_input('Age')
    gender = st.selectbox('Gender', A)
    ethnicity = st.selectbox('Ethnicity', G)
    jaundice = st.selectbox('Jaundice', B)
    autism = st.selectbox('Autistic member in the family', C)
    country_of_res = st.selectbox('Country of residence', F)
    used_app_before = st.selectbox('Used app before', D)
    relation = st.selectbox('Relation', E)

    input_data = {
        'A1_Score': A1_Score,
        'A2_Score': A2_Score,
        'A3_Score': A3_Score,
        'A4_Score': A4_Score,
        'A5_Score': A5_Score,
        'A6_Score': A6_Score,
        'A7_Score': A7_Score,
        'A8_Score': A8_Score,
        'A9_Score': A9_Score,
        'A10_Score': A10_Score,
        'age': age,
        'gender': gender,
        'ethnicity': ethnicity,
        'jaundice': jaundice,
        'autism': autism,
        'country_of_res': country_of_res,
        'used_app_before': used_app_before,
        'relation': relation
    }

    with st.expander("Examine Input Data"):
        st.subheader("Results:")
        prediction, probability = predict_autism(input_data, classifier, scaling_model)

        if prediction is not None:
            if prediction[0] == 0:
                st.info('The person is not with Autism spectrum disorder')
            else:
                st.warning('The person is with Autism spectrum disorder')
            probability_percentage = probability[0] * 100
            st.write(f'Probability of having Autism: {probability_percentage:.2f}%')

if __name__ == "__main__":
    main()
