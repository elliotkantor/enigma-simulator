import streamlit as st
from main import encode, alphabet
from settings import *

st.title("Enigma Simulator")
st.write("Based on the code from www.101computing.net/enigma-encoder/")

plugboard_original = plugboard

with st.expander("Basic settings"):
    rotors = st.multiselect(
        "Select the 3 rotors to use (order matters)",
        options=("I", "II", "III", "IV", "V"),
        default=("I", "II", "III"),
    )
    reflector = st.radio("Select reflector", options=("UKW-B", "UKW-C"))
    ringSettings = st.multiselect(
        "Set 3 ring settings (in order)",
        options=[a for a in alphabet],
        default=("A", "B", "C"),
    )
    ringPositions = st.multiselect(
        "Set 3 ring positions (in order)",
        options=[a for a in alphabet],
        default=("D", "E", "F"),
    )

    plugboard = st.text_input(
        "Enter plugboard pairs (do not repeat letters)", value=plugboard_original
    )

    accept_noncharacter = (
        st.radio("Output non-alphabetical characters?", ["Yes", "No"]) == "Yes"
    )


valid_settings = len(rotors) >= 3 and len(ringSettings) >= 3 and len(ringPositions) >= 3

raw_text = st.text_input(label="Enter your text to encode/decode here")
if not valid_settings:
    st.error(
        "Some of your settings are invalid. Check that you have the correct number of inputs for each of them."
    )
if raw_text and valid_settings:
    out_text = encode(
        raw_text,
        rotors,
        reflector,
        ringSettings,
        ringPositions,
        plugboard,
    )
    if not accept_noncharacter:
        out_text = "".join([char for char in out_text if char in alphabet])
    st.success(out_text)
