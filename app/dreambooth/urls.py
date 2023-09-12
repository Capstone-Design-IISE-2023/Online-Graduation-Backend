from django.urls import path
from . import views

urlpatterns = [
    path('', views.dreambooth_fine_tune, name='fine_tue')
]