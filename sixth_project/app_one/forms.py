from dataclasses import fields
from django import forms
from app_one.models import User

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'