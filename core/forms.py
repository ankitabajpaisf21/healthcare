from django import forms

from .models import Department, Employee

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields =["dept_id","dept_name","location"]

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields =["emp_id","emp_name","job","manager_id","hire_date","salary","comm" ,"dept_id"]        




          