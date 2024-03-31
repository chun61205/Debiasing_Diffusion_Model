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
    if st.button('Refresh', key='refresh1_0') or 'dataset1_0_image' not in st.session_state:
        st.session_state['dataset1_0_image'] = get_random_image(dataset_path)
    st.image(st.session_state['dataset1_0_image'])

# Dataset 1 function with a button to randomize the image (alpha = 0.1)
def dataset1_0_1():
    st.header("Male : Female = 1 : 4, alpha = 0.1")
    dataset_path = './demo_examples/images/dataset1_0_1'
    if st.button('Refresh', key='refresh1_0_1') or 'dataset1_0_1_image' not in st.session_state:
        st.session_state['dataset1_0_1_image'] = get_random_image(dataset_path)
    st.image(st.session_state['dataset1_0_1_image'])

# Dataset 1 function with a button to randomize the image (alpha = 0.05)
def dataset1_0_0_5():
    st.header("Male : Female = 1 : 4, alpha = 0.05")
    dataset_path = './demo_examples/images/dataset1_0_0_5'
    if st.button('Refresh', key='refresh1_0_0_5') or 'dataset1_0_0_5_image' not in st.session_state:
        st.session_state['dataset1_0_0_5_image'] = get_random_image(dataset_path)
    st.image(st.session_state['dataset1_0_0_5_image'])

# Dataset 1 function with a button to randomize the image (alpha = 0.01)
def dataset1_0_0_1():
    st.header("Male : Female = 1 : 4, alpha = 0.01")
    dataset_path = './demo_examples/images/dataset1_0_0_1'
    if st.button('Refresh', key='refresh1_0_0_1') or 'dataset1_0_0_1_image' not in st.session_state:
        st.session_state['dataset1_0_0_1_image'] = get_random_image(dataset_path)
    st.image(st.session_state['dataset1_0_0_1_image'])

# Dataset 2 function with a button to randomize the image (alpha = 0)
def dataset2_0():
    st.header("Male : Female = 4 : 1, alpha = 0")
    dataset_path = './demo_examples/images/dataset2_0'
    if st.button('Refresh', key='refresh2_0') or 'dataset2_0_image' not in st.session_state:
        st.session_state['dataset2_0_image'] = get_random_image(dataset_path)
    st.image(st.session_state['dataset2_0_image'])

# Dataset 2 function with a button to randomize the image (alpha = 0.1)
def dataset2_0_1():
    st.header("Male : Female = 4 : 1, alpha = 0.1")
    dataset_path = './demo_examples/images/dataset2_0_1'
    if st.button('Refresh', key='refresh2_0_1') or 'dataset2_0_1_image' not in st.session_state:
        st.session_state['dataset2_0_1_image'] = get_random_image(dataset_path)
    st.image(st.session_state['dataset2_0_1_image'])

# Dataset 2 function with a button to randomize the image (alpha = 0.05)
def dataset2_0_0_5():
    st.header("Male : Female = 4 : 1, alpha = 0.05")
    dataset_path = './demo_examples/images/dataset2_0_0_5'
    if st.button('Refresh', key='refresh2_0_0_5') or 'dataset2_0_0_5_image' not in st.session_state:
        st.session_state['dataset2_0_0_5_image'] = get_random_image(dataset_path)
    st.image(st.session_state['dataset2_0_0_5_image'])

# Dataset 2 function with a button to randomize the image (alpha = 0.01)
def dataset2_0_0_1():
    st.header("Male : Female = 4 : 1, alpha = 0.01")
    dataset_path = './demo_examples/images/dataset2_0_0_1'
    if st.button('Refresh', key='refresh2_0_0_1') or 'dataset2_0_0_1_image' not in st.session_state:
        st.session_state['dataset2_0_0_1_image'] = get_random_image(dataset_path)
    st.image(st.session_state['dataset2_0_0_1_image'])

# Dataset 3 function with a button to randomize the image (alpha = 0)
def dataset3_0():
    st.header("Male : Female = 1 : 1, alpha = 0")
    dataset_path = './demo_examples/images/dataset3_0'
    if st.button('Refresh', key='refresh3_0') or 'dataset3_0_image' not in st.session_state:
        st.session_state['dataset3_0_image'] = get_random_image(dataset_path)
    st.image(st.session_state['dataset3_0_image'])

# Dataset 3 function with a button to randomize the image (alpha = 0.1)
def dataset3_0_1():
    st.header("Male : Female = 1 : 1, alpha = 0.1")
    dataset_path = './demo_examples/images/dataset3_0_1'
    if st.button('Refresh', key='refresh3_0_1') or 'dataset3_0_1_image' not in st.session_state:
        st.session_state['dataset3_0_1_image'] = get_random_image(dataset_path)
    st.image(st.session_state['dataset3_0_1_image'])

# Dataset 3 function with a button to randomize the image (alpha = 0.05)
def dataset3_0_0_5():
    st.header("Male : Female = 1 : 1, alpha = 0.05")
    dataset_path = './demo_examples/images/dataset3_0_0_5'
    if st.button('Refresh', key='refresh3_0_0_5') or 'dataset3_0_0_5_image' not in st.session_state:
        st.session_state['dataset3_0_0_5_image'] = get_random_image(dataset_path)
    st.image(st.session_state['dataset3_0_0_5_image'])

# Dataset 3 function with a button to randomize the image (alpha = 0.01)
def dataset3_0_0_1():
    st.header("Male : Female = 2 : 1, alpha = 0.01")
    dataset_path = './demo_examples/images/dataset3_0_0_1'
    if st.button('Refresh', key='refresh3_0_0_1') or 'dataset3_0_0_1_image' not in st.session_state:
        st.session_state['dataset3_0_0_1_image'] = get_random_image(dataset_path)
    st.image(st.session_state['dataset3_0_0_1_image'])

ST_IMAGE_SHOW_DEMOS = {
    "Male : Female = 1 : 4, alpha = 0": (
        dataset1_0,
        " ",
    ),
    "Male : Female = 1 : 4, alpha = 0.1": (
        dataset1_0_1,
        " ",
    ),
    "Male : Female = 1 : 4, alpha = 0.05": (
        dataset1_0_0_5,
        " ",
    ),
    "Male : Female = 1 : 4, alpha = 0.01": (
        dataset1_0_0_1,
        " ",
    ),
    "Male : Female = 4 : 1, alpha = 0": (
        dataset2_0,
        " ",
    ),
    "Male : Female = 4 : 1, alpha = 0.1": (
        dataset2_0_1,
        " ",
    ),
    "Male : Female = 4 : 1, alpha = 0.05": (
        dataset2_0_0_5,
        " ",
    ),
    "Male : Female = 4 : 1, alpha = 0.01": (
        dataset2_0_0_1,
        " ",
    ),
    "Male : Female = 1 : 1, alpha = 0": (
        dataset3_0,
        " ",
    ),
    "Male : Female = 1 : 1, alpha = 0.1": (
        dataset3_0_1,
        " ",
    ),
    "Male : Female = 1 : 1, alpha = 0.05": (
        dataset3_0_0_5,
        " ",
    ),
    "Male : Female = 1 : 1, alpha = 0.01": (
        dataset3_0_0_1,
        " ",
    ),
}
