import streamlit as st

def render_png_image():
    image_path = './demo_model/images/Debiasing Diffusion Model.png'
    st.image(image_path)

# Update the ST_MODEL_STRUCTURE_DEMOS dictionary
ST_MODEL_STRUCTURE_DEMOS = {
    "Display Model Structure": (
        render_png_image,
        "We introduce the debiasing modele including an bias mitigating indicator C operating in the denoising process, which utilizes denoised latent variables as inputs to identify and learn potential attributes. This indicator outputs a value ŷ which serves as a key factor in the loss computation, thereby guiding the model’s learning process. However, this output is solely utilized for training and is not involved in image generation tasks.",
    ),
}