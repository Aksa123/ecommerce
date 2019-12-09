from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from .forms import RegisterForm, ProfileEditForm
from .models import UserProfile
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login as authlogin, logout as authlogout
from django.contrib.auth.decorators import login_required

def signup(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                check_user = User.objects.get(email=form.cleaned_data.get('email'))     # email already exists !
                form = RegisterForm()
                email_warning = "Email already exist! Please use another email, or login."
                return render(request, "userauth/signup.html",context={"form": form, "email_warning": email_warning})

            except:
                name = form.cleaned_data.get('name')
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                gender = form.cleaned_data.get('gender')
                role = form.cleaned_data.get('role')

                new_user = User.objects.create_user(username=email, email=email, password=password)
                new_user.userprofile.name2 = name
                new_user.userprofile.gender = gender
                new_user.userprofile.role = role
                new_user.userprofile.save()

                return render(request, "userauth/login.html")
        else:
            return HttpResponse('form not valid')


    else:
        form = RegisterForm()
        return render(request, "userauth/signup.html",context={"form": form})

def login(request):

    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)        
        if user is not None:
            authlogin(request, user)
            # return HttpResponse(request.user.is_authenticated)
            return redirect('about:about')
        else:
            return HttpResponse("something's off")
    return render(request, "userauth/login.html")

def logout(request):
    if request.user.is_authenticated:
        authlogout(request)
        return redirect('about:about')
    else:
        return redirect('access-denied/login-required')


def profile(request):

    if request.method == 'POST':
        edit = ProfileEditForm(request.POST)

        if edit.is_valid():
            user_id = request.user.id
            user = User.objects.get(pk=user_id)

            name = edit.cleaned_data.get('name')
            gender = edit.cleaned_data.get('gender')
            role = edit.cleaned_data.get('role')
            money = edit.cleaned_data.get('money')

            user.userprofile.name2 = name
            user.userprofile.gender = gender
            user.userprofile.role = role
            user.userprofile.money = money
            user.userprofile.save()

            return render(request, "userauth/profile.html", context={"profile":edit, 'warning':'Profile has been saved!'})

        else:
            return render(request, "userauth/profile.html", context={"profile":edit, 'warning':'Input not valid!'})

    elif request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(pk=user_id)
        edit = ProfileEditForm(initial={'name':user.userprofile.name2, 'gender':user.userprofile.gender, 'role':user.userprofile.role, 'money':user.userprofile.money})

        return render(request, "userauth/profile.html", context={"profile":edit})


    else:
        HttpResponse("You need to login to access this page!")

    
def admin(request):

    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(pk=user_id)

        if user.userprofile.role == 'admin':
            return HttpResponse("do admin stuff")

        else:
            return redirect('access-denied/login-required')

    return HttpResponse("Login required!")

def access_denied(request, issue):

    if issue == "login-required":
        warning = "You must be logged in to access this page !"

        return render(request, "userauth/access_denied.html", context={
            "warning": warning
        })