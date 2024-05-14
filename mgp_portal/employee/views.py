from django.shortcuts import render, redirect
from .form import RegisterForm, EmployeeModel, LoginModel
from .models import Activity
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .geolocation import geofencing

# Create your views here.


def register(request):
    if request.user and request.user.is_authenticated:
        return redirect("/dashboard")

    userform = RegisterForm()
    employeeform = EmployeeModel()

    if request.method == "POST":
        userformpost = RegisterForm(request.POST)
        employeeformpost = EmployeeModel(request.POST)

        if userformpost.is_valid() and employeeformpost.is_valid():
            user = userformpost.save(commit=False)
            user.is_active = False
            user.save()

            employee = employeeformpost.save(commit=False)
            employee.user = user
            employee.save()

            messages.success(request, "Successfully Registered!")
            return redirect("/login")

    return render(request, "register.html", {"userform": userform, "employeeform": employeeform})


def user_login(request):
    if request.user and request.user.is_authenticated:
        return redirect("/dashboard")

    if request.method == "POST":
        loginform = LoginModel(request.POST)
        if loginform.is_valid():
            username = loginform.cleaned_data["username"]
            password = loginform.cleaned_data["password"]
            latitude = loginform.cleaned_data["latitude"]
            longitude = loginform.cleaned_data["longitude"]

            if geofencing(latitude, longitude):
                user = authenticate(username=username, password=password)
                if user and user.is_active:
                    login(request, user)
                    return redirect("/dashboard")
                else:
                    messages.warning(request, "Invalid Username or Password")
            else:
                messages.error(request, "You Need To Get Closer To The Office!")
    else:
        loginform = LoginModel()

    return render(request, "loginpage.html", {"loginform": loginform})


@login_required(login_url="/login")
def user_logout(request):
    if request.user and request.user.is_authenticated:
        user = request.user
        logout(request)
        activity = request.POST["activity"]
        Activity.objects.create(user=user, activity=activity, activity_time=timezone.now())
        messages.success(request, f"You Have Successfully {activity}")
    return redirect("/login")


def redirect_to_homepage(request):
    return redirect("/login")


@login_required(login_url="/login")
def dashboard(request):
    return render(request, "dashboard.html")
