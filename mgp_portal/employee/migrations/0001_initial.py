# Generated by Django 5.0.6 on 2024-05-08 13:30

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Activity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("activity", models.CharField(max_length=100)),
                ("activity_time", models.DateTimeField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_activity",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EmployeeDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("designation", models.CharField(max_length=100)),
                (
                    "mobile_number",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1000000000),
                            django.core.validators.MaxValueValidator(9999999999),
                        ]
                    ),
                ),
                ("department", models.CharField(max_length=100)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_employee_detail",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
