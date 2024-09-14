from django.db import models

class Employee(models.Model): 
    
    Employee_name = models.CharField(max_length=200, null=True)
    Employee_position = models.CharField(max_length=200, null= True)
    Employee_department = models.CharField(max_length=200)
    Employee_salary = models.IntegerField()
    
    
    def __str__(self):
        return self.Employee_title
