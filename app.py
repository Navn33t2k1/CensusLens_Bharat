import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('india2011census.csv')

list_of_states = list(df['State name'].unique())
list_of_states.insert(0, 'Overall India')

st.sidebar.title("CensusLens Bharat")
selected_state = st.sidebar.selectbox("Select a state".upper(), list_of_states)
primary = st.sidebar.selectbox('select Primary parameter'.upper(), list(df.columns[5:]), index=0)
secondary = st.sidebar.selectbox('select secondary parameter'.upper(), list(df.columns[5:]), index=1)

plot = st.sidebar.button('Plot Graph')

st.sidebar.markdown("<br><br><br><br><br><br><br><hr>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center;'>Created by <b>Navneet</b></p>", unsafe_allow_html=True)

if plot:
    st.text('Size represent primary parameter'.upper())
    st.text('Color represent secondary parameter'.upper())
    if selected_state=='Overall India':
        # plot for india
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude",
                                size=primary, color=secondary, zoom=3.5, size_max=30,
                                color_continuous_scale=px.colors.sequential.Plasma,
                                mapbox_style='carto-positron', width=1200, height=700,
                                hover_name='District name')
        st.plotly_chart(fig, use_container_width=True)
    else:
        # plot for state
        state_df = df[df['State name']==selected_state]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude",
                                size=primary, color=secondary, zoom=5, size_max=30,
                                color_continuous_scale=px.colors.sequential.Plasma,
                                mapbox_style='carto-positron', width=1200, height=700,
                                hover_name='District name')
        st.plotly_chart(fig, use_container_width=True)