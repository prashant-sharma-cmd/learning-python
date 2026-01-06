import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

st.header("The Best Company")
content = """
WanderLoop Innovations is a quirky tech startup reimagining how people explore the 
world around them. Founded by three college friends with a shared love for wandering
off the beaten path, the company designs smart travel gear that syncs with a companion
app to create personalized micro-adventures. Their flagship product, the “WanderTag,”
suggests spontaneous destinations based on your mood, location, and playlist.
From hidden alley cafés to forest trails barely marked on the map, WanderLoop helps
you rediscover curiosity, one detour at a time. They're fueled by recycled coffee 
grounds, collective wanderlust, and a stubborn refusal to take the straight road. 
"""
st.write(content)

st.subheader("Our Team")

col1, empty_col1, col2, empty_col2, col3 = st.columns([3, 0.5, 3, 0.5, 3])

df = pd.read_csv("data.csv",sep=",")

with (col1):
    for index, row in df[:4].iterrows():
        name = row["first name"].capitalize() + " " + row["last name"].capitalize()
        st.subheader(name)
        st.write(row["role"])
        st.image("images/"+row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        name = row["first name"].capitalize() + " " + row["last name"].capitalize()
        st.subheader(name)
        st.write(row["role"])
        st.image("images/"+row["image"])

with col3:
    for index, row in df[8:].iterrows():
        name = row["first name"].capitalize() + " " + row["last name"].capitalize()
        st.subheader(name)
        st.write(row["role"])
        st.image("images/"+row["image"])