from django.db import models

# Create your models here.



class Department(models.Model):
    dname=models.CharField(max_length=120,null=False)
    description=models.CharField(max_length=120)
    def __str__(self):
        return self.dname



class Employee(models.Model):
    ename=models.CharField(max_length=120)
    designation=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    phone=models.CharField(max_length=20)
    address=models.CharField(max_length=120)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.ename




