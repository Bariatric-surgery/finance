import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict1,predict2


st.set_page_config(layout="wide")   

def cal_result():
    
    
    gender_list =['female', 'men']
    gender1 = gender_list.index(gender) +1

    depression_list= ['yes','no']
    depression1 = depression_list.index(depression) +1
    
    prior_abdominal_surgery_list =['yes', 'no']
    prior_abdominal_surgery1 = prior_abdominal_surgery_list.index(prior_abdominal_surgery) +1    
    
    Diabetes_list =['no','yes']
    Diabetes1 = Diabetes_list.index(Diabetes)
    
  
    osas_preoperaative_list =['no','yes']
    osas_preoperaative1 = osas_preoperaative_list.index(osas_preoperaative)
    
    surgery_list =['Laparoscopic Sleeve Gastrectomy','Roux en-Y Gastric Bypass']
    surgery1 = surgery_list.index(surgery)     
    
    
    no_complication = 0
    Anastomotic_leakage = 0
    Gastric_leakage = 0
    Intussusception = 0
    Mesenteric_internal_hernia = 0
    Internal_hernia_through_Peterson = 0
    Hiatal_hernia = 0
    Gastro_Esophageal = 0
    Amastomotic_Ulcera = 0
    
    if surgery1 == 0:
  
        complication_list = ['no complication','Gastric leakage', 'Hiatal hernia','Gastro Esophageal Reflux Disease (GERD)']
        complication1 = complication_list.index(complication)
        
        if complication1 ==0:
            no_complication = 1
        if complication1 ==1:
            Gastric_leakage = 1   
         
            
        if complication1 ==2:
            Hiatal_hernia = 1             
            
        if complication1 ==3:
            Gastro_Esophageal = 1    
    if surgery1 == 1:
        complication_list = ['no complication','Anastomotic leakage', 'Intussusception','Mesenteric internal hernia',
                           'Internal hernia through Petersons','Hiatal hernia','Gastro Esophageal Reflux Disease','Amastomotic Ulcera']
        
        complication1 = complication_list.index(complication)
        if complication1 ==0:
            no_complication = 1
            
        if complication1 ==1:
            Anastomotic_leakage = 1   
 
            
        if complication1 ==2:
            Intussusception = 1             
            
        if complication1 ==3:
            Mesenteric_internal_hernia = 1
            
        if complication1 == 4:
            Internal_hernia_through_Peterson = 1      
            
        if complication1 == 5:
            Hiatal_hernia = 1 

        if complication1 == 6:
            Gastro_Esophageal = 1

        if complication1 == 7:
            Amastomotic_Ulcera = 1 
            
    X = [gender1, age, asa, charleson_comorbidity_index,
     depression1, prior_abdominal_surgery1, Diabetes1, surgery1, surgery_time, real_anesthesia_time,
     Anastomotic_leakage, Gastric_leakage, Intussusception, Mesenteric_internal_hernia,
     Internal_hernia_through_Peterson, Hiatal_hernia, Gastro_Esophageal, no_complication,
     Amastomotic_Ulcera, bmi_pre, hospital_days, osas_preoperaative1] 
    
    X = np.array(X)
    X = X.reshape(1, -1)
            
            
    result = predict1(X)
    st.text("Final cost")
    st.text(str(int(result[0])) +" CHF")
    
    result2 = predict2(X)
    st.text("Final Revenue")
    st.text(str(int(result2[0])) +" CHF")    

st.title('Predict model')



col1, col2, col3 = st.columns(3)

with col1:
    st.header('Categorical Input')
    gender =st.selectbox('gender', ('female','men'))
    asa = st.selectbox('ASA score', ('1','2','3','4'))
    
    
    depression = st.selectbox('depression', ('yes','no'))
    
  
    prior_abdominal_surgery = st.selectbox('prior abdominal surgery', ('yes','no'))
    Diabetes = st.selectbox('Diabetes mellitus type II preoperativ', ('yes','no'))
    surgery = st.selectbox('surgery', ('Laparoscopic Sleeve Gastrectomy', 'Roux en-Y Gastric Bypass'))
    
    osas_preoperaative = st.selectbox('osas preoperaative', ('yes','no'))
    
    if surgery=='Laparoscopic Sleeve Gastrectomy':
        complication = st.selectbox('complication', ('no complication','Gastric leakage', 'Hiatal hernia','Gastro Esophageal Reflux Disease (GERD)'))
    if surgery=='Roux en-Y Gastric Bypass':
        complication = st.selectbox('complication', ('no complication','Anastomotic leakage', 'Intussusception','Mesenteric internal hernia',
                                                  'Internal hernia through Petersons','Hiatal hernia','Gastro Esophageal Reflux Disease','Amastomotic Ulcera'))
    

with col2:
    st.header('Numerical Input')

    
    charleson_comorbidity_index = st.slider('charleson comorbidity index', min_value=0, max_value=20,value=5, step=1)
    
    age = st.slider('age', min_value=18, max_value=100,value=51,step=1)
    surgery_time = st.slider('surgery time(min)', min_value=50, max_value=500,value=88,step=1)
    
    real_anesthesia_time = st.slider('real anesthesia time(min)', min_value=50, max_value=500,value=91,step=1)
    hospital_days = st.slider('length of hospital stay(days)', min_value=1, max_value=25,value=4,step=1)
    
    bmi_pre = st.slider('body mass index preoperative', min_value=35.0, max_value=60.0, value=36.,step=0.1)
   
   

with col3:
    st.header('result')
    
    if st.button('Predict'):
        cal_result()
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    