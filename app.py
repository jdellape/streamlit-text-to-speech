import streamlit as st
import requests
from bs4 import BeautifulSoup
from gtts import gTTS

url = st.text_input('paste a url')

def get_article_text(url):
    session = requests.Session()
    res = session.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(res.text,'html.parser')
    text = soup.find_all("p")
    text_with_tags = [t.get_text() for t in text]
    text = [t.get_text().strip() for t in text]
    text_only = " ".join(text)
    return (text_only, text_with_tags)


if url:
    text_without_tags, text_with_tags = get_article_text(url)
    aud_file = gTTS(text=text_without_tags, lang='en', slow=False)
    aud_file.save("article.mp3")
    audio_file_read = open('article.mp3', 'rb')
    audio_bytes = audio_file_read.read()
    st.audio(audio_bytes, format='audio/mp3')
    st.write(text_with_tags)


