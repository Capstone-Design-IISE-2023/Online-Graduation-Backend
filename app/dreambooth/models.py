from django.db import models

class UserPhotos(models.Model):
    image = models.ImageField(upload_to="uploads/")
    generated_image = models.ImageField(upload_to="generated_images/")
