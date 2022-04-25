from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Drugs(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    disease = models.CharField(max_length=100)
    symptoms = models.TextField(max_length=400)
    time = models.DateTimeField(auto_now_add=True)
    drug_type = models.CharField(max_length=100)
    prescription = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name
