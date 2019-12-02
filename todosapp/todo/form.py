from django import forms
from .models import List

class listform(forms.ModelForm):
    class Meta:
        model=List
        fields=["task","completed"]
