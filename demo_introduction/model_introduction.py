import streamlit as st

def render_value_image():
    image_path = './demo_introduction/images/value.jpg'
    st.image(image_path)

def render_model_image():
    image_path = './demo_introduction/images/debiasing diffusion model.jpg'
    st.image(image_path)

ST_DISPLAY_INTRODUCTION_DEMOS = {
    "Value": (
        render_value_image,
        None,
    ),
    "Display Model Structure": (
        render_model_image,
        "Stable Diffusion + feature learning indicator C = fairness generative model",
    ),
}

