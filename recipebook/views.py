from django.shortcuts import render,redirect
from recipebook.models import recipes
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here
@login_required(login_url="/signup/")
def recipe(request):
    if request.method=="POST":
        data=request.POST
        title=data.get("title")
        description=data.get("description")
        recipe_image=request.FILES.get("img")
        time=data.get("created_at")
        
        recipes.objects.create(title=title,description=description,image=recipe_image,created_at=time)
        return redirect('/recipe/')
    queryset=recipes.objects.all()
    if request.GET.get('search'):
        
        queryset=queryset.filter(title__icontains=request.GET.get("search"))
    
    
    context={'recipe':queryset}
    return render(request,"index.html",context)

@login_required(login_url="/signup/")
def delete(request,id):
    queryset=recipes.objects.get(id = id)
    queryset.delete()
    return redirect('/recipe/')
@login_required(login_url="/signup/")
def update(request,id):
    queryset=recipes.objects.get(id = id)
    if request.method=="POST":
        data =request.POST
        title=data.get("title")
        description=data.get("description")
        recipe_image=request.FILES.get("img")
        
        queryset.title=title
        queryset.description=description
        if recipe_image:
            queryset.image=recipe_image
        queryset.save()
        return redirect('/recipe/')
    context={'a':queryset}
    
    return render(request,"update.html",context)

def signup(request):
    if request.method=="POST":
       
        name=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        
        user=User.objects.filter(username=name)
        messages.info(request,"username already taken")
        if user.exists():
            return redirect('/signup/')
            
        data=User.objects.create(username=name,email=email)
        data.set_password(password)
        data.save()
        messages.error(request,'account create successfully')
        return redirect("/")
    return render(request,'signup.html')

def login_page(request):
    if request.method =="POST":
        username= request.POST.get('username')
        password=request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request,"username doesn't not exist create account first!")
            return redirect('/login/')
        
        user = authenticate(username=username,password=password)
        
        if user is None:
            messages.error(request,"invalid password")
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/recipe/')
    
    return render(request,"login.html")

def logout_page(request):
    logout(request)
    return redirect('/login/')