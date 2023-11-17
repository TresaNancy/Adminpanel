from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from userlogin.models import UserProfile
from django.contrib.auth.models import User


# Create your views here.

def home(request):
     return render(request,'home.html')

@never_cache
def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        print(user)

        if user is not None and user.is_superuser:
            login(request, user)
            # messages.success(request, "Login successful.")
            return redirect('index')  
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'admin_login.html')


@never_cache
@login_required(login_url='/admin_login')
def index(request):
    
    # data = User.objects.select_related('user__userprofile').all().order_by('id')
    data = User.objects.all()
    context={"data":data}
   
    return render(request,'index.html',context)


def insert(request):

    if request.method =="POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        age = request.POST.get("first_name")
        password=request.POST.get("password")
        print(username,email,age)
        # query = Student(name=name, email= email,=age)
        query = User.objects.create_user(username =username,email=email,first_name=age,password=password)
        query.save()
        messages.info(request,"Data inserted successfully")
        return redirect("index")
    return render(request,'index.html')

@never_cache
@login_required(login_url='/admin_login')
def update(request,id):
    if request.method =="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        age = request.POST.get('first_name')
        print(username,email,"Get........")
        edit=User.objects.get(id=id)
        edit.username=username
        edit.email=email
        edit.first_name=age
       
        edit.save()
        print(edit,"SAVe........")
        messages.warning(request,"Data updated successfully")
        return redirect("index")

    d=User.objects.get(id=id)
    context = {"d":d}
    return render(request,'update.html',context)

def delete(request,id):
        d =User.objects.get(id=id)
        d.delete()
        messages.error(request,"Data deleted successfully")
        return redirect ("index")

def search_students(request):
    query = request.GET.get('q')  # Get the search query from the request
    
    if query:
        students = User.objects.filter(
            Q(id__icontains=query) |  # Search by ID
            Q(username__icontains=query) |  # Search by name
            Q(username__istartswith=query)  # Search by first name
        )
    else:
        students = User.objects.all()  # Display all students if no query
    
    return render(request, 'search_results.html', {'students': students, 'query': query})

@never_cache
@login_required(login_url='/admin_login')
def admin_logout(request):
    logout(request)
    return redirect("home")



    
       
        

