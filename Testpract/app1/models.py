from django.db import models

class Oxygen(models.Model):
    Business_name=models.CharField(max_length=100)
    name=models.CharField(max_length=25)
    contact=models.BigIntegerField()
    address=models.CharField(max_length=200)
    Verifed_status=models.BooleanField(default=False)
    timestamp=models.TimeField()

    def __str__(self):
        return  self.Business_name





# Create your models here