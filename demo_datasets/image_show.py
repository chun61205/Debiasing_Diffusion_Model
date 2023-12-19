import os
import random

import streamlit as st

# Male : Female = 1 : 4
def dataset1():
    dataset_path = './demo_datasets/images/dataset1'
    images = [file for file in os.listdir(dataset_path) if file.endswith('.jpg')]
    selected_image = random.choice(images) if images else None
    image_path = os.path.join(dataset_path, selected_image) if selected_image else None
    st.image(image_path)

def dataset2():
    dataset_path = './demo_datasets/images/dataset2'
    images = [file for file in os.listdir(dataset_path) if file.endswith('.jpg')]
    selected_image = random.choice(images) if images else None
    image_path = os.path.join(dataset_path, selected_image) if selected_image else None
    st.image(image_path)

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
