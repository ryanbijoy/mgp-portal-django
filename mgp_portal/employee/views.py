from django.shortcuts import render, redirect
from .form import RegisterForm, EmployeeModel, LoginModel
from .models import Activity
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .choices import ACTIVITY_CHOICES
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
            user = User.objects.create_user(
                username=userformpost.cleaned_data["username"],
                email=userformpost.cleaned_data["email"],
                password=employeeformpost.cleaned_data["password"],
                first_name=userformpost.cleaned_data["first_name"],
                last_name=userformpost.cleaned_data["last_name"],
                is_active=False
            )

            employee = employeeformpost.save(commit=False)
            employee.user = user
            employee.save()

            messages.success(request, "Successfully Registered!")
            return redirect("/login")
        else:
            print(employeeformpost.errors)
            messages.warning(request, userformpost.errors)
            messages.warning(request, employeeformpost.errors)

    return render(request, "register.html", {"userform": userform, "employeeform": employeeform})


def user_login(request):
    if request.user and request.user.is_authenticated:
        return redirect("/dashboard")

    if request.method == "POST":
        loginform = LoginModel(request.POST)
        employeeform = EmployeeModel(request.POST)
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
        obj = Activity.objects.create(user=user, activity=activity, activity_at=timezone.now())
        messages.success(request, f"You Have Successfully {obj.activity}")
    return redirect("/login")


def redirect_to_homepage(request):
    return redirect("/login")


@login_required(login_url="/login")
def dashboard(request):
    username = request.user.username
    return render(request, "dashboard.html", {"name": username.capitalize(), "activity": ACTIVITY_CHOICES})
