import os
import random
import torch
import streamlit as st

from inference import pipeline

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

def inference():
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
    pipeline(**param_pipeline)

def reconstruction():
    st.header("Human Face Reconstruction")
    canvas_result = st.camera_input("Take a picture or draw on the canvas")

    if canvas_result:
        # Convert the camera input to a numpy array
        img = np.frombuffer(canvas_result.getvalue(), np.uint8)
        img = cv2.imdecode(img, cv2.IMREAD_COLOR)

        # Display the image on the canvas
        st.image(img, channels="BGR")

        if st.button("Generate"):
            # Code to generate an image using a model based on the user's drawing
            # Replace this with your own model implementation
            generated_image = img  # Example: Just passing the input image for now

            # Display the generated image
            st.image(generated_image, channels="BGR", caption="Generated Image")

ST_IMAGE_GEN_DEMOS = {
    "Male : Female = 1 : 4, alpha = 0": (
        dataset1_0,
        " ",
    )
}
