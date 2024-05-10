from .models import User, EmployeeDetails
from django import forms
from django.contrib.auth import password_validation


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password", "password2"]
        labels = {
            "username": "Username",
            "email": "Email",
            "first_name": "First Name",
            "last_name": "Last Name",
            "password": "Password",
            "password2": "Confirm Password",
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        placeholders = {
            "username": "Enter Username",
            "email": "Enter Email",
            "first_name": "Enter First Name",
            "last_name": "Enter Last Name",
            "password": "Enter Password",
            "password2": "Enter Confirm Password",
        }

        for field_name, field in self.fields.items():
            field.widget.attrs["placeholder"] = placeholders.get(field_name, "")
            field.widget.attrs["class"] = "form-control"

            if field_name in self.Meta.labels:
                field.label = self.Meta.labels[field_name]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        re_password = cleaned_data.get("password2")

        ## password validation
        if password != re_password:
            raise forms.ValidationError({"password": ["Passwords does not match"]})

        if password == None:
            raise forms.ValidationError({"password": ["Password can't be empty"]})
        try:
            password_validation.validate_password(password=password)
        except forms.ValidationError as error:
            raise forms.ValidationError({"password": error})


class EmployeeModel(forms.ModelForm):
    class Meta:
        model = EmployeeDetails
        exclude = ("user",)

        labels = {
            "designation": "Designation",
            "department": "Department",
            "mobile_number": "Mobile Number",
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeModel, self).__init__(*args, **kwargs)

        placeholders = {
            "designation": "Enter Designation",
            "department": "Enter Department",
            "mobile_number": "Enter Mobile Number",
        }

        for field_name, field in self.fields.items():
            field.widget.attrs["placeholder"] = placeholders.get(field_name, "")
            field.widget.attrs["class"] = "form-control"


class LoginModel(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username", "class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", "class": "form-control"}))
    latitude = forms.FloatField(widget=forms.HiddenInput())
    longitude = forms.FloatField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(LoginModel, self).__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['password'].label = ""
