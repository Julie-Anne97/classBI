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
#Select box in streamlit
st.title("Welcome to Streamlit! Select Box")

selectbox = st.selectbox(
    "Select a person",
    ["Perrine", "Julie-Anne", "Edona", "Ismail"]
)
st.write(f"You selected {selectbox}")
#The first argument to st.selectbox is the string to display and the second argument is a list of options to select. 
#And then we display the selected value in the app using st.write method.

#Line chart in streamlit
import numpy as np
st.title("Welcome to Streamlit! Line chart")
st.write("Line Chart in Streamlit")
# 10 * 2 dimensional data
chart_data = pd.DataFrame(
    np.random.randn(10, 2),
    columns=[f"Col{i+1}" for i in range(2)]
)

st.line_chart(chart_data)
#Plotly charts in streamlit
#pip install plotly
import plotly.graph_objects as go

st.title("Welcome to Streamlit! Plotly Graphs")

fig = go.Figure(
    data=[go.Pie(
        labels=['A', 'B', 'C'],
        values=[30, 20, 50]
    )]
)
fig = fig.update_traces(
    hoverinfo='label+percent',
    textinfo='value',
    textfont_size=15
)
st.write("Pie chart in Streamlit")
st.plotly_chart(fig)
