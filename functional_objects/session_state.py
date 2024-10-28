# We define access to a Streamlit app in a browser tab as a session.
# For each browser tab that connects to the Streamlit server, a new session is created.
# Streamlit reruns your script from top to bottom every time you interact with your app.
# Each reruns takes place in a blank slate: no variables are shared between runs.

# Session State is a way to share variables between reruns, for each user session.
# In addition to the ability to store and persist state, Streamlit also exposes the ability to manipulate state using Callbacks.

# In this tutorial, we will illustrate the usage of Session State and Callbacks as we build a weight conversion app.
# st.session_state allows the implementation of session state in a Streamlit app.

import streamlit as st

st.title("st.session_state")


def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs / 2.2046


def kg_to_lbs():
    st.session_state.lbs = st.session_state.kg * 2.2046


st.header("Input")
col1, spacer, col2 = st.columns([2, 1, 2])
with col1:
    pounds = st.number_input("Pounds:", key="lbs", on_change=lbs_to_kg)
with col2:
    kilogram = st.number_input("Kilograms:", key="kg", on_change=kg_to_lbs)

st.header("Output")
st.write("st.session_state object:", st.session_state)
