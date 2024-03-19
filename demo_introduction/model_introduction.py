import streamlit as st

def render_value_image():
    image_path = './demo_model/images/value.jpg'
    st.image(image_path)

def render_model_image():
    image_path = './demo_model/images/debiasing diffusion model.jpg'
    st.image(image_path)

# Update the ST_VALUE_DEMOS dictionary
ST_VALUE_DEMOS = {
    "Value": (
        render_value_image,
        None,
    ),
}

# Update the ST_MODEL_STRUCTURE_DEMOS dictionary
ST_MODEL_STRUCTURE_DEMOS = {
    "Display Model Structure": (
        render_model_image,
        "Stable Diffusion + feature learning indicator C = fairness generative model",
    ),
}

