from pydoc import describe
from django.db import models
from django.forms import CharField

class Job_notification(models.Model):
    id=models.CharField(max_length=500,primary_key=True);
    img=models.CharField(max_length=500,default='')
    company_name=models.CharField(max_length=100);
    posted_on=models.DateTimeField(null=True)
    job_title=models.CharField(max_length=200);
    designation=models.CharField(max_length=200);
    eligibility=models.CharField(max_length=200);
    experience=models.CharField(max_length=1000,default="");
    qualification=models.TextField();
    job_description=models.TextField();
    ctc=models.CharField(max_length=100,default='')
    last_date=models.CharField(max_length=100,default='')
    job_locations=models.CharField(max_length=1000);
    apply_link=models.CharField(max_length=500);
    official_website=models.CharField(max_length=500,default="");

class Company(models.Model):
    id = models.CharField(max_length=200,primary_key = True)
    name = models.CharField(max_length=20000)
    img = models.CharField(max_length=200,default='')

class Solution(models.Model):
    id = models.IntegerField(primary_key = True)
    title = models.CharField(max_length=100)
    description=models.CharField(max_length=2000,default="")
    input_format=models.CharField(max_length=2000,default="")
    output_format=models.CharField(max_length=2000,default="")
    sample_input=models.CharField(max_length=2000,default="")
    sample_output=models.CharField(max_length=2000,default="")
    code = models.CharField(max_length=2000,null=False)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,default=None)

class Course(models.Model):
    id=models.CharField(max_length=200,primary_key=True)
    name=models.CharField(max_length=200);
class Quiz(models.Model):
    id=models.IntegerField(primary_key=True)
    description=models.CharField(max_length=4000,default="")
    is_script=models.BooleanField(default=False)
    script=models.CharField(max_length=5000,default="",null=True,blank=True)
    choice1=models.CharField(max_length=200, default="")
    choice2=models.CharField(max_length=200,default="")
    choice3=models.CharField(max_length=200,default="")
    choice4=models.CharField(max_length=200,default="")
    correct_choice=models.CharField(max_length=200,default="")
    course=models.ForeignKey(Course,on_delete=models.CASCADE,default=None)