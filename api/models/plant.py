from django.db import models
from django.contrib.auth import get_user_model

class Plant(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    author = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"The {self.name} plant costs ${self.price}"