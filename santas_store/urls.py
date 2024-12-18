from django.urls import path
from .views import HomePage, letter_list, letter_detail

urlpatterns = [
    path('', HomePage.as_view(), name='home'),  # Home Page
    path('letters/', letter_list, name='letter_list'),  # List of Letters
    path('letters/<int:pk>/', letter_detail, name='letter_detail'),  # Detail View for a Letter
]
