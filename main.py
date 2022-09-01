import streamlit as st
import pandas as pd
import pickle
import numpy as np
df=pd.read_csv('../datasets/Anime.csv')
model=pickle.load(open(r'C:\Users\amanb\OneDrive\Desktop\Coding\Pyfiles\ipynbs\model.pkl','rb'))

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://wallpaperaccess.com/full/1915194.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

def returnPredictions(opt):
    ans=df[df['Name']==opt].index[0]
    rec_index=model[ans]
    fin_name=[]
    for i in rec_index:
        fin_name.append(df['Name'][i])
    return fin_name

original_title = '<p style="font-family:fantasy; color:Black; font-size: 20px;background-color: white;">Enter Anime Name</p>'
st.markdown(original_title, unsafe_allow_html=True)

opt=st.selectbox(
     '',
     (list(df['Name'])))

if st.button('Recommend'):
     st.write(returnPredictions(opt))






    

    