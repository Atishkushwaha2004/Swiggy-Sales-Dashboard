import streamlit as st
import os
import pandas as pd

st.title("Swiggy Sales Dashboard")

st.write("Files in current directory:")
st.write(os.listdir())

df = pd.read_excel("Swiggy Raw Data Excel.xlsx")

st.dataframe(df)
