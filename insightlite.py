import streamlit as st
import pandas as pd
import plotly.express as px
st.title("InsightLite Dashboard")
#upload data
upload_file = st.file_uploader("Upload your data in csv or excel file format", type="csv")
if upload_file:
    df = pd.read_csv(upload_file)
    st.write("Preview of your data", df.head())

    #visual
    chart = px.bar(df, x="Date", y="Value", color="Category")
    st.plotly_chart(chart)

    # Smart Summary
    st.subheader("Auto Summary")
    st.write(f"Most common service: {df['Service Type'].mode()[0]}")

