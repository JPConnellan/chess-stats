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
        st.subheader(profile+"'s Profile")
    else:
        st.subheader("Profile for "+resp_dict['name'])
    col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([10,12,12,7,7,7,12,7])
    print(resp_dict)
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
        st.write("Blitz")
        if 'chess_blitz' in stats_dict:
            if stats_dict.get('chess_blitz') is not None and stats_dict.get('chess_blitz').get('best') is not None:
                st.write("Rating:",stats_dict.get('chess_blitz').get('best').get('rating'))
                st.write("Wins:",stats_dict.get('chess_blitz').get('record').get('win'))
                st.write("Losses:",stats_dict.get('chess_blitz').get('record').get('loss'))
            elif stats_dict.get('chess_blitz') is not None and stats_dict.get('chess_blitz').get('last') is not None:
                st.write("Rating:",stats_dict.get('chess_blitz').get('last').get('rating'))
                st.write("Wins:",stats_dict.get('chess_blitz').get('record').get('win'))
                st.write("Losses:",stats_dict.get('chess_blitz').get('record').get('loss'))
        else:
            st.write("N/A")
    with col6:
        st.write("Rapid")
        if 'chess_rapid' in stats_dict:
            if stats_dict.get('chess_rapid') is not None and stats_dict.get('chess_rapid').get('best') is not None:
                st.write("Rating:",stats_dict.get('chess_rapid').get('best').get('rating'))
                st.write("Wins:",stats_dict.get('chess_rapid').get('record').get('win'))
                st.write("Losses:",stats_dict.get('chess_rapid').get('record').get('loss'))
            elif stats_dict.get('chess_rapid') is not None and stats_dict.get('chess_rapid').get('last') is not None:
                st.write("Rating:",stats_dict.get('chess_rapid').get('last').get('rating'))
                st.write("Wins:",stats_dict.get('chess_rapid').get('record').get('win'))
                st.write("Losses:",stats_dict.get('chess_rapid').get('record').get('loss'))
        else:
            st.write("N/A")
    with col7:
        st.write("League")
        if 'league' in resp_dict:
            st.write(resp_dict.get('league'))
        else:
            st.write("N/A")
    with col8:
        if 'title' in resp_dict:
            st.write("Title")
            st.write(resp_dict.get('title'))


