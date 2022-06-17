import streamlit as st
import pyttsx3
import requests
from bs4 import BeautifulSoup
import comtypes.client

url = st.text_input('paste a url')
rate_adjustment = st.slider('Speech Rate Adjustment',-50,50)


def content(url):
    session = requests.Session()
    res = session.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    #st.write(res)
    soup = BeautifulSoup(res.text,'html.parser')
    text = soup.find_all("p", text=True)
    text = [t.getText().strip() for t in text]
    output = " ".join(text)
    return output

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

def save_file(audio):
    engine.save_to_file(audio, 'test.mp3')
    engine.runAndWait()


if url:
    #print(url)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate + rate_adjustment)

    contents = content(url)
    #print(contents)

    save_file(contents)
    audio_file = open('test.mp3', 'rb')
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format='audio/mp3')
    #engine.say(contents)
    #engine.runAndWait()


