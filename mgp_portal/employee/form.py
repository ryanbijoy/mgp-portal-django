from .models import User, EmployeeDetail
from django import forms
from django.contrib.auth import password_validation


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
        labels = {
            "username": "Username",
            "email": "Email",
            "first_name": "First Name",
            "last_name": "Last Name",
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        placeholders = {
            "username": "Enter Username",
            "email": "Enter Email",
            "first_name": "Enter First Name",
            "last_name": "Enter Last Name",
        }

        for field_name, field in self.fields.items():
            field.widget.attrs["placeholder"] = placeholders.get(field_name, "")
            field.widget.attrs["class"] = "form-control"

            if field_name in self.Meta.labels:
                field.label = self.Meta.labels[field_name]


class EmployeeModel(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}), label="Confirm Password")

    class Meta:
        model = EmployeeDetail
        exclude = ("user",)

        labels = {
            "designation": "Designation",
            "department": "Department",
            "mobile_number": "Mobile Number",
            "password": "Password",
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeModel, self).__init__(*args, **kwargs)

        placeholders = {
            "designation": "Enter Designation",
            "department": "Enter Department",
            "mobile_number": "Enter Mobile Number",
            "password": "Enter Password",
            "password2": "Enter Confirm Password",
        }

        for field_name, field in self.fields.items():
            field.widget.attrs["placeholder"] = placeholders.get(field_name, "")
            field.widget.attrs["class"] = "form-control"

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        re_password = cleaned_data.get("password2")

        # password validation
        if password != re_password:
            raise forms.ValidationError({"password": ["Passwords does not match"]})

        if password == None:
            raise forms.ValidationError({"password": ["Password can't be empty"]})
        try:
            password_validation.validate_password(password=password)
        except forms.ValidationError as error:
            raise forms.ValidationError({"password": error})


class LoginModel(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username", "class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", "class": "form-control"}))
    latitude = forms.FloatField(widget=forms.HiddenInput())
    longitude = forms.FloatField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(LoginModel, self).__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['password'].label = ""
