from django.http import HttpResponse
from django.shortcuts import redirect, render

from core.forms import DepartmentForm, EmployeeForm
from core.models import Department, Employee
 

def dashboard(request):
    context = {
        "numbers":[1,2,3,4,5],
        "names" :["apple","Boy" ,"Cat"],
    }
    return render(request,"core/dashboard.html",context)


def home(request):
    message = "welcome home from views again"
    data ={"msg":message}
    return render(request,"core/home.html",data)


def testing(request):
    return render(request,"core/testing.html")

def get_departments(request):
    departments = Department.objects.all()
    data ={"depts": departments}
    return render(request,"core/departments.html",data)

def get_employees(request):
    employees = Employee.objects.all()
    data ={"empl": employees}
    return render(request,"core/employees.html",data)

def whatsmyname(request,name):
    context ={"name":name}
    return render(request,"core/hello.html",context)


def department_details(request,dept_id):
    departments = Department.objects.get(dept_id=dept_id)
    context ={"department":departments}
    return render(request,"core/department_details.html",context)

def employee_details(request,emp_name):
    employee = Employee.objects.get(emp_name=emp_name)
    context ={"employee":employee}
    return render(request,"core/employee_details.html",context)


def create_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect("core:departments")
    else:
        form =DepartmentForm()

    context ={"form":form}
    return render(request,"core/create_department.html",context)


def create_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect("core:employees")
    else:
        form =EmployeeForm()

    context ={"form":form}
    return render(request,"core/create_employee.html",context)