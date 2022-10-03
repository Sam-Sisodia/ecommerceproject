import email
import imp
from operator import imod
from . models import *

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.Form):
    name = forms.CharField()
    email =forms.EmailField()
    password1 = forms.CharField()
   # password2 = forms.CharField()


    
    def clean_name(self):    
        validatname = self.cleaned_data['name']
        if User.objects.filter(username=validatname).exists():
            raise forms.ValidationError("Username Already Exists")
        elif   len(validatname) <4 :
            raise forms.ValidationError("Enter more then 5 Charecter ")

        return validatname


    def clean_email(self):    
        validateemail = self.cleaned_data['email']
        if User.objects.filter(email=validateemail).exists():
            raise forms.ValidationError("Email already exist")
        return validateemail 
    

    


# class UserRegistrationForm(UserCreationForm):
#     pass

# class Userregform(forms.Form):
#     pass


# def clean_password (self):
#         pass1 = self.cleaned_data['password1']
#         pass2 = self.cleaned_data['password2']
#         pass
