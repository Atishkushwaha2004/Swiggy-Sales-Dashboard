import streamlit as st
import pandas as pd
import os

st.title("Swiggy Sales Dashboard")

# DEBUG: show files and current path
st.write("Current working directory:")
st.write(os.getcwd())

st.write("Files available here:")
st.write(os.listdir())

# Try loading file
df = pd.read_excel("Swiggy Raw Data Excel.xlsx")

st.dataframe(df)
