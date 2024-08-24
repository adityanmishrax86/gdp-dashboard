import streamlit as st
import pymongo
import pandas as pd
import plotly.express as px

# Connect to MongoDB
@st.cache_resource
def init_connection():
    return pymongo.MongoClient("mongodb+srv://azax1234:azax1234@cluster0.h8w1bp1.mongodb.net?retryWrites=true&w=majority&appName=Cluster0")

client = init_connection()

# Select the database and collection
db = client["prod1"]
collection = db["expenses"]

# Fetch data from MongoDB
@st.cache_data
def get_data():
    items = collection.find()
    items = list(items)  # Convert cursor to list
    return pd.DataFrame(items)

df = get_data()

# Streamlit app
st.title("MongoDB Dashboard")

# Display raw data
st.subheader("Raw Data")
st.write(df)

# Create a bar chart
st.subheader("Bar Chart")
column_to_plot = st.selectbox("Select a column for the bar chart", df.columns)
fig = px.bar(df, x=df.index, y=column_to_plot)
st.plotly_chart(fig)

# Create a line chart
st.subheader("Line Chart")
column_to_plot = st.selectbox("Select a column for the line chart", df.columns)
fig = px.line(df, x=df.index, y=column_to_plot)
st.plotly_chart(fig)

# Create a scatter plot
st.subheader("Scatter Plot")
x_axis = st.selectbox("Select X-axis", df.columns)
y_axis = st.selectbox("Select Y-axis", df.columns)
fig = px.scatter(df, x=x_axis, y=y_axis)
st.plotly_chart(fig)