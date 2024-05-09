from django.contrib import admin
from .models import Company, Employee, Device, DeviceAssignment

# Register your models with the admin site
admin.site.register(Company)
admin.site.register(Employee)

