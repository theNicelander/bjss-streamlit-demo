# streamlit run streamlit_app.py

import streamlit as st
import pandas as pd
import time
import plotly.express as px

# top left corner of app
img_url = "https://webapp-tt-prod.azurewebsites.net/static/images/bjss.png"
st.sidebar.image(img_url)

st.sidebar.title("Hello BJSS")
st.sidebar.write("Lets recreate the BJSS London Table Tennis app")

page = st.sidebar.selectbox("Page", options=["Home", "Leaderboard", "Submit"])

def submit_page():
    st.subheader("SUBMIT YOUR RESULTS")
    st.text(
        "names should be alphanumeric and not matching, \n"
        + "no spaces or characters that aren't [a-z]/[0-9]"
    )
    col1, col2 = st.columns(2)
    winner = col1.text_input("Winner Name:", value="Petur", help="Give us the winner")
    loser = col2.text_input("Loser Name:", value="Steve")
    score = st.text_input("Score")

    if st.button("Submit"):
        if all((winner, loser, score)):
            col1, col2 = st.columns(2)
            col1.metric(winner, 1500 + 20, 20)
            col2.metric(loser, 1500 - 20, -20)
        else:
            st.write("Fill in all the things plz")


@st.cache(show_spinner=False, persist=True)
def get_leaderboard():
    with st.spinner("Scraping leaderboard..."):
        time.sleep(3)
        url = "https://webapp-tt-prod.azurewebsites.net/leaderboard"
        return pd.read_html(url)[0]


if page == "Submit":
    submit_page()


if page == "Home":
    st.title("Welcome!")
    st.video("https://www.youtube.com/watch?v=9Fv5cuYZFC0")

if page == "Leaderboard":
    top = st.slider("Top what?", 0, 20, value=5)

    df = get_leaderboard()
    st.table(df.head(top))

    fig = px.bar(df, x='User', y='MMR')
    st.plotly_chart(fig)
