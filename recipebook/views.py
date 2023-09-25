from django.shortcuts import render,redirect
from recipebook.models import recipes
from django.http import HttpResponse
# Create your views here
def recipe(request):
    
    if request.method=="POST":
        data=request.POST
        title=data.get("title")
        description=data.get("description")
        recipe_image=request.FILES.get("img")
        time=data.get("created_at")
        
        recipes.objects.create(title=title,description=description,image=recipe_image,created_at=time)
        
        return redirect('/')
    queryset=recipes.objects.all()
    if request.GET.get('search'):
        
        queryset=queryset.filter(title__icontains=request.GET.get("search"))
    
    
    context={'recipe':queryset}
    return render(request,"index.html",context)

def delete(request,id):
    queryset=recipes.objects.get(id = id)
    queryset.delete()
    return redirect('/')

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
        return redirect('/')
    context={'a':queryset}
    
    return render(request,"update.html",context)
    