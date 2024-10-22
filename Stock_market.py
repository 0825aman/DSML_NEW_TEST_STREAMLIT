import pandas as pd
import streamlit as st
import yfinance as yf
import datetime

# Title for the app
st.title("Stock Market Analysis")

# Input for the stock ticker
company = st.text_input("Which stock do you want?", "AAPL")

# Input for start and end dates
col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Start date", datetime.date(2020, 1, 1))

with col2:
    end_date = st.date_input("End date", datetime.date(2024, 9, 30))

# Ensure end date is after start date
if end_date < start_date:
    st.error("End date must be after start date.")
else:
    # Fetch historical market data
    data = yf.Ticker(company)
    hist = data.history(start=start_date, end=end_date)

    # Display the raw data
    st.subheader("Raw Data")
    st.dataframe(hist)

    # Plotting the data
    st.subheader("Open Price Chart")
    st.line_chart(hist['Open'])

    st.subheader("Close Price Chart")
    st.bar_chart(hist['Close'])
