from django import forms
from .models import Blog , comment


class commentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['comment']
