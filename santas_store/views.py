from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Letter

# Class-based View for the Home Page
class HomePage(TemplateView):
    """
    Displays the home page.
    """
    template_name = 'index.html'


# Function-based View: List View
def letter_list(request):
    """
    Displays a list of letters.
    """
    letters = Letter.objects.all()
    return render(request, 'letter_list.html', {'letters': letters})


# Function-based View: Detail View
def letter_detail(request, pk):
    """
    Displays the details of a single letter.
    """
    letter = get_object_or_404(Letter, pk=pk)
    return render(request, 'letter_detail.html', {'letter': letter})

from django import forms
from .models import Letter

class LetterForm(forms.ModelForm):
    """
    Form for creating or updating a Letter instance.
    """

    class Meta:
        model = Letter
        fields = '__all__'  # Use this to include all fields from the model
        # Alternatively, specify the fields explicitly:
        # fields = ['title', 'content', 'date']

        # Optional: Add widgets or labels if needed
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter content'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'title': 'Letter Title',
            'content': 'Letter Content',
            'date': 'Date',
        }
