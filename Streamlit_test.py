import streamlit as st

import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
st.title("Streamlit")
st.header("Special Treatment")

agree = st.checkbox("I agree")

if agree:
    st.write("Nice to meet you! Aman!")

import streamlit as st

genre = st.radio(
    "What's your favorite movie genre",
    ["Comedy", "Drama", "Documentary", "Thriller"],
    captions=[
        "Kapil sharma show.",
        "Saumya mall.",
        "Keep learning.",
        "Extra"
    ],
)

if genre == "Comedy":
    st.write("You selected comedy.")
elif genre == "Drama":
    st.write("You like drama.")
elif genre == "Documentary":
    st.write("You loved documentary.")