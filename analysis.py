import streamlit as st
#Widgets
value = st.slider('val')  # this is a widget
#Layout
#Streamlit runs the python script from top to bottom
#Each time the user interacts the script is a rerun from top to bottom
#Streamlit allows you to use caching for costly operations like loading large datasets
import pandas as pd
st.title("Welcome to Streamlit! DataFrame")
st.write("Our first DataFrame")
st.write(
  pd.DataFrame({
      'A': [1, 2, 3, 4],
      'B': [5, 6, 7, 8]
    })
) 
