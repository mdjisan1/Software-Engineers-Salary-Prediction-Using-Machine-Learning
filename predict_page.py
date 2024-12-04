import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('salary_model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]
le_employment = data["le_employment"]

def show_predict_page():
    st.title("Software Engineers Salary Prediction")

    st.write("""### We need some information to predict the salary""")

    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
        "Turkey",
        "Switzerland",
        "Israel",
        "Pakistan",
        "Romania",
        "Mexico",
        "Czech Republic",
        "Ukraine",
        "Austria",
        "South Africa",
        "Ireland",
        "Iran",
        "Norway",
        "Belgium",
        "Denmark",
        "Portugal",
        "Argentina",
        "Hungary",
        "Finland",
        "New Zealand",
        "Greece",
    )

    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    employment = (
        "Full time",
        "Part time",
        "No employment",
    )

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education)
    employment = st.selectbox("Employment Level", employment)

    expericence = st.slider("Years of Experience", 0, 50, 3)

    ok = st.button("Calculate Salary")
    if ok:
        X = np.array([[country, education, employment, expericence ]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X[:, 2] = le_employment.transform(X[:,2])
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"The estimated yearly salary is ${salary[0]:.2f}")