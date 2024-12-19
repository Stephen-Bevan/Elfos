from django.db import models

from django.db import models
from django.contrib.auth.models import User


# Clinet Model
class Letter(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='letters'
        )

    def __str__(self):
        return self.name