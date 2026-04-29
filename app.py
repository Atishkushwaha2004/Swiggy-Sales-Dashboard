import streamlit as st
import pandas as pd

st.title("Swiggy Sales Dashboard")

df = pd.read_excel("data.xlsx")

st.dataframe(df)
st.bar_chart(df)
