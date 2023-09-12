# dreambooth_api/views.py
from django.shortcuts import render
import requests
import json
from django.conf import settings

def dreambooth_fine_tune(request):
    if request.method == 'POST':
        url = "https://stablediffusionapi.com/api/v3/fine_tune"

        payload = json.dumps({
            "key": settings.DREAMBOOTH_API_KEY,
            "instance_prompt": request.POST['instance_prompt'], # prompt 확인 필요
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
            return render(request, 'result.html', {'result': result})   #프론트 연결 때 바꿔야 함.
        else:
            return render(request, 'error.html')

    return render(request, 'fine_tune.html')
