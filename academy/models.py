from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField
from django.db.models.fields.related import ForeignKey

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


class StudentData(models.Model):
    name = models.CharField(max_length=200)
    placeOfBirth = models.CharField(max_length=200)
    dateOfBirth = DateField()
    gender = models.CharField(max_length=200)
    address = models.TextField()
    handphone = models.CharField(max_length=200)
    education = models.SmallIntegerField()
    user = models.OneToOneField(User, on_delete=CASCADE)


class ClassData(models.Model):
    name = models.CharField(max_length=200)
    meetingsCount = models.SmallIntegerField()
    # activeDay = models.CharField(max_length=200, null=True)
    price = models.IntegerField()


class Branch(models.Model):
    name = models.CharField(max_length=300)


class ClassInBranch(models.Model):
    branch = models.ForeignKey(Branch, on_delete=CASCADE)
    classRegistered = models.ForeignKey(ClassData, on_delete=CASCADE)


class StudentAttendClass(models.Model):
    student = models.ForeignKey(StudentData, on_delete=CASCADE)
    classToAttend = models.ForeignKey(ClassData, on_delete=CASCADE)
