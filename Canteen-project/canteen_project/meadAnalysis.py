import csv
import streamlit as st 
import pandas as pd
import plotly.express as px 

def Meal():
      file = open('/Canteen-Management-System/Canteen-project/MealQuantity.csv')
      df = pd.read_csv(file)
      st.header("Item Vs Quantity")
      my_row = st.slider("select Rows", min_value=1,max_value=df.shape[0])
      st.dataframe(df.head(my_row))
      fig = px.bar(df,x='Item',y='Quantity')
      st.write(fig)


if __name__ == '__main__':
    Meal()