import streamlit as st

def render_image():
    image_path = './demo_value/images/value.jpg'
    st.image(image_path)

# Update the ST_VALUE_DEMOS dictionary
ST_VALUE_DISPLAY_DEMOS = {
    "Value Display": (
        render_image,
        None,
    ),
}