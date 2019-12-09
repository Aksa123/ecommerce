from django import forms
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver




class RegisterForm(forms.Form):

    gender_choices = [('male', "Male"), ('female', 'Female')]
    role_choices = [('admin', 'Admin'), ('normal', 'Normal User')]

    name = forms.CharField(label="Username", max_length=100, widget=forms.TextInput(attrs={"class":"form-control mr-sm-2"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class":"form-control mr-sm-2", "placeholder":"Email..."}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class":"form-control mr-sm-2", "placeholder":"Password..."}))
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=gender_choices)
    role = forms.ChoiceField(widget=forms.RadioSelect, choices=role_choices)


class ProfileEditForm(forms.Form):
    gender_choices = [('male', "Male"), ('female', 'Female')]
    role_choices = [('admin', 'Admin'), ('normal', 'Normal User')]

    name = forms.CharField(label="Username", max_length=100, initial="", widget=forms.TextInput(attrs={"class":"form-control mr-sm-2"}))
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=gender_choices, initial="")
    role = forms.ChoiceField(widget=forms.RadioSelect, choices=role_choices, initial="")
    money = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.00, widget=forms.NumberInput(attrs={"class":"form-control mr-sm-2"}))
