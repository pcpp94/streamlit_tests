# st.cache allows you to optimize the performance of your Streamlit app.

# Streamlit provides a caching mechanism that allows your app to stay performant even when loading data from the web,
# manipulating large datasets, or performing expensive computations. This is done with the @st.cache decorator.

# When you mark a function with the @st.cache decorator,
# it tells Streamlit that whenever the function is called it needs to check a few things:
# The input parameters that you called the function with
# The value of any external variable used in the function
# The body of the function
# The body of any function used inside the cached function

# If this is the first time Streamlit has seen these four components with these exact values and in this exact combination and order,
# it runs the function and stores the result in a local cache. Then, next time the cached function is called, if none of these components changed, Streamlit will just skip executing the function altogether and, instead, return the output previously stored in the cache.

# The way Streamlit keeps track of changes in these components is through hashing. Think of the cache as an in-memory key-value store, where the key is a hash of all of the above and the value is the actual output object passed by reference.

# Finally, @st.cache supports arguments to configure the cache's behavior. You can find more information on those in our API reference.

# How to use?
# You can simply add st.cache decorator on the preceding line of a custom function that you define in your Streamlit app. See the example below.

import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title("st.cache")

# Using cache
a0 = time()
st.subheader("Using st.cache")


@st.cache(suppress_st_warning=True)
def load_data_a():
    df = pd.DataFrame(np.random.rand(2000000, 5), columns=["a", "b", "c", "d", "e"])
    return df


st.write(load_data_a())
a1 = time()
st.info(a1 - a0)


# Not using cache
b0 = time()
st.subheader("Not using st.cache")


def load_data_b():
    df = pd.DataFrame(np.random.rand(2000000, 5), columns=["a", "b", "c", "d", "e"])
    return df


st.write(load_data_b())
b1 = time()
st.info(b1 - b0)
