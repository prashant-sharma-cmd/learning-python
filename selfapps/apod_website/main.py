import streamlit as st
import requests
from datetime import date

# Storing parameters for API
api_key = "YRALdZLpdrHowAKJlaMn2d4niQ4ovcpGhmMQXSac"
today = date.strftime(date.today(), '%Y-%m-%d')

# Loading the API url
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={today}"

# Loading the API and storing
request = requests.get(url)
content = request.json()

# Creating a web page
st.set_page_config(layout="wide")

# Writing content in the web page
st.title(content["title"])
st.image(content["url"])
st.text(content["explanation"])
