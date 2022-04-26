
import csv
import streamlit as st 
import pandas as pd
import plotly.express as px 

file = open('/home/hind/Canteen-Management-System/Canteen-project/canteen_project/nutrients_csvfile.csv')
df = pd.read_csv(file)

class Analysis():


   st.title("Data Analysis")
   
 
# Create a button, that when clicked, shows a text
   if(st.button("Greeting")):
    st.text("Welcome To  Data Analysis !!!")
   

 
   # st.dataframe(df.head())
   if st.checkbox("Show Data "):

      st.table(df)

   def FoodCalory():
      st.header("Food Vs Calories")
      fig = px.bar(df,x='Food',y='Calories')
      st.write(fig)

   def FoodProtein():
      st.header("Food Vs Protein")
      fig = px.bar(df,x='Food',y='Protein')
      st.write(fig)
      
   def Student(stdid):
      file = open('/home/hind/Canteen-Management-System/Canteen-project/studentDailyOrder.csv')
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
      # my_row = st.slider("select Rows", min_value=1,max_value=df.shape[0])
      # st.dataframe(df.head(my_row))
      




   def Meal():
      file = open('/home/hind/Canteen-Management-System/Canteen-project/MealQuantity.csv')
      df = pd.read_csv(file)
      st.header("Item Vs Quantity")
      fig = px.bar(df,x='Item',y='Quantity')
      st.write(fig)
               
      # my_row = st.slider("select Rows", min_value=1,max_value=df.shape[0])
      # st.dataframe(df.head(my_row))

   # var = st.selectbox("select X-Axis",df.columns.tolist())
   # fig=px.bar(df,x=var,y="name")
   # fig

   # my_row = st.number_input("select Rows", min_value=1,max_value=df.shape[0])
   # st.dataframe(df.head(my_row))

   
if __name__ == '__main__':
   Analysis.FoodCalory()
   Analysis.FoodProtein()
   Analysis.Student(1)
   Analysis.Meal()