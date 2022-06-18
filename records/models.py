from django.db import models

# Create your models here.

class Cust_Info(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField
    Occupation = models.CharField(max_length=50)
    AmountPaid = models.IntegerField
    Room_Number = models.IntegerField
    NumberofNights = models.IntegerField
    StartDate = models.DateField()
    End_Date = models.DateField()

    def __str__(self):
        return self.Name