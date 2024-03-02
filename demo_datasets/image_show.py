import os
import random

import streamlit as st

# Dataset
def dataset():
    st.session_state['dataset_image'] = './demo_datasets/images/datasets.jpg'
    st.image(st.session_state['dataset_image'])

ST_IMAGE_SHOW_DEMOS = {
    "datasets": (
        dataset,
        "Credit: https://github.com/switchablenorms/CelebAMask-HQ",
    ),
}
