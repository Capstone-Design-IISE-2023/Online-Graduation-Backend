# dreambooth_api/views.py

import os
import torch
import numpy as np
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserImageUploadForm
from .models import UserPhotos
from diffusers import StableDiffusionPipeline, DDIMScheduler
from PIL import Image
from django.http import HttpResponse
from torch.cuda.amp import autocast
from google.cloud import storage


def generate_dreambooth(request):
    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")
    seed = 1

    if request.method == 'POST':
        form = UserImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()

            bucket_name = 'capstone-design-iise'
            client = storage.Client()
            bucket = client.get_bucket(bucket_name)

            image_path_in_bucket = 'gs://capstone-design-iise/images/Slide1.png'
            temp_image_path = os.path.join(settings.MEDIA_ROOT, 'temp_image.jpg')
            blob = bucket.blob(image_path_in_bucket)
            blob.download_to_filename(temp_image_path)

            prompt = "(masterpiece), ultra realistic, photo of zwx person wearing graduation gown, wearing graduation cap, highly detailed, dslr, sharp focus, tack sharp, 4K, 8K,"
            negative_prompt = "bad anatomy, bad eyes, bad hands, bad proportions, cloned face, deformed, disfigured, double head, extra arms, extra digit, extra heads, extra legs, extra limbs, fewer digits, gross proportions, malformed limbs, missing arms, missing fingers, missing legs, mutated, mutated hands, poorly drawn face, poorly drawn hands, too many fingers, ugly eyes, black and white, blurry, boring, close up, confusing, cropped, depth of field, distorted, grainy, monochrome, multiple people, noisy, out of focus, out of frame, out of shot, oversaturated, error, fake, glitchy, jpeg artifacts, low quality, worst quality, fonts, logo, signature, text, username, watermark, writing"
            guidance_scale = 7.5

            g_cuda = torch.Generator(device='cuda')
            g_cuda.manual_seed(seed)

            with autocast("cuda"), torch.inference_mode():
                images = pipe(
                    prompt,
                    height=512,
                    width=512,
                    negative_prompt=negative_prompt,
                    num_images_per_prompt=1,
                    num_inference_steps=30,
                    guidance_scale=guidance_scale,
                    generator=g_cuda
                ).images

            if images:
                generated_image = images[0].cpu()
                generated_image = generated_image.permute(1, 2, 0).numpy()
                generated_image = (generated_image * 255).astype(np.uint8)
                generated_image = Image.fromarray(generated_image)
                generated_image_path = os.path.join(settings.MEDIA_ROOT, 'generated_images', 'output.png')
                generated_image.save(generated_image_path)

                image_instance.generated_image = generated_image_path
                image_instance.save()

                return redirect('show_generated_image', pk=image_instance.pk)
        else:
            form = UserImageUploadForm()
        return render(request, 'upload_image.html', {'form': form})

def show_generated_image(request, pk):
    image_instance = get_object_or_404(UserPhotos, pk=pk)
    with open(image_instance.generated_image.path, 'rb') as img_file:
        response = HttpResponse(img_file.read(), content_type='image/png')
    return response