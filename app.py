import streamlit as st
import pandas as pd
import os
import plotly.express as px

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="Swiggy Sales Dashboard", layout="wide")

st.title("🍔 Swiggy Sales Dashboard")

# -------------------------------
# Load Data (Safe way)
# -------------------------------
file_path = os.path.join(os.path.dirname(__file__), "data.xlsx")

try:
    df = pd.read_excel(file_path, engine="openpyxl")
except Exception as e:
    st.error(f"Error loading file: {e}")
    st.stop()

# -------------------------------
# Show Raw Data
# -------------------------------
st.subheader("📄 Raw Data")
st.dataframe(df)

# -------------------------------
# Basic Info
# -------------------------------
st.subheader("📊 Dataset Info")
st.write("Rows:", df.shape[0])
st.write("Columns:", df.shape[1])

# -------------------------------
# Example Columns (change if needed)
# -------------------------------
# Assume columns: City, Category, Price

if "City" in df.columns and "Price" in df.columns:

    # -------------------------------
    # Total Sales
    # -------------------------------
    total_sales = df["Price"].sum()
    st.metric("💰 Total Sales", f"₹ {total_sales:,.2f}")

    # -------------------------------
    # Sales by City
    # -------------------------------
    st.subheader("🏙️ Sales by City")

    city_sales = df.groupby("City")["Price"].sum().reset_index()

    fig = px.bar(city_sales, x="City", y="Price", title="City-wise Sales")
    st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# Category Analysis
# -------------------------------
if "Category" in df.columns and "Price" in df.columns:

    st.subheader("🍕 Category-wise Sales")

    cat_sales = df.groupby("Category")["Price"].sum().reset_index()

    fig2 = px.pie(cat_sales, names="Category", values="Price", title="Category Distribution")
    st.plotly_chart(fig2, use_container_width=True)

# -------------------------------
# Sidebar Filter
# -------------------------------
st.sidebar.header("🔍 Filters")

if "City" in df.columns:
    city_filter = st.sidebar.selectbox("Select City", ["All"] + list(df["City"].unique()))

    if city_filter != "All":
        df = df[df["City"] == city_filter]
        st.write(f"Filtered Data for {city_filter}")
        st.dataframe(df)

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.write("Made with ❤️ using Streamlit")
