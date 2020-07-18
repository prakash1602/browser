from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

def makeentry(request):
    if request.method =="POST":
        fname1 = request.POST.get('fname')
        lname1 = request.POST.get('lname')
        salary1 = request.POST.get('salary')
        email1 = request.POST.get('email')
        location1 = request.POST.get('location')
        company1 = request.POST.get('company')

        data = Employee(
            first_name=fname1,
            last_name=lname1,
            sal=salary1,
            email=email1,
            loc=location1,
            company=company1
        )
        data.save()
        return render(request, 'makeentryfile.html')
    else:
        return render(request,'makeentryfile.html')

def index(request):
    response=HttpResponse()
    response.write("<html><body>\n")
    response.write("<h1>Employees Details</h1>")
    response.write("<hr>")
    elist=Employee.objects.all()
    for e in elist:
        link="<a href=\'browserapp\info\%d\'>"%(e.id)

        response.write("%s<li>%s &nbsp %s</a></li>"
        %(link,e.first_name,e.last_name))

        response.write("<br></body></html>")
    return response

def details(request,eid=0):
    response=HttpResponse()
    response.write("<html><body>\n")
    try:
        e=Employee.objects.get(id=eid)
        response.write("<h1>Details for Employee %s</h1><hr>\n"%e.first_name)
        response.write("<li>First Name:%s</li><br>"%e.first_name)
        response.write("<li>Last Name:%s</li><br>"%e.last_name)
        response.write("<li>Company:%s</li><br>"%e.company)
        response.write("<li>Location:%s</li><br>"%e.loc)
        response.write("<li>Salary:%s</li><br>"%e.sal)
    except Employee.DoesNotExist:response.write("Employee Not Found")
    response.write("</body></html>")
    return response