import pandas as pd
# import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='white')
st.set_page_config(layout="wide")

st.header("Air Quality Dataset Analysis")

##Read Data
Aotizhongxin = pd.read_csv('PRSA_Data_20130301-20170228/PRSA_Data_Aotizhongxin_20130301-20170228.csv',usecols = ['year','month','RAIN','TEMP'])
Changping = pd.read_csv('PRSA_Data_20130301-20170228/PRSA_Data_Changping_20130301-20170228.csv',usecols = ['year','month','RAIN','TEMP'])

#Get Monthly Recap
monthly_recap_rain_Aotizhongxin = Aotizhongxin.groupby(by='month')["RAIN"].mean().reset_index()
monthly_recap_rain_Changping = Changping.groupby(by='month')["RAIN"].mean().reset_index()

monthly_recap_temp_Aotizhongxin = Aotizhongxin.groupby(by='month')["TEMP"].mean().reset_index()
monthly_recap_temp_Changping = Changping.groupby(by='month')["TEMP"].mean().reset_index()

st.subheader('Question 1: Bagaimana perbandingan curah hujan pada kota Aotizhongxin dan kota changping pada tahun 2016?')
monthly_recap_rain_Aotizhongxin_Changping = monthly_recap_rain_Aotizhongxin.join(monthly_recap_rain_Changping,on='month',how='inner',lsuffix='_Aotizhongxin',rsuffix='_Changping')
st.line_chart(monthly_recap_rain_Aotizhongxin_Changping,x='month', y=['RAIN_Aotizhongxin','RAIN_Changping'], color=["#FF0000", "#0000FF"])


st.subheader('Question 2: Bagaimana perbandingan temperatur pada kota Aotizhongxin dan kota changping pada tahun 2016?')
monthly_recap_temp_Aotizhongxin_Changping = monthly_recap_temp_Aotizhongxin.join(monthly_recap_temp_Changping,on='month',how='inner',lsuffix='_Aotizhongxin',rsuffix='_Changping')
st.line_chart(monthly_recap_temp_Aotizhongxin_Changping,x='month', y=['TEMP_Aotizhongxin','TEMP_Changping'], color=["#FF0000", "#0000FF"])

st.subheader('Question 3: Apakah curah hujan mempengaruhi temperatur pada tahun 2016 di kota Aotizhongxin dan kota changping?')
monthly_recap_temp_rain_Aotizhongxin = Aotizhongxin.groupby(by='month')[["RAIN","TEMP"]].mean().reset_index()
st.scatter_chart(monthly_recap_temp_rain_Aotizhongxin,x='TEMP',y='RAIN')