import requests
import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from chess_openings import *
from datetime import datetime

st.set_page_config(page_title="Chess.com Insights",page_icon="♟",
                    layout="centered",
                    initial_sidebar_state="collapsed")
st.header("Chess.com Insights ♟")

profile = st.text_input("Enter your chess.com username: ")

curr_month = str(datetime.now().month)
curr_year = str(datetime.now().year)
if len(curr_month)<2:
    curr_month = "0"+curr_month

API_URL= "https://api.chess.com/pub/player/"+profile

STATS_URL = "https://api.chess.com/pub/player/"+profile+"/stats"

ARCHIVE_URL = "https://api.chess.com/pub/player/"+profile+"/games/"+curr_year+"/"+curr_month

submit = st.button('Get Profile')

if submit:
    response = requests.get(API_URL, headers={"User-Agent": "karmadebjit@gmail.com"})
    stats = requests.get(STATS_URL, headers={"User-Agent": "karmadebjit@gmail.com"})
    archive = requests.get(ARCHIVE_URL, headers={"User-Agent": "karmadebjit@gmail.com"})
    
    resp_dict = response.json()
    stats_dict = stats.json()
    games_dict = archive.json()      

    print(len(games_dict.get('games')))

    if resp_dict.get('name') is None:
        st.subheader(profile+"'s Profile")
    else:
        st.subheader("Profile for "+resp_dict['name'])     
    
    col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([10,12,16,10,7,7,12,7])
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
        if 'chess_blitz' in stats_dict:
            if stats_dict.get('chess_blitz') is not None and stats_dict.get('chess_blitz').get('best') is not None:
                st.write(stats_dict.get('chess_blitz').get('best').get('rating'))
            elif stats_dict.get('chess_blitz') is not None and stats_dict.get('chess_blitz').get('last') is not None:
                st.write(stats_dict.get('chess_blitz').get('last').get('rating'))
        else:
            st.write("N/A")
    with col6:
        st.write("Rapid Rating")
        if 'chess_rapid' in stats_dict:
            if stats_dict.get('chess_rapid') is not None and stats_dict.get('chess_rapid').get('best') is not None:
                st.write(stats_dict.get('chess_rapid').get('best').get('rating'))
            elif stats_dict.get('chess_rapid') is not None and stats_dict.get('chess_rapid').get('last') is not None:
                st.write(stats_dict.get('chess_rapid').get('last').get('rating'))
        else:
            st.write("N/A")
    with col7:
        if 'league' in resp_dict:
            st.write("League")
            st.write(resp_dict.get('league'))
    with col8:
        if 'title' in resp_dict:
            st.write("Title")
            st.write(resp_dict.get('title'))
    
    
    if 'chess_blitz' in stats_dict:
        st.subheader("Blitz Wins & Losses")
        #print(stats_dict.get('chess_blitz').get('record'))
        if stats_dict.get('chess_blitz') is not None and stats_dict.get('chess_blitz').get('record') is not None:
            
            labels = ['win', 'loss', 'draw']
            games = []
            games.append(stats_dict.get('chess_blitz').get('record').get('win'))
            games.append(stats_dict.get('chess_blitz').get('record').get('loss'))
            games.append(stats_dict.get('chess_blitz').get('record').get('draw'))

            fig = go.Figure(
                        go.Pie(
                            labels = labels,
                            values = games,
                            hoverinfo = "label+percent",
                            textinfo = "value"
                ))
            st.plotly_chart(fig)

        else:
            st.write("N/A")
    
    if 'chess_rapid' in stats_dict:
        st.subheader("Rapid Wins & Losses")
        #print(stats_dict.get('chess_rapid').get('record'))
        if stats_dict.get('chess_rapid') is not None and stats_dict.get('chess_rapid').get('record') is not None:
           
            labels = ['win', 'loss', 'draw']
            games = []
            games.append(stats_dict.get('chess_rapid').get('record').get('win'))
            games.append(stats_dict.get('chess_rapid').get('record').get('loss'))
            games.append(stats_dict.get('chess_rapid').get('record').get('draw'))

            fig = go.Figure(
                        go.Pie(
                            labels = labels,
                            values = games,
                            hoverinfo = "label+percent",
                            textinfo = "value"
                    ))
            st.plotly_chart(fig)

        else:
            st.write("N/A")

    st.subheader("Games Played this month")
    st.write("Total: "+str(len(games_dict.get('games'))))
    
    list_of_openings=[]
    time_controls=[]

    for game in games_dict.get('games'):
        time_controls.append(game.get('time_control'))
    unique_time_controls = set(time_controls)
    for control in unique_time_controls:
        if str(control).find('+')==-1 and str(control).find('/')==-1:
            st.write(str(int(int(control)/60))+" min: "+str(time_controls.count(control)))
        elif str(control).find('/')!=-1 and str(control).find('+')==-1:
            extra_time_games = control[control.find('/')+1:]
            days = int(int(extra_time_games)/86400)
            st.write(str(days)+" day(s): "+str(time_controls.count(control)))
        elif str(control).find('+')!=-1:
            extra_time_games = control[:control.find('+')]
            mins_part = int(int(extra_time_games)/60)
            sec_part = control[control.find('+')+1:]
            st.write(str(mins_part)+" min"+"+"+str(sec_part)+" s: "+str(time_controls.count(control)))
    st.subheader("Most Played Opening of the Month")
    st.write(get_openings(list_of_openings,games_dict))
    

    