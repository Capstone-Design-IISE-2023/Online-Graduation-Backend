from django.urls import path
from . import views

urlpatterns = [
    path('generate_graduation_photo/', views.generate_graduation_photo, name='generate_graduation_photo'),
]