
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib import messages, auth
from .models import UserProfile



# Create your views here.
def user_index(request):
    return render(request,'userindex.html')

@never_cache
@login_required(login_url='/user_login')
def user_home(request):
    dict_users = {
        'users': User.objects.all()
    }
    return render(request,'userhome.html',dict_users)

@never_cache
def user_login(request):
   
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username,"haiiiiiiiiiiiiiiiiiiiiiiii")
        user= authenticate(username=username, password=password)
        print(user,"userrrrrrrrrrrrrrrrrrrr")

        if user is not None:
            login(request,user)
            messages.success(request, "Login successful.")
            return redirect('user_home')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request,'userlogin.html')

def user_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username is taken.")
            return redirect("/user_signup")

        if User.objects.filter(email=email).exists():
            messages.info(request, "Email is already registered.")
            return redirect("/user_signup")

        myuser = User.objects.create_user(username=username,email=email,password=password)
        
        myuser.save()
        messages.success(request, "Sign Up Successful! Please login.")

        return redirect('user_login')
    return render(request,'usersignup.html')

@never_cache
@login_required(login_url='/user_login')
def user_logout(request):
    username = request.user.username
    logout(request)
    messages.success(request, f"Logout successful, {username}!")
   
    return redirect(user_login)

