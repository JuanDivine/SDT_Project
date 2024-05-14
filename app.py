import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

# App title
st.title("Car Sales Dashboard")

# Header
st.header("Car Sales Analysis")

# Histogram of Prices
fig_hist = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig_hist)

# Scatter Plot of Price vs. Odometer
fig_scatter = px.scatter(df, x='price', y='odometer', title='Price vs Odometer')
st.plotly_chart(fig_scatter)

# Checkbox to show/hide data
if st.checkbox('Show Data'):
    st.write(df.head())
