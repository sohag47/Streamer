from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ExtraUserInfo(models.Model):
    user_info = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(
        null=True, blank=True, upload_to='userimage/')
    country = models.CharField(max_length=250)
    language = models.CharField(max_length=250)
    description = models.TextField(blank=True)
