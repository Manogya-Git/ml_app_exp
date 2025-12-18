import streamlit as st
import mlflow

st.title("My new Application")
age = st.sidebar.slider('Age',min_value=1,max_value=100,step=1)
gender = st.sidebar.selectbox('Gender',['Male','Female','Others'])
