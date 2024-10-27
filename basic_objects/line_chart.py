# This is syntax-sugar around st.altair_chart.
# The main difference is this command uses the data's own column and indices to figure out the chart's spec.
# As a result this is easier to use for many "just plot this" scenarios, while being less customizable.

import streamlit as st
import pandas as pd
import numpy as np

st.header("Line chart")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)
