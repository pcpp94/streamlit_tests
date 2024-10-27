import streamlit as st
import altair as alt
import pandas as pd


@st.cache_data
def get_UN_data():  # This decorator caches the function output, so get_UN_data() is only run once unless the data source or parameters change. This improves performance by reducing redundant data loading.
    AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")


try:
    df = get_UN_data()
    countries = st.multiselect("Choose countries", list(df.index), ["Peru", "Chile"])
    if not countries:
        st.error("Please select at least one country.")
    else:
        data = df.loc[countries]
        data /= 1000000.0
        st.write(
            "### Gross Agricultural Production ($B)", data.sort_index()
        )  # Displays a table of the gross agricultural production data (in billions of dollars) sorted by index.

        data = data.T.reset_index()  # data = data.T.reset_index()
        data = pd.melt(
            data, id_vars=["index"]
        ).rename(  # Unpivots the DataFrame, creating a long format DataFrame with columns "year" and "Gross Agricultural Product ($B)".
            columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
        )
        chart = (
            alt.Chart(data)  # Creates an Altair chart from the DataFrame.
            .mark_area(opacity=0.3)
            .encode(
                x="year:T",
                y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
                color="Region:N",
            )
        )
        st.altair_chart(
            chart, use_container_width=True
        )  # Renders the Altair chart in Streamlit with the container width set to fit the display.
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )
