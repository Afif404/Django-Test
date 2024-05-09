from django.contrib.auth.models import User
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.company})"
