from .models import CommentPost
from django.forms import ModelForm, Textarea
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentPost
        fields = ('name', 'email', 'body')
        widgets = {
          'body': Textarea(attrs={'rows':5, 'cols':90}),
        }
