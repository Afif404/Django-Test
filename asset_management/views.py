from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Company, Employee, Device, DeviceAssignment
from .forms import CompanyForm, EmployeeForm, DeviceForm, DeviceAssignmentForm

# Company Views (admin only)
@login_required
def company_list(request):
    if request.user.is_superuser:
        companies = Company.objects.all()
        #return render(request, 'asset_tracking/company_list.html', {'companies': companies})
    else:
        return redirect('home')

@login_required
def company_create(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CompanyForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('company_list')
        else:
            form = CompanyForm()
        #return render(request, 'asset_tracking/company_create.html', {'form': form})

@login_required
def company_edit(request, pk):
    if request.user.is_superuser:
        company = get_object_or_404(Company, pk=pk)
        if request.method == 'POST':
            form = CompanyForm(request.POST, instance=company)
            if form.is_valid():
                form.save()
                return redirect('company_list')
        else:
            form = CompanyForm(instance=company)
        #return render(request, 'asset_tracking/company_edit.html', {'form': form})

# Employee Views (consider user roles and permissions)
@login_required
def employee_list(request):
    # Filter employees based on user role (if applicable)
    employees = Employee.objects.all()  # Replace with filtered query if needed
    #return render(request, 'asset_tracking/employee_list.html', {'employees': employees})

@login_required
def employee_create(request):
    # Restrict access based on user role (if applicable)
    if request.user.is_superuser:  # Replace with permission check
        if request.method == 'POST':
            form = EmployeeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('employee_list')
        else:
            form = EmployeeForm()
        #return render(request, 'asset_tracking/employee_create.html', {'form': form})
    else:
        return redirect('home')  # Or display appropriate message

@login_required
def employee_edit(request, pk):
    # Restrict access based on user role (if applicable)
    employee = get_object_or_404(Employee, pk=pk)
    if request.user.is_superuser or request.user == employee.user:  # Replace with permission check
        if request.method == 'POST':
            form = EmployeeForm(request.POST, instance=employee)
            if form.is_valid():
                form.save()
                return redirect('employee_list')
        else:
            form = EmployeeForm(instance=employee)
        #return render(request, 'asset_tracking/employee_edit.html', {'form': form})



#commented out the html rendering parts as i dont have any frontend
    
