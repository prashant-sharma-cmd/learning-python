import streamlit as st
from send_email import send_email
import pandas as pd

df = pd.read_csv('topics.csv')

with st.form(key='form'):
    email = st.text_input('Your Email Address')
    topic = st.selectbox("What topic do you want to discuss?", df['topic'])
    text = st.text_area('Text')
    message = f"""\
Subject: New email from {email}

From: {email}
Topic: {topic}
{text}
"""
    button = st.form_submit_button('Submit')
    if button:
        send_email(message)
        st.info('Email sent successfully!!')

