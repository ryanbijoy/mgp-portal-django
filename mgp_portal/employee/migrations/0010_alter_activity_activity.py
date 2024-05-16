# Generated by Django 5.0.6 on 2024-05-16 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employee", "0009_alter_activity_activity_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="activity",
            name="activity",
            field=models.CharField(
                choices=[("punch_in", "Start My Day"), ("punch_out", "End My Day")],
                max_length=100,
            ),
        ),
    ]
