from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib import messages, auth



# Create your views here.
def index(request):
    return render(request,'index.html')

@never_cache
@login_required(login_url='/login')
def home(request):
    dict_users = {
        'users': User.objects.all()
    }
    return render(request,'home.html',dict_users)

@never_cache
def user_login(request):
   
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user= authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            messages.success(request, "Login successful.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request,'login.html')

def user_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username is taken.")
            return redirect("/signup")

        if User.objects.filter(email=email).exists():
            messages.info(request, "Email is already registered.")
            return redirect("/signup")

        myuser = User.objects.create_user(username=username,email=email,password=password)
        
        myuser.save()
        messages.success(request, "Sign Up Successful! Please login.")

        return redirect('login')
    return render(request,'signup.html')

@never_cache
@login_required(login_url='/login')
def user_logout(request):
    username = request.user.username
    logout(request)
    messages.success(request, f"Logout successful, {username}!")
   
    return redirect(user_login)

