from django.db import models

class Userdata(models.Model):
    fullname=models.CharField(max_length=250)
    about=models.TextField()
    email=models.CharField(max_length=250)
    mobile=models.IntegerField()
    skills=models.CharField(max_length=250)
    workexperience=models.TextField()
    education=models.CharField(max_length=250)
    certifications=models.CharField(max_length=250)
    projecttitle=models.CharField(max_length=250)
    projectdescription=models.TextField()
    projectlink=models.CharField(max_length=250)
