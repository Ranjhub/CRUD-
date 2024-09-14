from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
def index(request):
    return render(request,'home.html')

def HomePage(request):
    return render(request,'home.html')


def AddEmployee(request):
    context = { 'Employee': Employee_Form() }
    if request.method == 'POST':
        employee_form = Employee_Form(request.POST)
        
        if employee_form.is_valid():
            employee_form.save()        
    return render (request, 'addEmp.html', context)



def ViewEmployee(request):
    context ={
        "all_Employee" : Employee.objects.all()
     }
    
    return render(request, 'viewEmp.html', context)



def Delete_Employee(request, id):
    selected_data = Employee.objects.get(id=id)
    selected_data.delete() 
    return redirect('/viewEmployeeData/')



def Employee_update(request, id):
    selected_Employee = Employee.objects.get(id=id)
    context = {
        'Employee_update': Employee_Form(instance=selected_Employee)
    }

    if request.method == "POST":
        employee = Employee_Form(request.POST,instance=selected_Employee)
        if employee.is_valid():
            employee.save()
            return redirect('/viewEmployeeData/')

    return render(request, 'updateEmp.html', context)

def Filter(request):
    filter1=request.GET.get('search')
    filter2=Employee.objects.all()
    if filter1:
        try:
            department = filter1
            filter2=Employee.objects.filter(Employee_department__icontains=department) or Employee.objects.filter(Employee_position__icontains=department )
        except:
            pass
    context={'all_Employee':filter2}
        # 
        # ValueError:
        #     filter2=Employee.objects.filter(product_name__icontains=filter1)
            
    return render(request,'viewEmp.html',context)