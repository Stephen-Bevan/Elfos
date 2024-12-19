from django import forms
from .models import Letter

class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = ["text"]  # Only include the 'text' field in the form
        widgets = {
            "text": forms.Textarea(attrs={"class": "form-control", "placeholder": "Write your letter here..."}),
        }