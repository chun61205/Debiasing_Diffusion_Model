import os
import random
import torch
from diffusers import (
    AutoencoderKL,
    DDPMScheduler,
    StableDiffusionPipeline,
    StableDiffusionImg2ImgPipeline,
    DPMSolverMultistepScheduler,
    UNet2DConditionModel,
)
from peft import PeftModel, LoraConfig

from PIL import Image
from math import floor
from typing import Union, Optional, Tuple, Any

def get_lora_sd_pipeline(
    ckpt_dir                : str, 
    base_model_name_or_path : Optional[ str ] = None, 
    dtype                   : Optional[ torch.dtype ] = torch.float16, 
    device                  : Optional[ torch.device ] = "cuda", 
    adapter_name            : Optional[ str ] = "default"
):
    
    unet_sub_dir = os.path.join( ckpt_dir, "unet" )
    text_encoder_sub_dir = os.path.join(ckpt_dir, "text_encoder")
    if os.path.exists(text_encoder_sub_dir) and base_model_name_or_path is None:
        config = LoraConfig.from_pretrained(text_encoder_sub_dir)
        base_model_name_or_path = config.base_model_name_or_path

    if base_model_name_or_path is None:
        raise ValueError("Please specify the base model name or path")

    pipe = StableDiffusionPipeline.from_pretrained(
        base_model_name_or_path, torch_dtype=dtype, requires_safety_checker=False
    ).to(device)
    pipe.unet = PeftModel.from_pretrained(pipe.unet, unet_sub_dir, adapter_name=adapter_name)
    print(pipe.unet)

    if os.path.exists(text_encoder_sub_dir):
        pipe.text_encoder = PeftModel.from_pretrained(
            pipe.text_encoder, text_encoder_sub_dir, adapter_name=adapter_name
        )

    if dtype in (torch.float16, torch.bfloat16):
        pipe.unet.half()
        pipe.text_encoder.half()

    pipe.to(device)
    return pipe

def load_adapter(
    pipe        : StableDiffusionPipeline, 
    ckpt_dir    : str, 
    adapter_name: str ):

    unet_sub_dir = os.path.join(ckpt_dir, "unet")
    text_encoder_sub_dir = os.path.join(ckpt_dir, "text_encoder")
    pipe.unet.load_adapter(unet_sub_dir, adapter_name=adapter_name)
    if os.path.exists(text_encoder_sub_dir):
        pipe.text_encoder.load_adapter(text_encoder_sub_dir, adapter_name=adapter_name)

def set_adapter(pipe, adapter_name):
    pipe.unet.set_adapter(adapter_name)
    if isinstance(pipe.text_encoder, PeftModel):
        pipe.text_encoder.set_adapter(adapter_name)

def merging_lora_with_base(pipe, ckpt_dir, adapter_name = "default" ) -> StableDiffusionPipeline:
    """
    merging_lora_with_base:
    將 peft lora unit 的權重合併進原生 Stable Diffusion 內
    分為 UNet 與 text_encoder

    Args:
    ----------
    pipe: StableDiffusionPipeline
    待合併的權重
    ----------
    ckpt_dir: str
    儲存有 UNet 與 text_encoder 權重的資料夾
    ----------
    adapter_name: str
    愈合併的 adapter 的名字，預設為 `default`

    Return:
    ----------
    StableDiffusionPipeline
    合併後的 SD pipeline
    
    """
    unet_sub_dir = os.path.join(ckpt_dir, "unet")
    text_encoder_sub_dir = os.path.join(ckpt_dir, "text_encoder")
    if isinstance(pipe.unet, PeftModel):
        pipe.unet.set_adapter(adapter_name)
    else:
        pipe.unet = PeftModel.from_pretrained(pipe.unet, unet_sub_dir, adapter_name=adapter_name)
    pipe.unet = pipe.unet.merge_and_unload()
    print( 'peft-lora-pipeline, merging-lora-with-base: load unet' )

    if os.path.exists(text_encoder_sub_dir):
        if isinstance(pipe.text_encoder, PeftModel):
            pipe.text_encoder.set_adapter(adapter_name)
        else:
            pipe.text_encoder = PeftModel.from_pretrained(
                pipe.text_encoder, text_encoder_sub_dir, adapter_name=adapter_name
            )
        pipe.text_encoder = pipe.text_encoder.merge_and_unload()
        print( 'peft-lora-pipeline, merging-lora-with-base: load text encoder' )

    return pipe


def create_weighted_lora_adapter( 
    pipe : StableDiffusionPipeline, 
    adapters, 
    weights, 
    adapter_name = "default" ) -> StableDiffusionPipeline:

    pipe.unet.add_weighted_adapter(adapters, weights, adapter_name)
    if isinstance(pipe.text_encoder, PeftModel):
        pipe.text_encoder.add_weighted_adapter(adapters, weights, adapter_name)

    return pipe

def pipeline_generate( 
    ckpt_dir        : str,
    base_model      : str,
    device          : Optional[torch.device] = 'cuda',
    adapter_name    : Optional[str] = 'adapter',
    strength        : float = 0.8,
    dtype           : Optional[torch.dtype] = torch.float32,
    num_image       : Optional[int] = 1,) -> None:

    # Initializeng a normal pipeline
    pipe = StableDiffusionPipeline.from_pretrained(pretrained_model_name_or_path = base_model, torch_dtype=dtype)
    pipe = merging_lora_with_base( 
        pipe = pipe,
        ckpt_dir = ckpt_dir,
        adapter_name = adapter_name)
    pipe = pipe.to(device)

    seed = random.randint(0, 1000)
    torch.manual_seed(seed)
    generator = torch.Generator(device = device).manual_seed(seed)

    prompt = 'A human face'

    out = pipe( 
        prompt = prompt,
        num_inference_steps = 40,
        num_images_per_prompt = num_image,
        generator = generator
    )
    torch.cuda.empty_cache()
    result : Image.Image = out[0][0]
    result.convert("RGB")

    return result

def pipeline_reconstruct( 
    img,
    ckpt_dir        : str,
    base_model      : str,
    device          : Optional[torch.device] = 'cuda',
    adapter_name    : Optional[str] = 'adapter',
    strength        : float = 0.8,
    dtype           : Optional[torch.dtype] = torch.float16,
    num_image       : Optional[int] = 1,) -> None:

    # Initializing an img2img pipeline
    pipe = StableDiffusionImg2ImgPipeline.from_pretrained(pretrained_model_name_or_path = base_model, torch_dtype=dtype)
    pipe = merging_lora_with_base( 
        pipe = pipe,
        ckpt_dir = ckpt_dir,
        adapter_name = adapter_name)
    pipe = pipe.to(device)

    seed = random.randint(0, 1000)
    torch.manual_seed(seed)
    generator = torch.Generator(device = device).manual_seed(seed)
    print(device)
    prompt = 'A human face'
    
    out = pipe( 
        prompt = prompt,
        num_inference_steps = 40,
        image = img,
        num_images_per_prompt = num_image,
        strength = strength,
        generator = generator
    )
    torch.cuda.empty_cache()
    result : Image.Image = out[0][0]
    result.convert("RGB")
    
    return result

def random_check():
    torch.manual_seed(42)

    sample = torch.randn((2, 2))
    print(sample)

if __name__ == "__main__":
    image = Image.open("./images/base.jpg")
    ckpt_dir = './model'
    base_model = "runwayml/stable-diffusion-v1-5"
    dtype = torch.float16
    param_pipeline = {
            'ckpt_dir' : ckpt_dir,
            'base_model' : base_model,
            'adapter_name': 'adapter',
            'device' : 'cuda',
            'strength' : 0.98,
            'num_image': 1,
            'dtype' : dtype,
    }
    pipeline_reconstruct(image, **param_pipeline)