import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time


url = 'https://webapp-tt-prod.azurewebsites.net/static/images/bjss.png'
st.sidebar.image(url, width=200)
page = st.sidebar.selectbox("Page", options=["Home", "Leaderboard", "Submit"])


@st.cache(show_spinner=False)
def get_data():
    with st.spinner("Getting data from DB"):
        time.sleep(3)
        return pd.read_html("https://webapp-tt-prod.azurewebsites.net/leaderboard")[0]

# home page
if page =='Home':
    st.title("Welcome!")
    st.video("https://www.youtube.com/watch?v=9Fv5cuYZFC0")

if page =='Leaderboard':
    df = get_data()
    min_number = st.slider("Min number", min_value=1000, max_value=1600)

    st.table(df[df['MMR'] >= int(min_number)])

    fig = px.bar(df, x='User', y='MMR')
    st.plotly_chart(fig)

