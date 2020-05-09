from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# for all the account processes

def home(request):
    # homepage
    return render(request,'account/signup.html')

def signup(request):
    # signup process
    if request.method=='POST':
        # checks if request method is POST
        mail = request.POST.get('email','')
        username = request.POST.get('username','')
        fname = request.POST.get('fname','')
        lname = request.POST.get('lname','')
        password = request.POST.get('password','')
        conf_pass = request.POST.get('confpassword','')

        # to check if username already exists
        sameUser=User.objects.filter(username=username)
        if sameUser:
            messages.error(request,"Username already exists")
            return redirect('/')

        # to check if password and conf password match
        if password==conf_pass:
            user_obj = User.objects.create_user(first_name = fname, last_name = lname, password = password, email = mail, username = username)
            user_obj.save()

    return redirect('/')

def user_login(request):
    # loginprocess
    if request.method=="POST":
        username = request.POST.get('username','')
        user_password = request.POST.get('password','')

        #authentication
        user = auth.authenticate(username= username, password = user_password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"Logged In")
            return redirect('/feed')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('/')

def user_logout(request):
    # logout process
    auth.logout(request)
    messages.success(request,"logged out")
    return redirect('/')
    
