from django.db import models
from django.contrib.auth.models import User



class Student(models.Model):
      name=models.CharField(max_length=100)
      age=models.IntegerField()
      email=models.EmailField()
      address=models.TextField()
      image=models.ImageField()


class Csr(models.Model):
      car_name=models.CharField(max_length=500)
      speed=models.IntegerField(default=50)

class Receipe (models.Model):
      user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
      receipe_name=models.CharField(max_length=100)
      receipe_description=models.TextField()
      receipe_image=models.ImageField(upload_to="receipe")