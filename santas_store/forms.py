from django import forms
from .models import Letter

class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = ["name", "title", "text"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your Name"}),
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Letter Title"}),
            "text": forms.Textarea(attrs={"class": "form-control", "placeholder": "Write your letter here..."}),
        }