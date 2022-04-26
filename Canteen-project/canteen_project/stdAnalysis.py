import csv
import streamlit as st 
import pandas as pd
import plotly.express as px 

def Student(stdid):
      file = open('/Canteen-Management-System/Canteen-project/studentDailyOrder.csv')
      df = pd.read_csv(file)
      st.header("Student Vs Amount")
      id = st.selectbox("Select id",df['id'],0)
      # # a = int(stdId)
      if id == stdid: 

         a =df[df['id'] == id ]
         
         fig = px.bar(a,x='name',y='amount')
         st.write(fig)
      else :
         raise Exception("Error")
if __name__ == '__main__':
    Student(1)