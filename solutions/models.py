from django.db import models

# Create your models here.
class Solution(models.Model):
    id = models.IntegerField(primary_key = True)
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=2000,null=False)
class Job_notification(models.Model):
    id=models.CharField(max_length=500,primary_key=True);
    img=models.CharField(max_length=500,default='')
    company_name=models.CharField(max_length=100);
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