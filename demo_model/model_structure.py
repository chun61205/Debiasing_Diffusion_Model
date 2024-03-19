import streamlit as st

def render_png_image():
    image_path = './demo_model/images/Debiasing Diffusion Model.jpg'
    st.image(image_path)

# Update the ST_MODEL_STRUCTURE_DEMOS dictionary
ST_MODEL_STRUCTURE_DEMOS = {
    "Display Model Structure": (
        render_png_image,
        "Stable Diffusion + feature learning indicator C = fairness generative model",
    ),
}