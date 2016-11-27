from django import forms
from .models import Users

class Users(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name']
