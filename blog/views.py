from django.shortcuts import render,HttpResponse,redirect
from . models import Blog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.
def home(request):
    post=Blog.objects.all()
    return render(request,'home.html',{'post':post})
def blog(request):
    post=Blog.objects.all()
    return render(request,'blog.html',{'post':post})
def shop(request):
    post=Blog.objects.all()
    return render(request,'shop.html',{'post':post})
def handleSearch(request):
    query=request.GET.get('Search')
    if not query:
        return HttpResponse("please enter the searched query")
    print(query)
    title=Blog.objects.filter(title__icontains=query)
    content=Blog.objects.filter(content__icontains=query)
    searcheddata=title.union(content)
    return render(request,'search.html',{'searched_data':searcheddata})

def handlelogin(request):
    if request.method=="POST":
        loginuser =request.POST['Username']
        loginpassword =request.POST['Password']
        user=authenticate(username=loginuser,password=loginpassword)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Invalid user or password ")
    return render(request,'login.html')    

def signup(request):
    if request.method=="POST":
        loginuser =request.POST['Username']
        loginpassword =request.POST['Password']
        user=authenticate(username=loginuser,password=loginpassword)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Invalid user or password ")
    return render(request,'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html', {'error': 'Invalid credentials'})
    return render(request, 'signin.html')


def handelogout(request):
    if request.method=="POST":
        logout(request)
        return redirect('login')
    else:
        return HttpResponse("404 not found")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')  # redirect to home page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def hello(request):
    post=Blog.objects.all()
    return render(request,'hello.html',{'post':post})
    




  





