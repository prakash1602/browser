from django.contrib import admin
from .models import Employee
class AdminEmployee(admin.ModelAdmin):
    list_display = ["first_name",
                    "last_name",
                    "company",
                    "loc",
                    "email",
                    "sal"]
admin.site.register(Employee,AdminEmployee)
