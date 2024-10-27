# st.secrets allows you to store confidential information such as API keys, database passwords or other credentials.

import streamlit as st

st.title("st.secrets")

st.write(st.secrets["message"])
