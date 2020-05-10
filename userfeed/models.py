from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    # for Post Table in db
    user=models.ForeignKey(User,on_delete=models.CASCADE)       #user who posts th Post
    caption= models.CharField(max_length=200)
    image = models.ImageField(upload_to="Posts")
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)+" "+str(self.date)

class Profile(models.Model):
    # for Profile Table for profile pages in db
    user=models.ForeignKey(User,on_delete=models.CASCADE)       #user who created the profile
    displayPicture=models.ImageField(upload_to="Profiles", default="default/default-user-icon.jpg")
    bio=models.CharField(max_length=200, blank=True)
    followers=models.IntegerField(default=0)
    following=models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)

class Like(models.Model):
    user = models.ManyToManyField(User, related_name="liking_user")
    post = models.OneToOneField(Post, on_delete=models.CASCADE) # class methods are much like static methods , can be accessed by class name as well as object name 
    #the class method is always attached to a class with first argument as the class itself cls.

    # for liking post
    @classmethod
    def like(cls, post, likingUser):
        #instead of self we use cls
        obj, create  = cls.objects.get_or_create(post = post)
        obj.user.add(likingUser)

    # for disliking post
    @classmethod
    def dislike(cls, post, dislikingUser):
        obj, create  = cls.objects.get_or_create(post = post) # if an object exists returns(object,false),  else creates an object and returns (object,True)
        
        obj.user.remove(dislikingUser)

    def __str__(self):
        return str(self.post)


