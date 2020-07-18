from django.db import models

class Employee(models.Model):
    first_name=models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    company=models.CharField(max_length=20, blank=True)
    email=models.EmailField(blank=True)
    sal = models.IntegerField()
    loc=models.CharField(max_length=20)

    def __str__(self):
        return self.first_name
