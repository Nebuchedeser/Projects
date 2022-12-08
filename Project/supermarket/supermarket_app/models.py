# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class Item(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  description = models.TextField()
  image = models.ImageField()
  category = models.ForeignKey('Category', on_delete=models.CASCADE)
  subcategory = models.ForeignKey('Subcategory', on_delete=models.CASCADE)
  public = models.BooleanField(default=False)

class Category(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)

class Subcategory(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  category = models.ForeignKey('Category', on_delete=models.CASCADE)

class UserManager(models.Manager):
  def create_user(self, first_name, last_name, username, email, password, photo):
    user = self.model(
      first_name=first_name,
      last_name=last_name,
      username=username,
      email=email,
      password=password,
      photo=photo
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

class User(AbstractUser):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.EmailField()
  photo = models.ImageField()

  objects = UserManager()
