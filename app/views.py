from django.shortcuts import render,redirect,HttpResponse
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.contrib.auth import login, logout
from .forms import EmployeeForm
from .models import Professor,User

def home(request): #Home page
    # data  = {"msg":"test message"}
    if 'user' in request.session:
        print("===============================")
        user=request.session['user']
        return render(request,"home.html",{"user":user})
    return redirect("login")

def index(request): #Returnign Json Response
    data = {"location": "Inside app"}
    return JsonResponse(data)    

def name(request,name): #Dynamic Routing
    data = {"name": f"{name}"}
    return JsonResponse(data)  

def get(request): #How to retreive GET data
    data = request.GET
    return JsonResponse(data) 

def register(request): #user register 
    if request.method == "GET":
        return render(request, "register.html")
    if request.method == "POST":
        username = request.POST['username']
        user = User(
            username=username,
            password=request.POST['password'],
        )
        user.save()
        return redirect("login")

def login(request): #user login
    if request.method == "GET":
        if "user" not in request.session:
            return render(request, "login.html")
        return redirect("home")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username).first()
        status = user.check_password(password)
        if status == True:
            request.session['user'] = user.username
            return redirect("home")
        return render(request, "login.html")

def logout(request):#user logout 
    if request.method == "GET":
        if "user" not in request.session:
            return render(request, "login.html")
        del request.session['user']
        return redirect("login")
        
#C
def employee_form(request): # first method to save data form Form
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # You can define a success URL name in your urls.py
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})
#C
def employee_form2(request): # 2nd method to save data form Form
    if request.method == 'POST':
        data = request.POST
        employee = Professor(
            fname=data['fname'],
            lname=data['lname'],
            doj=data['doj'],
            contact=data['contact']
        )
        employee.save()
        return JsonResponse({"message":"Saved data"})
    else:
        return render(request, 'form.html')
#R    
def show(request): #Read Data from db
    if request.method == 'GET':
        data = request.GET.get('name')
        # professors = Professor.objects.all()
        # Filter professors by the given name
        professors = Professor.objects.filter(fname=data)
        lst = []
        # Print details of the matching professor(s)
        for professor in professors:
            print(professor.fname, professor.lname, professor.doj)
            data = {"fname":professor.fname,"lname":professor.lname,"doj":professor.doj}#Manual
            professor_dict = model_to_dict(professor) #Auto
            lst.append(professor_dict)
        return JsonResponse(lst,safe=False)    
        # return HttpResponse("ok")
#U
def update(request): #Update Data from DB
    if request.method == "GET":
        # id = request.GET.get("id") 
        name = request.GET.get("fname")
        newname = request.GET.get("name")
        # professor = Professor.objects.get(id=id) #GEt by id
        # professor = Professor.objects.filter(fname=name).first() #Update only first entry
        professors = Professor.objects.filter(fname=name) 
        for professor in professors:   #Update all entries
            professor.fname =   newname
            professor.save()
        return JsonResponse({"message":"OK"})   
#D        
def delete(request): #Delete data form db
    if request.method == "GET":
        id  = request.GET.get('id')
        name  = request.GET.get('name')
        if id:
            professor = Professor.objects.get(id=id)
            professor.delete()
            return JsonResponse({"msg":f"Deleted {professor.fname}"})
        if name:
            professors = Professor.objects.filter(fname=name) 
            # professors = Professor.objects.filter(fname=name).first() 
            lst = []
            for professor in professors:
                professor.delete()
                lst.append({"fname":professor.fname})
            return JsonResponse(lst,safe=False)
        return JsonResponse({"error":f"Invalid name or id"})
                
            
            
            
        