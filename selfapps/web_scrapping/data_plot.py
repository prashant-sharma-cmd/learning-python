import streamlit as st
import plotly.express as px
import sqlite3

connection = sqlite3.connect("weather.db")
cursor = connection.cursor()

def data_extract():
    cursor.execute("SELECT * FROM temperature")
    rows = cursor.fetchall()
    time = [item[0] for item in rows]
    temp = [item[1] for item in rows]
    dataset = {"time": time, "temp": temp}
    return dataset

date = data_extract()["time"]
temperature = data_extract()["temp"]
chart = px.line(x=date,y=temperature, title="Changes in World Temperature with time",
                labels={"x": f"Date", "y": f"Temperature"})
st.plotly_chart(chart)
