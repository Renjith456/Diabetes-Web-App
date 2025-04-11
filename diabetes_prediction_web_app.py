# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 19:40:25 2025

@author: rajes
"""

import numpy as np
import pickle
import streamlit as st
loaded_model=pickle.load(open('C:/Users/rajes/Downloads/trained_model.sav','rb'))
def diabetes_predition(input_data):
    
    input_array=np.asarray(input_data)
    input_reshaped=input_array.reshape(1,-1)
    prediction=loaded_model.predict(input_reshaped)
    print(prediction)
    if prediction[0]==0:
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'


def main():
    
    #giving a title
    st.title('Diabetes Predicton Web App')
    
    #getting input from user
    Pregnancies=st.text_input("Number of Pregnencies")
    Glucose=st.text_input("Glucose_level")
    BloodPressure=st.text_input("Blood Pressure value")
    SkinThickness=st.text_input("Skin Thickness value")
    BMI=st.text_input("BMI value")
    DiabetesPedigreeFunction=st.text_input("DiabetesPedigreeFunction value")
    Age=st.text_input("Enter age")
    
    #code for prediction
    diagnosis= ''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis=diabetes_predition([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(diagnosis)
    
if __name__=='__main__':
    main()