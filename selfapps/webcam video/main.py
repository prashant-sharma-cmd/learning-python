import cv2
import streamlit as st
import time

st.title("Motion Detector")
start = st.button("Start Camera")

if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        week_day = time.strftime("%A")
        current_time = time.strftime("%H:%M:%S")

        cv2.putText(img=frame, text=week_day, org=(30, 80),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3,
                    color=(255, 255, 255), thickness=1, lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text=current_time, org=(30,140),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3,
                    color=(255, 0, 0), thickness=1, lineType=cv2.LINE_AA)

        streamlit_image.image(frame)

