import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('vehicles_us.csv')

# Cleaning the data
df['model_year'] = df['model_year'].fillna(df['model_year'].median())
df['cylinders'] = df['cylinders'].fillna(df['cylinders'].mode()[0])
df['odometer'] = df['odometer'].fillna(df['odometer'].median())
df['paint_color'] = df['paint_color'].fillna(df['paint_color'].mode()[0])
df['is_4wd'] = df['is_4wd'].fillna(0)


# Streamlit app
st.title("Car Sales Dashboard")

# Header
st.header("Analysis of Car Sales Data")

# Histogram for Price Distribution
fig_price = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig_price)

# Scatter Plot for Price vs. Odometer
fig_scatter = px.scatter(df, x='odometer', y='price', title='Price vs. Odometer')
st.plotly_chart(fig_scatter)

# Scatter Plot for Price vs. Model Year
if st.checkbox('Show Price vs. Model Year'):
    fig_scatter_year = px.scatter(df, x='model_year', y='price', title='Price vs. Model Year')
    st.plotly_chart(fig_scatter_year)


