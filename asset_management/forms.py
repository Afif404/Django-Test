from django import forms
from .models import Company, Employee, Device, DeviceAssignment

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'

class DeviceAssignmentForm(forms.ModelForm):
    class Meta:
        model = DeviceAssignment
        fields = ['device', 'employee', 'condition_on_checkout']

        def clean(self):
            cleaned_data = super().clean()
            device = cleaned_data.get('device')
            # Check if device is already assigned
            if device.deviceassignment_set.filter(checked_in_date__isnull=True).exists():
                raise forms.ValidationError('This device is already assigned to someone.')
            return cleaned_data