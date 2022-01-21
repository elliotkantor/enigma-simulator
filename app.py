import streamlit as st
from main import encode

st.title("Enigma Simulator")
st.write("Based on the code from www.101computing.net/enigma-encoder/")

raw_text = st.text_input(label="Enter your text to encode/decode here")
if raw_text:
    st.write(encode(raw_text))
