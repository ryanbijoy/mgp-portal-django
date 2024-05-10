from django.contrib import admin
from .models import EmployeeDetails, Activity
# Register your models here.


@admin.register(EmployeeDetails)
class Employee(admin.ModelAdmin):
    list_display = ['id', "user", "mobile_number", "designation", "department"]


@admin.register(Activity)
class Activity(admin.ModelAdmin):
    list_display = ['id', "user", "activity", "activity_time"]
