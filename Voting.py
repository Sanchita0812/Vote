import streamlit as st
import urllib
from PIL import Image
import time
import numpy as npp
import tensorflow as tf
from tensorflow import keras
#from tensorflow.keras.preprocessing import image
import pandas as pd
import pickle

# loading in the model to predict on the data
pickle_in = open('model1 (1).pkl', 'rb')
Voting = pickle.load(pickle_in)


def welcome():
    return 'welcome all'
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(Communication_Skills, Student_Involvement , Teacher_Relations, Leadership_Skills, Anonymous_Voting_Score):  
   
    prediction = Voting.predict(
        [[Communication_Skills, Student_Involvement, Teacher_Relations, Leadership_Skills, Anonymous_Voting_Score]])
    print(prediction)
    return prediction

def main():
    html_temp= '''
            <div>
            <center> <H1> How likely are you to be in the council! </H1> </center> </div>'''
    st.markdown(html_temp, unsafe_allow_html= True)
#@st.cache(allow_output_mutation= True, suppress_st_warning= True)
html_temp= '''
            <div>
            <center> <H3> Please upload the relevant data. </H3> </center> </div>'''
      
Communication_Skill = st.text_input("Communication Skill", "Type Here")
Student_Involvement = st.text_input("Student Involvement", "Type Here")
Teacher_Relations = st.text_input("Teacher Relations", "Type Here")
Leadership_Skills = st.text_input("Leadership Skills", "Type Here")
Anonymous_Voting_Score = st.text_input("Anonymous Voting Score", "Type Here")
result =""
            
if st.button("Predict"):
        result = prediction(Communication_Skill, Student_Involvement, Teacher_Relations, Leadership_Skills, Anonymous_Voting_Score)
st.success('The output is {}'.format(result))
     
if __name__=='__main__':
    main()        
