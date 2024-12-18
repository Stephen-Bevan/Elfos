from django.contrib import admin
from .models import Letter

@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'creation_date', 'user')
    search_fields = ('name', 'title', 'text')