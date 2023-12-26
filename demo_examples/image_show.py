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
    dataset_path = './demo_examples/images/dataset1_0'
    if st.button('Refresh', key='refresh1') or 'dataset1_0_image' not in st.session_state:
        st.session_state['dataset1_0_image'] = get_random_image(dataset_path)
    st.image(st.session_state['dataset1_0_image'])

# Dataset 1 function with a button to randomize the image (alpha = 0.1)
def dataset1_0_1():
    st.header("Male : Female = 1 : 4, alpha = 0.1")
    dataset_path = './demo_examples/images/dataset1_0_1'
    if st.button('Refresh', key='refresh1') or 'dataset1_0_1_image' not in st.session_state:
        st.session_state['dataset1_0_1_image'] = get_random_image(dataset_path)
    st.image(st.session_state['dataset1_0_1_image'])

# Dataset 1 function with a button to randomize the image (alpha = 0.05)
def dataset1_0_0_5():
    st.header("Male : Female = 1 : 4, alpha = 0.05")
    dataset_path = './demo_examples/images/dataset1_0_0_5'
    if st.button('Refresh', key='refresh1') or 'dataset1_0_0_5_image' not in st.session_state:
        st.session_state['dataset1_0_0_5_image'] = get_random_image(dataset_path)
    st.image(st.session_state['dataset1_0_0_5_image'])

# Dataset 1 function with a button to randomize the image (alpha = 0.01)
def dataset1_0_0_1():
    st.header("Male : Female = 1 : 4, alpha = 0.01")
    dataset_path = './demo_examples/images/dataset1_0_0_1'
    if st.button('Refresh', key='refresh1') or 'dataset1_0_0_1_image' not in st.session_state:
        st.session_state['dataset1_0_0_1_image'] = get_random_image(dataset_path)
    st.image(st.session_state['dataset1_0_0_1_image'])

ST_IMAGE_SHOW_DEMOS = {
    "Male : Female = 1 : 4, alpha = 0": (
        dataset1_0,
        "https://github.com/switchablenorms/CelebAMask-HQ",
    ),
    "Male : Female = 1 : 4, alpha = 0.1": (
        dataset1_0_1,
        "https://github.com/switchablenorms/CelebAMask-HQ",
    ),
    "Male : Female = 1 : 4, alpha = 0.05": (
        dataset1_0_0_5,
        "https://github.com/switchablenorms/CelebAMask-HQ",
    ),
    "Male : Female = 1 : 4, alpha = 0.01": (
        dataset1_0_0_1,
        "https://github.com/switchablenorms/CelebAMask-HQ",
    ),
}
