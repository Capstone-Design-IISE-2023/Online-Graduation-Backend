# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_dreambooth, name='generate_dreambooth'),  # 'fine_tue'를 'generate_dreambooth'로 수정
]
