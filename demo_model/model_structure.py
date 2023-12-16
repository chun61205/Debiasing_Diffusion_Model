import streamlit as st

def render_png_image():
    image_path = './images/De-Biasing Diffusion Model.png'
    st.image(image_path)

# Update the ST_MODEL_STRUCTURE_DEMOS dictionary
ST_MODEL_STRUCTURE_DEMOS = {
    "Display Model Structure": (
        render_png_image,
        None,
    ),
}