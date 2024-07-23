import streamlit as st
import pandas as pd
import numpy as np

# Sample stock data
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=100)
data = {
    'Date': dates,
    'Stock': np.random.choice(['AAPL', 'GOOG', 'MSFT', 'AMZN'], size=100),
    'Close': np.random.uniform(100, 500, size=100),
    'Volume': np.random.randint(1000, 5000, size=100)
}
df = pd.DataFrame(data)

# Sidebar for filtering
st.sidebar.title("Filters")

# Multiselect box for selecting stocks
selected_stocks = st.sidebar.multiselect('Select Stocks', options=df['Stock'].unique(), default=df['Stock'].unique())

# Slider for selecting price range
min_price, max_price = st.sidebar.slider('Select Price Range', float(df['Close'].min()), float(df['Close'].max()), (float(df['Close'].min()), float(df['Close'].max())))

# Slider for selecting volume range
min_volume, max_volume = st.sidebar.slider('Select Volume Range', int(df['Volume'].min()), int(df['Volume'].max()), (int(df['Volume'].min()), int(df['Volume'].max())))

# Filter the dataframe based on user input
filtered_df = df[
    (df['Stock'].isin(selected_stocks)) &
    (df['Close'] >= min_price) &
    (df['Close'] <= max_price) &
    (df['Volume'] >= min_volume) &
    (df['Volume'] <= max_volume)
]

# Display the dataframe
st.title("Stock Data")
st.dataframe(filtered_df)
