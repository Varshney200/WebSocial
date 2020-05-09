from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Post, Profile
# Create your views here.
def userHome(request):
    # the feed page
    posts = Post.objects.all().order_by('-pk')
    data = {'posts':posts}
    return render(request,'userfeed/userfeed.html',data)

def post(request):
    # post process 
    if request.method=="POST":
        pimage = request.FILES['image']
        pcaption = request.POST.get('caption','')
        puser = request.user
        # making a Post object 
        post_obj = Post(user= puser, caption= pcaption, image=pimage)
        post_obj.save()
        messages.success(request,"Posted")
        return redirect('/feed')
    else:
        messages.success(request, "Something went wrong :(")

def delPost(request, postId):
    # delete Post process
    post=Post.objects.filter(pk=postId)
    image_path = post[0].image.url
    post.delete()
    messages.info(request,"Post Deleted")
    return redirect('/feed')

def userProfile(request,username):
    users = User.objects.filter(username=username)
    if users:
        # as users is a list of users. As only one user with one username may exist, list should contain only one element
        for user in users:
            profile=Profile.objects.get(user=user)
            posts=getPostImages(user)
            followers=profile.followers
            following=profile.following
            userImage=profile.displayPicture
            # creating a dictionary to be passed in render
            data={'username':user.username,
                'fname':user.first_name,
                'lname':user.last_name,
                'bio':profile.bio, 
                'followers':followers, 
                'following':following,
                'userImage':userImage,
                'posts':posts,
            }
            return render(request, 'userfeed/userprofile.html',data)
    else:
        # if no username matches the database
        messages.success(request, "User does not exist")
        return redirect('/feed')

def getPostImages(user):
    # to get all the posts made by the user whose profile page is being used
    postObj = Post.objects.filter(user=user)
    # making a list of lists of 3 posts each and returning the list
    imgList= [postObj[i:i+3] for i in range(0, len(postObj), 3)]
    return imgList