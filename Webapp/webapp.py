import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from binance.client import Client
import datetime as dt
from datetime import datetime, timedelta
from tqdm import tqdm as tqdm


st.title("Karimunjawa")

st.subheader("subheader")
st.header("This is a header")

st.write("This is text")

{
    "key":"value",
    "key2":"value2"
}

st.sidebar.title("Write this to the sidebar")

st.image("https://github.com/juanluishg/dataproject1/blob/main/WhatsApp%20Image%202020-12-11%20at%2022.35.04.jpeg?raw=true")

option = st.sidebar.selectbox("Wich Dashboard?",('twitter','chart', 'Binance','Manual'))
st.header(option)

if option == 'twitter':
    st.subheader('this is the chart dashboard')

    num_days = st.sidebar.slider('Number of days',1,30,10)

    num_days

if option == 'Manual':
    excel_file = 'bolsa.xlsx'
    sheet_name ='Sheet1'
    df = pd.read_excel(excel_file,
                        sheet_name=sheet_name,
                        header=0)

    st.dataframe(df)

    num_days = st.slider('Number of days',1,472,300)
    alto = st.slider('Alto',600,2000,600)

    df = df[num_days:]
    fig = go.Figure(data=[go.Candlestick(x=df['index'],
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'])])
    
    fig.update_xaxes(type='category')
    fig.update_layout(height=alto)

    st.plotly_chart(fig,use_container_width =True)

