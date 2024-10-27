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

st.header("Other writing methods")

st.markdown("markdown")
st.header("header")
st.subheader("subheader")
st.caption("caption")
st.text("text")
st.latex("latex")
st.code("import pandas as pd", language="python")
