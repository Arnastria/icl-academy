from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    ADMIN = 0
    TEACHER = 1
    STUDENT = 2
    USER_LEVEL_CHOICES = (
        (ADMIN, "Admin"),
        (TEACHER, "Teacher"),
        (STUDENT, "Student"),
    )
    user_level = models.IntegerField(choices=USER_LEVEL_CHOICES, null=True)
