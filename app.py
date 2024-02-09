import requests
import streamlit as st

st.set_page_config(page_title="Chess.com Profile",page_icon="♟",
                    layout="centered",
                    initial_sidebar_state="collapsed")
st.header("Chess.com Insights ♟")

profile = st.text_input("Enter your chess.com username: ")

API_URL= "https://api.chess.com/pub/player/"+profile

submit = st.button('Get Profile')

if submit:
    response = requests.get(API_URL, headers={"User-Agent": "karmadebjit@gmail.com"})
    resp_dict = response.json()
    col1,col2,col3,col4 = st.columns([4,4,4,4])
    #print(resp_dict)
    #st.write(resp_dict)
    with col1:
        st.write("Avatar")
        st.image(resp_dict['avatar'],width=70)
    with col2:
        st.write("Name")
        st.write(resp_dict['name'])
    with col3:
        st.write("User ID")
        st.write(resp_dict['username'])
    with col4:
        st.write("Friends")
        st.write(resp_dict['followers'])
