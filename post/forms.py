from django.forms import fields
from .models import Comment, Contact
from django import forms

class CommmentForm(forms.ModelForm):
  #body = forms.CharField(label="", widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Text goes here!!!','rows':4, 'cols':50}))
  class Meta:
      model = Comment
      fields = ('name','body')


class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = ('name', 'email', 'message')
