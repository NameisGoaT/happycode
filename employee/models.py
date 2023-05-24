from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name=models.CharField(max_length=100)
    emp_id=models.IntegerField(null=False)
    mobile_num=models.IntegerField()
    
    
