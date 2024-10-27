# st.write

# allows writing text and arguments to the Streamlit app.

# In addition to being able to display text, the following can also be displayed via the st.write() command:
# > Prints strings; works like st.markdown()
# > Displays a Python dict
# > Displays pandas DataFrame can be displayed as a table
# > Plots/graphs/figures from matplotlib, plotly, altair, graphviz, bokeh
# > And more (see st.write on API docs)

import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header("st.write")

# Example 1

st.write("Hello, *World!* :sunglasses:")

# Example 1.5

st.write({"test": 1234, "test2": "mhhm"})

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
st.write(df)

# Example 4

st.write("Below is a DataFrame:", df, "Above is a dataframe.")

# Example 5

df2 = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
c = (
    alt.Chart(df2)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)
st.write(c)
