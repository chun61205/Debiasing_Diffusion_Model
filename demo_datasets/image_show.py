import os
import random

import streamlit as st

# Dataset
def dataset():
    if st.button('Refresh', key='refresh1') or 'dataset_image' not in st.session_state:
        st.session_state['dataset_image'] = './demo_datasets/images/datasets.jpg'
    st.image(st.session_state['dataset_image'])

ST_IMAGE_SHOW_DEMOS = {
    "Datasets": (
        dataset,
        "Credit: https://github.com/switchablenorms/CelebAMask-HQ",
    ),
}
