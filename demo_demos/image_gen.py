import os
import random
import torch
import cv2

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from PIL import Image, ImageEnhance
from .inference import pipeline_generate, pipeline_reconstruct
from streamlit_drawable_canvas import st_canvas

def generate():
    st.header("Fair Human Face Generator")
    st.session_state['generated_image'] = Image.new('RGB', (1024, 1024), color='white')
    if st.button('Generate', key='generate'):
        ckpt_dir = './demo_demos/model'
        base_model = "runwayml/stable-diffusion-v1-5"
        dtype = torch.float32
        #IMAGE_FOLDER = 'mixed_dataset/img'

        if torch.cuda.is_available() is True:
            device = 'cuda'
        else:
            device = 'cpu'
        print('peft_lora_pipeline, device: {}'.format(device))
        
        param_pipeline = {
            'ckpt_dir' : ckpt_dir,
            'base_model' : base_model,
            'adapter_name': 'adapter',
            'device' : device,
            'strength' : 0.98,
            'num_image': 5,
            'dtype' : dtype,
        }
        st.session_state['generated_image'] = pipeline_generate(**param_pipeline)
    if(st.session_state['generated_image'] != None):
        st.image(st.session_state['generated_image'])

def reconstruct():
    st.header("Fair Human Face Reconstructor")
    drawing_mode = st.sidebar.selectbox(
        "Drawing tool:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )
    stroke_width = st.sidebar.slider("Stroke width: ", 1, 10, 3)
    if drawing_mode == "point":
        point_display_radius = st.sidebar.slider("Point display radius: ", 1, 10, 3)
    stroke_color = st.sidebar.color_picker("Stroke color hex: ")
    bg_image = Image.open("./demo_demos/images/base.jpg").convert('RGBA')
    realtime_update = st.sidebar.checkbox("Update in realtime", True)

    # Create a canvas component
    canvas_result = st_canvas(
        fill_color="rgba(255, 255, 255, 0.3)",
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_image=bg_image,
        update_streamlit=realtime_update,
        height = 512,
        width = 512,
        drawing_mode=drawing_mode,
        point_display_radius=point_display_radius if drawing_mode == "point" else 0,
        display_toolbar=st.sidebar.checkbox("Display toolbar", True),
        key="full_app",
    )
    if canvas_result.image_data is not None:
        canvasImg = Image.fromarray(canvas_result.image_data)
        img = Image.alpha_composite(bg_image, canvasImg)
    else:
        img = bg_image
    
    # Adjusting
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(0.7) 
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(0.5)
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(2.0)
    st.image(img)
    if st.button('Reconstruct', key='reconstruct'):
        ckpt_dir = './demo_demos/model'
        base_model = "runwayml/stable-diffusion-v1-5"
        dtype = torch.float32

        if torch.cuda.is_available() is True:
            device = 'cuda'
        else:
            device = 'cpu'
        print('peft_lora_pipeline, device: {}'.format(device))
        
        param_pipeline = {
            'ckpt_dir' : ckpt_dir,
            'base_model' : base_model,
            'adapter_name': 'adapter',
            'device' : device,
            'strength' : 0.98,
            'num_image': 5,
            'dtype' : dtype,
        }
        st.session_state['reconstructed_image'] = pipeline_reconstruct(img, **param_pipeline)
    if(st.session_state['reconstructed_image'] != None):
        st.image(st.session_state['reconstructed_image'])

ST_IMAGE_GEN_DEMOS = {
    "Fair Human Face Generator": (
        generate,
        " ",
    ),
    "Fair Human Face Reconstructor": (
        reconstruct,
        " ",
    )
}
