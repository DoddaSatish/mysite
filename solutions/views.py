import base64
from django.shortcuts import render
from solutions.models import *
from django.forms.models import model_to_dict
from json import dumps
import random
def solution(request,id):
    var=Solution.objects.get(id=id)
    var.code=base64.b64decode(var.code).decode();
    #print(var.code)
    return render(request,'solution.html',{'solution':var})
def home(request):
    return render(request,'home.html');
def job_notifications(request ,id):
    var=Job_notification.objects.get(id=id)
    var.qualification = var.qualification.split('#')
    var.job_description = var.job_description.split('#')
    return render(request,'job_notifications.html',{'job_notification':var});
def jobNotifications(request):
    var = []
    for x in Job_notification.objects.order_by('posted_on')[::-1]:
        obj = model_to_dict(x)
        del obj['posted_on']
        var.append(obj)
    return render(request,'job_notifications_home.html',{'objects':dumps(var)})
def prev_coding_problems(request):
    var=[model_to_dict(x) for x in Company.objects.all() ]
    return render(request,'prev_coding_problems.html',{'objects':dumps(var)})
def coding_problems(request,id):
    company=Company.objects.get(id=id)
    problems = Solution.objects.all().filter(company=company)
    return render(request,'coding_problem.html',{'problems':problems})
def quiz(request,id):
    course = Course.objects.get(id=id)
    quiz = [model_to_dict(x) for x in Quiz.objects.filter(course=course)]
    random.shuffle(quiz)
    return render(request,'quiz.html',{'quiz':dumps(quiz),'course':course});


# Create your views here.
