from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    # for Post Table in db
    user=models.ForeignKey(User,on_delete=models.CASCADE)       #user who posts th Post
    caption= models.CharField(max_length=200)
    image = models.ImageField(upload_to="user_images/Posts")
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)+" "+str(self.date)

class Profile(models.Model):
    # for Profile Table for profile pages in db
    user=models.ForeignKey(User,on_delete=models.CASCADE)       #user who created the profile
    diplayPicture=models.ImageField(upload_to="user_image/Profiles")
    bio=models.CharField(max_length=200, blank=True)
    followers=models.IntegerField(default=0)
    following=models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)
