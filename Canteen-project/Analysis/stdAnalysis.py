import csv
import streamlit as st 
import pandas as pd
import plotly.express as px 

def Student(stdid):
      file = open('/home/student88/CanteenMangmentSystem/Canteen-Management-System/Canteen-project/studentDailyOrder.csv')
      df = pd.read_csv(file)
      st.header("Student Vs Amount")
      id = st.selectbox("Select id",df['id'],0)
    #   if st.checkbox("Show Data "):
    #     st.table()
    #   a = int(stdId)
      if id == stdid: 
         a =df[df['id'] == id ]
         fig = px.bar(a,x='date',y='amount')
         st.write(fig)
      else :
         raise Exception("Error")

if __name__ == '__main__':
    Student(1)