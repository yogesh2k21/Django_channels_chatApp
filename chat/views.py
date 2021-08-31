from django.shortcuts import render,redirect
from django.contrib.auth.models import User #django built in user model
from django.contrib.auth import authenticate,login,logout    #auth is authentication model in django
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            if username and password:
                user = authenticate(username=username,password=password)
                if user:
                    login(request,user)
                    messages.success(request, "Logged in Successfull.")
                    return redirect("index")
        return render(request,'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, "Logout Successfull.")
    return redirect('/login')

def signup_user(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password1 = request.POST['password1']
            email = request.POST['email']
            user = User.objects.create_user(username=username,email=email,password=password1)
            if user:
                messages.success(request, "Account created Successfull.")
                return redirect("login")
        return render(request,'signup.html',{}) 
    
def chat(request):
    return render(request,'chat.html',{})
