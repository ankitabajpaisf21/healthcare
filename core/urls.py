from django.urls import path

from .views import dashboard, home, testing, get_departments,get_employees,whatsmyname,department_details,employee_details,create_department,create_employee
app_name ="core"


urlpatterns = [
    path('dashboard/', dashboard, name ='Dashboard-page'),
    path('home/', home, name ='Home-page'),
    path('testing/', testing, name ='testing'),
    path('departments/', get_departments, name ='departments'),
    path('employees/', get_employees, name ='employees'),
    path('hello/<str:name>', whatsmyname, name ='whatsmyname'),
    path('departments/<int:dept_id>', department_details, name ='department_details'),
    path('employees/<str:emp_name>', employee_details, name ='employee_details'),
    path('departments/create/', create_department, name ='create_department'),
    path('employees/create/', create_employee, name ='create_employee'),





]
