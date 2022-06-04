import base64
from django.shortcuts import render
from solutions.models import *
def solution(request,id):
    var=Solution.objects.get(id=id)
    var.code=base64.b64decode(var.code).decode();
    #print(var.code)
    return render(request,'solution.html',{'solution':var})
def home(request):
    return render(request,'home.html');
def job_notifications(request ,id):
    var=Job_notification.objects.get(id=id)
    var.qualification = var.qualification.split(',')
    var.job_description = var.job_description.split(',')
    return render(request,'job_notifications.html',{'job_notification':var});
def jobNotifications(request):
    var=Job_notification.objects.all()
    return render(request,'job_notifications_home.html',{'objects':var})


# Create your views here.
