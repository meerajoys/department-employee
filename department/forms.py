from django import forms
from department.models import Employee,Department
from django import forms
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())

class EmployeeDetailForm(forms.ModelForm):
    class Meta:
        model=Employee

        fields = "__all__"
        widgets = {
            'ename': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs={"class":"form-control"}),
            'phone':forms.TextInput(attrs={"class":"form-control"}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            # 'department': forms.TextInput(attrs={'class': 'form-control'})

        }


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields = "__all__"
        widgets = {
            'ename': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'phone': forms.TextInput(attrs={"class": "form-control"}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            # 'department': forms.TextInput(attrs={'class': 'form-control'})

        }
class DepartmentDetailsForm(forms.ModelForm):
    class Meta:
        model=Department

        fields = "__all__"
        widgets = {
            'dname': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }