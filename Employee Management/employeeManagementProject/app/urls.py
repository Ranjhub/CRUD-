from django.urls import path
from .views import *

urlpatterns = [
     path('', index,),
    path('home/',HomePage),
    path('addEmployeeData/',AddEmployee),
    path('viewEmployeeData/',ViewEmployee),
    path('filter/',Filter, name='filter_access'),
    path('Employees/delete/<int:id>/',Delete_Employee, name='Employee_delete'),
    path('Employees/update/<int:id>/',Employee_update, name='Employee_update'),
]
