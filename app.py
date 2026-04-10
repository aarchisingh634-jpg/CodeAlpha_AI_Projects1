import streamlit as st
from googletrans import Translator

translator = Translator()

st.title("Language Translation Tool")

text = st.text_area("Enter text")

if st.button("Translate"):
    translated = translator.translate(text, dest='hi')
    st.success(translated.text)
