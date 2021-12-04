from django.forms import fields
from .models import Comment, Contact
from django import forms

class CommmentForm(forms.ModelForm):
  class Meta:
      model = Comment
      fields = ('name','body')


class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = ('name', 'email', 'message')