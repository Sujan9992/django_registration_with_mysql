from email import message
from django.shortcuts import render
from .models import *

# Create your views here.
def registerPage(request):
    return render(request, 'app/register.html')

def userRegister(request):
    if request.method == 'POST':
        name = request.POST['Username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['cpassword']

        # validating user
        user = User.objects.filter(Email=email)

        if user:
            message = "User already exists"
            return render(request, 'app/register.html', {'message': message})
        else:
            if password == confirmPassword:
                user = User.objects.create(Name=name, Email=email, Password=password)
                user.save()
                message = "User registered successfully"
                return render(request, 'app/login.html', {'message': message})
            else:
                message = "Password and confirm password does not match"
                return render(request, 'app/register.html', {'message': message})

def loginView(requset):
    return render(requset, 'app/login.html')

def loginUser(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # checking email with database
        user = User.objects.get(Email=email)
        if user:
            if user.Password == password:
                # getting user data in session
                request.session['Username'] = user.Name
                request.session['Email'] = user.Email
                message = "User logged in successfully"
                return render(request, 'app/index.html', {'message': message})
            else:
                message = "Password is incorrect"
                return render(request, 'app/login.html', {'message': message})
        else:
            message = "User does not exist"
            return render(request, 'app/login.html', {'message': message})