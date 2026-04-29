# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_excel("swiggy Raw Data Excel.xlsx")

# st.title("Swiggy Sales Dashboard")

# city = st.selectbox("Select city", df['city'].unique())
# filtered = df[df['city'] == city]

# st.write(filtered)

# plt.figure()
# filtered.groupby('Restaurant')['Sales'].sum().plot(kind='bar')
# st.pyplot(plt)


# import pandas as pd

# df = pd.read_excel("swiggy Raw Data Excel.xlsx")

# df.columns = df.columns.str.strip().str.lower()

# print(df.head())


import streamlit as st
import pandas as pd

st.title("Swiggy Sales Dashboard")

# Excel file load
df = pd.read_excel("Swiggy Raw Data Excel.xlsx")

# Show data
st.dataframe(df)

# Simple chart
st.bar_chart(df)

