from django.db import models

class UserPhotos(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    portrait_photo = models.ImageField(upload_to='user_photos/')    #n개 필요
    graduation_prompt = models.CharField(max_length=255)    # prompt
    graduation_negative_prompt = models.CharField(max_length=255)   # negative prompt

# Create your models here.
