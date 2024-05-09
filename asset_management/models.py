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
    
class Device(models.Model):
    DEVICE_TYPE_CHOICES = (
        ('LAPTOP', 'Laptop'),
        ('PHONE', 'Phone'),
        ('TABLET', 'Tablet'),
        ('OTHER', 'Other'),
    )
    DEVICE_CONDITION_CHOICES = (
        ('NEW', 'New'),
        ('USED', 'Used'),
        ('FOR_REPAIR', 'For Repair'),
    )

    type = models.CharField(max_length=10, choices=DEVICE_TYPE_CHOICES)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    condition = models.CharField(max_length=20, choices=DEVICE_CONDITION_CHOICES, default='NEW')

    def __str__(self):
        return f"{self.type} - {self.brand} {self.model} ({self.serial_number})"

class DeviceAssignment(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checked_out_date = models.DateField(auto_now_add=True)
    checked_in_date = models.DateField(blank=True, null=True)
    condition_on_checkout = models.CharField(max_length=20, choices=Device.DEVICE_CONDITION_CHOICES)
    condition_on_return = models.CharField(max_length=20, choices=Device.DEVICE_CONDITION_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.device} assigned to {self.employee.name} (Checked Out: {self.checked_out_date})"
