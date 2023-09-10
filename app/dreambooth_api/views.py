# dreambooth_api/views.py
from django.shortcuts import render
import requests
import json

def fine_tune(request):
    if request.method == 'POST':
        url = "https://stablediffusionapi.com/api/v3/fine_tune"

        payload = json.dumps({
            "key": "Lax6AMj3Pcija31Rwh8ILndFLiGioOu99oSEPKnK9bcTRWjkXknBLcgwROI8",  # DreamBooth API 키를 넣어주세요.
            "instance_prompt": request.POST['instance_prompt'],
            "class_prompt": request.POST['class_prompt'],
            "base_model_id": "portraitplus-diffusion",
            "images": request.POST['images'].split(),  # 이미지 URL을 리스트로 변환
            "seed": "0",
            "training_type": "men", 
            "max_train_steps": "2000",
            "webhook": ""
        })

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200:
            result = response.json()
            return render(request, 'result.html', {'result': result})
        else:
            return render(request, 'error.html')

    return render(request, 'fine_tune.html')
