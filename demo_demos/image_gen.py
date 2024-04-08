import os
import random

import streamlit as st

# Helper function to get a random image
def get_random_image(dataset_path):
    images = [file for file in os.listdir(dataset_path) if file.endswith('.jpg')]
    selected_image = random.choice(images) if images else None
    return os.path.join(dataset_path, selected_image) if selected_image else None

# Dataset 1 function with a button to randomize the image (alpha = 0)
def dataset1_0():
    st.header("Male : Female = 1 : 4, alpha = 0")
    dataset_path = './demo_demos/images/dataset1_0'
    if st.button('Refresh', key='refresh1_0') or 'dataset1_0_image' not in st.session_state:
        st.session_state['dataset1_0_image'] = get_random_image(dataset_path)
    st.image(st.session_state['dataset1_0_image'])

ST_IMAGE_GEN_DEMOS = {
    "Male : Female = 1 : 4, alpha = 0": (
        dataset1_0,
        " ",
    )
}
