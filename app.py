import requests
import streamlit as st

st.set_page_config(page_title="Chess.com Profile",page_icon="♟",
                    layout="centered",
                    initial_sidebar_state="collapsed")
st.header("Chess.com Insights ♟")

profile = st.text_input("Enter your chess.com username: ")

API_URL= "https://api.chess.com/pub/player/"+profile

STATS_URL = "https://api.chess.com/pub/player/"+profile+"/stats"

submit = st.button('Get Profile')

if submit:
    response = requests.get(API_URL, headers={"User-Agent": "karmadebjit@gmail.com"})
    stats = requests.get(STATS_URL, headers={"User-Agent": "karmadebjit@gmail.com"})
    resp_dict = response.json()
    stats_dict = stats.json()
    if resp_dict.get('name') is None:
        st.subheader("Player's Profile")
    else:
        st.subheader("Profile for "+resp_dict['username'])
    col1,col2,col3,col4,col5,col6 = st.columns([7,10,10,7,7,7])
    print(stats_dict)
    #st.write(stats_dict)
    with col1:
        st.write("Avatar")
        if resp_dict.get('avatar') is None:
            st.write("N/A")
        else:
            st.image(resp_dict.get('avatar'),width=70)
    with col2:
        st.write("Name")
        if resp_dict.get('name') is None:
            st.write("N/A")
        else:
            st.write(resp_dict['name'])
    with col3:
        st.write("User ID")
        st.write(resp_dict['username'])
    with col4:
        st.write("Friends")
        st.write(resp_dict['followers'])
    with col5:
        st.write("Blitz Rating")
        if 'chess_blitz' in stats_dict and stats_dict['chess_blitz'] is not None and stats_dict['chess_blitz']['best'] is not None:
            st.write(stats_dict['chess_blitz']['best']['rating'])
        elif 'chess_blitz' in stats_dict and stats_dict['chess_blitz'] is not None and stats_dict['chess_blitz']['last'] is not None:
            st.write(stats_dict['chess_blitz']['last']['rating'])
        else:
            st.write("N/A")
    with col6:
        st.write("Rapid Rating")
        if 'chess_rapid' in stats_dict and stats_dict['chess_rapid'] is not None and stats_dict['chess_rapid']['best'] is not None:
            st.write(stats_dict['chess_rapid']['best']['rating'])
        elif 'chess_rapid' in stats_dict and stats_dict['chess_rapid'] is not None and stats_dict['chess_rapid']['last'] is not None:
            st.write(stats_dict['chess_rapid']['last']['rating'])
        else:
            st.write("N/A")



