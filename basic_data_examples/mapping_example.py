import streamlit as st
import pandas as pd
import pydeck as pdk


@st.cache_data
def from_data_file(filename):
    url = (
        "https://raw.githubusercontent.com/streamlit/"
        "example-data/master/hello/v1/%s" % filename
    )
    return pd.read_json(url)


try:
    # Define different map layers for visualization
    ALL_LAYERS = {
        "Bike Rentals": pdk.Layer(
            "HexagonLayer",  # Layer type for hexagonal bins
            data=from_data_file("bike_rental_stats.json"),  # Bike rental data
            get_position=["lon", "lat"],  # Longitude and latitude columns
            radius=200,  # Radius of each hexagon bin in meters
            elevation_scale=4,  # Scale of bin elevation
            elevation_range=[0, 1000],  # Elevation range for bins
            extruded=True,  # Extrusion enables 3D elevation
        ),
        "Bart Stop Exits": pdk.Layer(
            "ScatterplotLayer",  # Layer type for scatter points
            data=from_data_file("bart_stop_stats.json"),  # BART stop data
            get_position=["lon", "lat"],  # Longitude and latitude columns
            get_color=[200, 30, 0, 160],  # RGBA color for each point
            get_radius="[exits]",  # Radius of each point based on 'exits' column
            radius_scale=0.05,  # Scale factor for radius
        ),
        "Bart Stop Names": pdk.Layer(
            "TextLayer",  # Layer type for displaying text
            data=from_data_file("bart_stop_stats.json"),  # BART stop data
            get_position=["lon", "lat"],  # Longitude and latitude columns
            get_text="name",  # Column for text to display (stop name)
            get_color=[0, 0, 0, 200],  # RGBA color for text
            get_size=10,  # Font size
            get_alignment_baseline="'bottom'",  # Align text to the bottom
        ),
        "Outbound Flow": pdk.Layer(
            "ArcLayer",  # Layer type for connecting points with arcs
            data=from_data_file("bart_path_stats.json"),  # BART path data
            get_source_position=["lon", "lat"],  # Start point coordinates
            get_target_position=["lon2", "lat2"],  # End point coordinates
            get_source_color=[200, 30, 0, 160],  # RGBA color at the start
            get_target_color=[200, 30, 0, 160],  # RGBA color at the end
            auto_highlight=True,  # Highlights arcs on hover
            width_scale=0.0001,  # Scale for arc width
            get_width="outbound",  # Width based on 'outbound' column
            width_min_pixels=3,  # Minimum arc width in pixels
            width_max_pixels=30,  # Maximum arc width in pixels
        ),
    }
    # Sidebar for selecting map layers
    st.sidebar.markdown("### Map Layers")
    # Display checkboxes for each layer in the sidebar and collect selected layers
    selected_layers = [
        layer
        for layer_name, layer in ALL_LAYERS.items()
        if st.sidebar.checkbox(layer_name, True)  # Default checked
    ]

    # Render the map if at least one layer is selected
    if selected_layers:
        st.pydeck_chart(
            pdk.Deck(
                map_style=None,  # Default map style
                initial_view_state={  # Initial map view configuration
                    "latitude": 37.76,  # Latitude center for view
                    "longitude": -122.4,  # Longitude center for view
                    "zoom": 11,  # Initial zoom level
                    "pitch": 50,  # Map pitch angle
                },
                layers=selected_layers,  # Display only selected layers
            )
        )
    else:
        # Display error if no layers are selected
        st.error("Please choose at least one layer above.")

# Catch network errors in case data loading fails
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )
