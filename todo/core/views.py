from .models import ToDo
from django.shortcuts import render
from django.contrib import messages
from .forms import SignUpForm, AddTodoForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout

# Function to display the Home Page of the Website

def Home(request):
    todo = ToDo.objects.all()
    if request.user.is_authenticated:
        print('1')
        return render(request, 'core/home.html', {"todo":todo, "opreations" : True, 'needLog': True})
    print('0')
    return render(request, 'core/home.html', {"todo":todo, "opreations" : False, 'needLog': False })

# Function to Handle Singn Up 

def SignUp(request):
    if request.method == "POST":
        try:
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, "SignUp Successfuly!")
                return HttpResponseRedirect('/')
        except Exception as e:
            print(e.__str__())
            return render(request, 'core/signUp.html', {'form':fm})
    else:
        fm = SignUpForm()
    return render(request, 'core/signUp.html', {'form':fm})

# Function to Handle Log In 

def LogIn(request):
    fm = AuthenticationForm()
    if not request.user.is_authenticated:
        if request.method == "POST":
            try:
                fm = AuthenticationForm(request=request, data=request.POST)
                if fm.is_valid():
                    username = fm.cleaned_data['username']
                    password = fm.cleaned_data['password']
                    user = authenticate(username=username, password=password)
                    if user:
                        login(request=request, user=user)
                        messages.success(request, "LogIn Successfuly!")
                        return HttpResponseRedirect('/')
                    messages.error(request, "Please Enter Correct Credentials")
                return HttpResponseRedirect('/login/')
            except Exception as e:
                print(e.__str__())
                return render(request, 'core/logIn.html', {'form':fm})
        else:
            return render(request, 'core/logIn.html', {'form':fm})
    else:
        return HttpResponseRedirect('/')

# Function to Log Out the User

def LogOut(request):
    logout(request)
    return HttpResponseRedirect('/')

# Function to Let User Change the Password

def change_pass(request):
    if request.user.is_authenticated:
        fm = PasswordChangeForm(user=request.user)
        if request.method == "POST":
            try:   
                fm = PasswordChangeForm(user=request.user, data=request.POST)
                if fm.is_valid():
                    fm.save()
                    messages.success(request, "Password Changed Successfuly!")
                    return HttpResponseRedirect('/')
            except Exception as e:
                print(e.__str__())
                return render(request, 'core/changePass.html', {'form' : fm})
        else:
            return render(request, 'coer/changePass.html', {'form' : fm})
    return HttpResponseRedirect('/login/')

# Function to Add a new ToDoo

def AddToDo(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                frm = AddTodoForm(request, data=request.POST)
                if frm.is_valid():
                    frm.save()
                    messages.success(request, "ToDo Added Successfoly!")
                    return HttpResponseRedirect('/')
                messages.error(request, 'Something Went Wrong')
            except Exception as e:
                print(e.__str__())
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:   
        return HttpResponseRedirect('/')
