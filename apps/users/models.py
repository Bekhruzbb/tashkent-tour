from django.db import models
from apps.common.models import BaseModel
# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to="profiles/images/", null=True, blank=True)
    phone_number = models.CharField(max_length=15)

