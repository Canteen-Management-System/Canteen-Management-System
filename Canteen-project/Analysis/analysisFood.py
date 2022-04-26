import csv
import streamlit as st 
import pandas as pd
import plotly.express as px 
file = open('canteen_project/nutrients_csvfile.csv')
df = pd.read_csv(file)
class Analysis():
   st.title("Nutritional Facts for most common foods")
   st.header("Overview")
   
 
   txt = st.text_area('', '''
     Everybody nowadays is mindful of what they eat . 
     Counting calories and reducing fat intake is the number one advice given by all dieticians and nutritionists .
     Therefore, we need to know what foods are rich in what nutrients, don't we? (...)
     ''')
   st.header("Content")
   
 
   txt = st.text_area('', '''
     this  analysis contains a data for the Top 20 foods in the world each with the amount of Calories , Fats , Proteins , 
     Saturated Fats, Carbohydrates, Fibers labelled for each food . Also, the foods are also categorised into various groups 
     like Desserts, Vegetables, Fruits etc.
     ''')
    # st.write('Sentiment:', run_sentiment_analysis(txt))
    
   
   if st.checkbox("Show Data "):
      st.table(df)
   
   
   def FoodCalory():
      st.header("Food Vs Calories")
      st.text("check out this graphs show  the comparison  of the Calories for each of the food lidt   ")
      fig = px.bar(df,x='Food',y='Calories')
      st.write(fig)
   def FoodProtein():
      st.header("Food Vs Protein")
      st.text(" check out this graphs show  the comparison  of the Protein for each of the food lidt   ")
      fig = px.bar(df,x='Food',y='Protein')
      st.write(fig)
if __name__ == '__main__':
    Analysis.FoodProtein()
    Analysis.FoodCalory()
