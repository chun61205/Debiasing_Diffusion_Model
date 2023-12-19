import os
import random

import streamlit as st

# Helper function to get a random image
def get_random_image(dataset_path):
    images = [file for file in os.listdir(dataset_path) if file.endswith('.jpg')]
    selected_image = random.choice(images) if images else None
    return os.path.join(dataset_path, selected_image) if selected_image else None

# Dataset 1 function with a button to randomize the image
def dataset1():
    st.header("Male : Female = 1 : 4")
    dataset_path = './demo_datasets/images/dataset1'
    if st.button('Randomize Image', key='randomize1') or 'dataset1_image' not in st.session_state:
        st.session_state['dataset1_image'] = get_random_image(dataset_path)
    st.image(st.session_state['dataset1_image'])

# Dataset 2 function with a button to randomize the image
def dataset2():
    st.header("Male : Female = 4 : 1")
    dataset_path = './demo_datasets/images/dataset2'
    if st.button('Randomize Image', key='randomize2') or 'dataset2_image' not in st.session_state:
        st.session_state['dataset2_image'] = get_random_image(dataset_path)
    st.image(st.session_state['dataset2_image'])

ST_IMAGE_SHOW_DEMOS = {
    "Male : Female = 1 : 4": (
        dataset1,
        None,
    ),
    "Male : Female = 4 : 1": (
        dataset2,
        None,
    )
}
