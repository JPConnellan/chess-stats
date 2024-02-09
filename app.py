import requests
import streamlit as st

st.set_page_config(page_title="Chess.com Profile",page_icon="♟",
                    layout="centered",
                    initial_sidebar_state="collapsed")
st.header("Chess Insights ♟")

profile = st.text_input("Enter your chess.com username: ")

API_URL= "https://api.chess.com/pub/player/"+profile

submit = st.button('Get Profile')

if submit:
    response = requests.get(API_URL, headers={"User-Agent": "karmadebjit@gmail.com"})
    resp_dict = response.json()
    #print(resp_dict)
    #st.write(resp_dict)
    st.image(resp_dict['avatar'])
    st.write(resp_dict['name'])
    st.write(resp_dict['username'])
    st.write(resp_dict['followers'])
