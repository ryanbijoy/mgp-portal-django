from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from .choices import ACTIVITY_CHOICES


# Create your models here.
class EmployeeDetail(models.Model):
    user = models.OneToOneField(User, related_name="user_employee_detail", on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    mobile_number = models.BigIntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)])
    department = models.CharField(max_length=100)


class Activity(models.Model):
    user = models.ForeignKey(User, related_name="user_activity", on_delete=models.CASCADE)
    activity = models.CharField(max_length=100, choices=ACTIVITY_CHOICES)
    activity_at = models.DateTimeField()
