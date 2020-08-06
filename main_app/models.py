from django.db import models
from django.contrib.auth.models import User
from datetime import date, timezone

# Create your models here.
class City(models.Model):
  name = models.CharField(max_length=100)
  country = models.CharField(max_length=150)
  picture = models.FileField(upload_to='uploads/')
      
  def __str__(self):
    return self.name
    
class Profile(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.OneToOneField(User, on_delete=models.CASCADE) i found this in the lecture. looks like this needs to be one to one not foreign key
    profile_picture = models.FileField(upload_to='uploads/')
    # profile_date = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.first_name


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    picture = models.FileField(upload_to='uploads/')
    date = models.DateField(auto_now=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    def __str__(self):
      return self.title