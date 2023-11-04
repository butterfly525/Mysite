from .models import StyleCard
from django.forms import ModelForm, Textarea
from django import forms

class StyleCardForm(ModelForm):
    nameStyle = forms.CharField(widget=Textarea)
    class Meta:
        model = StyleCard
        fields = ['nameStyle', 'codeHTML', 'codeCSS', 'codeJS']

