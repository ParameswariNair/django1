from django.shortcuts import render
from myapp1.models import project,project1 #project is the class in models
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def registration(request):
    if(request.POST):
        
     obj=project() #for registration
     obj.name=request.POST.get('name')
     obj.location = request.POST.get('location')
     obj.age = request.POST.get('age')
     obj.gender = request.POST.get('gender')
     obj.username = request.POST.get('username')
     obj.email = request.POST.get('email')
     obj.save()
     obj1=project1() #for login
     obj1.username= request.POST.get('username')
     obj1.password=  request.POST.get('username')
     obj1.role="user"
     obj1.save()

    return render(request,"registration.html")
def viewform(request):
    
    data=project.objects.all()
    return render(request,"viewform.html",{"data":data})
    
def login(request):
    data=""
    if(request.POST):
        obj1=project1()
        obj1.username = request.POST.get('username')
        obj1.password = request.POST.get('password')
        #print(obj1.username)
        request.session["sname"]=obj1.username
        data=project1.objects.get(username=obj1.username) 
        if(data.role=="user"):
            return HttpResponseRedirect("users")
    return render(request,"login.html",{"data":data})
def users(request):
    data=""
    obj1=project() 
    obj1.username=request.session.get("sname")
    data=project.objects.get(username=obj1.username)
    return render(request,"users.html",{"data":data})
def update(request):
    obj = project()
    obj.username =  request.GET.get('username')
    data = project.objects.get(username=obj.username)
    if(request.POST):

     
     data.name=request.POST.get('name')
     data.location = request.POST.get('location')
     data.age = request.POST.get('age')
     
     data.username = request.POST.get('username')
     data.email = request.POST.get('email')
     data.save()
     return HttpResponseRedirect("viewform")

    return render(request,"update.html",{"data":data})