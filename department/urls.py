from django.urls import path
from department import views


urlpatterns=[
    path("home",views.HomePageView.as_view(),name="home"),
    path("emp/create",views.EmployeeCreateView.as_view(),name="emp-create"),
    path("emp/list",views.EmployeeListView.as_view(),name="emp-list"),
    path("emp/edit/<int:id>",views.EmployeeEditView.as_view(),name="emp-edit"),
    path("emp/delete/<int:id>",views.deleteEmp,name="emp-delete"),
    path("dept/create",views.DepartmentCreateView.as_view(),name="dept-create"),
    path("dept/list",views.DepartmentListView.as_view(),name="dept-list"),
    path("emp/detail/<int:id>",views.EmployeeDetailsView.as_view(),name="emp-details"),
    path("dep/emplist/<str:d_name>",views.DepartmentEmployeesListView.as_view(),name="dep-emplist")
]