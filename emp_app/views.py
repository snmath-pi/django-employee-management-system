from django.shortcuts import render, HttpResponse
from .models import *
from datetime import datetime
# Create your views here.
def index(request):
    return render(request, 'index.html')
def all_emp(request):
    # emp = request.get.Objects.all()
    emps = Employee.objects.all()
    return render(request, "all_emp.html", {'emps':emps})
def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dept = request.POST.get('dept')
        salary = request.POST.get('salary')
        bonus = request.POST.get('bonus')
        role = request.POST.get('role')
        phone = request.POST.get('phone')
        
        # Check if any field is missing
        if not (first_name and last_name and dept and salary and bonus and role and phone):
            return HttpResponse('Missing fields. Please fill all fields.')
        
        # Convert fields to appropriate types
        salary = int(salary)
        bonus = int(bonus)
        role=int(role)
        dept=int(dept)
        phone = int(phone)
        
        new_emp = Employee(
            first_name=first_name,
            last_name=last_name,
            dept_id=dept,
            salary=salary,
            bonus=bonus,
            role_id=role,
            phone=phone,
            hire_date=datetime.now()
        )
        new_emp.save()
        return render(request, 'index.html')
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse('An Exception occurred')
def remove_emp(request, e_id=0):
    if e_id:
        try:
            emp_removed = Employee.objects.get(id=e_id)
            emp_removed.delete()
            return HttpResponse('Employee removed successfully')
        except Exception as e:
            return HttpResponse(e)
            
    emps = Employee.objects.all()
    return render(request, 'remove_emp.html',{'emps':emps})

def filter_emp(request):
    
    if request.method == 'POST':
        dept=request.POST['dept']
        role=request.POST['role']
        emps = Employee.objects.all()
        if dept:
            emps=emps.filter(dept_name=dept)
        if role:
            emps=emps.filter(role_name=role)
        return render(request, 'all_emp.html',{'emps':emps})
    
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception occurred')