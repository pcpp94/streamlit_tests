# st.selectbox allows the display of a select widget.

import streamlit as st

st.header("st.selectbox")

option = st.selectbox("What is your favorite color?", ("Blue", "Red", "Green"))

st.write("Your favorite color is ", option)
