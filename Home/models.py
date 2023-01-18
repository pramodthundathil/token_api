from django.db import models

class PatientDetails(models.Model):
    
    Patient_Name = models.CharField(max_length=255)
    Patient_Phone = models.CharField(max_length = 12)
    Chair_Number = models.CharField(max_length=50)
    Treatment_Category = models.CharField(max_length=255)
    
class Tokens(models.Model):
    
    Token = models.CharField(max_length=10)
    Date = models.DateTimeField(auto_now_add=True)
    Patient = models.ForeignKey(PatientDetails,on_delete=models.CASCADE,null=True,blank=True)
    
    
    
