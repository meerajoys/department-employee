from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,CreateView,DetailView,UpdateView
from department.models import Employee,Department
from department.forms import EmployeeDetailForm,DepartmentDetailsForm,EmployeeUpdateForm
from django.urls import reverse_lazy



# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeDetailForm
    template_name = "emp-create.html"
    success_url = reverse_lazy("home")

class EmployeeListView(ListView):
    model = Employee
    context_object_name = "emplist"
    template_name = "emp-list.html"

    # def get_queryset(self):
    #     return Employee.objects.filter(department=self.request.user)

class EmployeeDetailsView(DetailView):
    model = Employee
    context_object_name = "emp"
    template_name = "emp-details.html"
    pk_url_kwarg = "id"

class EmployeeEditView(UpdateView):
    model = Employee
    template_name = "emp-edit.html"
    form_class = EmployeeUpdateForm
    success_url =reverse_lazy("emp-list")
    pk_url_kwarg = "id"


def deleteEmp(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("emp-list")



class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentDetailsForm
    template_name = "dept-create.html"
    success_url = reverse_lazy("home")

class DepartmentListView(ListView):
    model = Department
    context_object_name = "dept"
    template_name = "dept-list.html"


class DepartmentEmployeesListView(ListView):
    model = Employee
    context_object_name = "dep_emp"
    template_name = "dep-emp.html"


    def get_queryset(self):
        dname=self.kwargs.get("d_name")
        return Employee.objects.filter(department__dname=dname)





