# st.form creates a form that batches elements together with a "Submit" button.
# Typically, whenever a user interacts with a widget, the Streamlit app is rerun.

# A form is a container that visually groups other elements and widgets together, and contains a Submit button.
# Herein, a user can interacts with one or more widgets for as many times as they like without causing a rerun.
# Finally, when the form's Submit button is pressed, all widget values inside the form will be sent to Streamlit in a single batch.

# To add elements to a form object, you can use the with notation (preferred)
# or you could use it as an object notation by just calling methods directly on the form
# (by first assigning it to a variable and subsequently applying Streamlit methods on it). See in the example app.

# Forms have a few constraints:

# Every form must contain a st.form_submit_button.
# st.button and st.download_button cannot be added to a form.
# Forms can appear anywhere in your app (sidebar, columns, etc), but they cannot be embedded inside other forms.

import streamlit as st

st.title("st.form")

# Full example of using the with notation
st.header("1. Example of using `with` notation")
st.subheader("Coffee machine")

with st.form("my_form"):
    st.subheader("**Order your coffee**")

    # Input widgets
    coffee_bean_val = st.selectbox("Coffee bean", ["Arabica", "Robusta"])
    coffee_roast_val = st.selectbox("Coffee roast", ["Light", "Medium", "Dark"])
    brewing_val = st.selectbox(
        "Brewing method", ["Aeropress", "Drip", "French press", "Moka pot", "Siphon"]
    )
    serving_type_val = st.selectbox("Serving format", ["Hot", "Iced", "Frappe"])
    milk_val = st.select_slider("Milk intensity", ["None", "Low", "Medium", "High"])
    owncup_val = st.checkbox("Bring own cup")

    # Every form must have a submit button
    submitted = st.form_submit_button("Submit")

if submitted:
    st.markdown(
        f"""
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        """
    )
else:
    st.write("☝️ Place your order!")


# Short example of using an object notation
st.header("2. Example of object notation")

form = st.form("my_form_2")
selected_val = form.slider("Select a value")
form.form_submit_button("Submit")

st.write("Selected value: ", selected_val)
