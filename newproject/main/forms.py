from .models import StyleCard
from django.forms import ModelForm, Textarea
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import User

class StyleCardForm(ModelForm):
    nameStyle = forms.CharField(widget=Textarea)
    class Meta:
        model = StyleCard
        fields = ['nameStyle', 'codeHTML', 'codeCSS', 'codeJS']


class SignupForm(UserCreationForm):
   class Meta:
       model = User
       fields = ("username", "email")
       field_classes = {'username': UsernameField}