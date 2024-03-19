import streamlit as st

def render_image():
    image_path = './demo_model/images/value.jpg'
    st.image(image_path)

# Update the ST_MODEL_STRUCTURE_DEMOS dictionary
ST_VALUE_DISPLAY_DEMOS = {
    "Value": (
        render_image,
        None
    ),
}