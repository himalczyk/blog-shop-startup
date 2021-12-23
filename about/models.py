from django.db import models
# from core import user_info

# Create your models here.

class About(models.Model):
    title = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    # admins = models.TextField(default= user_info())
