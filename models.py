from django.db import models
from django.utils import timezone

class User(models.Model):
	email=models.CharField(max_length=30)
	password=models.CharField(max_length=20)

class Member(models.Model):
    
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    gender = models.CharField(max_length=10,default=False)
    mobile = models.CharField(max_length=15,default=False)
    email = models.CharField(max_length=30,default=False)
    star = models.CharField(max_length=20,default=False)
    rassi = models.CharField(max_length=20,default=False)
    fathername = models.CharField(max_length=20,default=False)
    mothername = models.CharField(max_length=20,default=False)
    fathercontact = models.CharField(max_length=15,default=False)
    religion = models.CharField(max_length=20,default=False)
    caste=models.CharField(max_length=20,default=False)
    lang = models.CharField(max_length=20,default=False)
    education = models.CharField(max_length=20,default=False)
    profession = models.CharField(max_length=20,default=False)
    country = models.CharField(max_length=20,default=False)
    state = models.CharField(max_length=20,default=False)
    pincode = models.CharField(max_length=10,default=False)
    address1 = models.CharField(max_length=60,default=False)
    address2 = models.CharField(max_length=60,default=False)
    height = models.CharField(max_length=20,default=False)
    weight = models.CharField(max_length=20,default=False)
    hobby = models.CharField(max_length=20,default=False)
    salary = models.CharField(max_length=20,default=False)
    family = models.CharField(max_length=20,default=False)
    work = models.CharField(max_length=40,default=False)
    image=models.ImageField(upload_to='pictures/',default=False)

    created_at = models.DateTimeField(auto_now=True)
    status=models.IntegerField(default=1)
    # last_login_lt=models.DateField(auto_now_add=True)
    
class Profile(models.Model):
	email=models.CharField(max_length=30)
	password=models.CharField(max_length=30)

class Offer(models.Model):
    name=models.CharField(max_length=30)
    validation=models.CharField(max_length=30)
    amount=models.CharField(max_length=30)
    requests=models.CharField(max_length=30,default=False)

class Story(models.Model):
    bridename=models.CharField(max_length=30,default=False)
    date=models.DateField(default=False)
    description=models.CharField(max_length=50,default=False,null=True)
    image=models.ImageField(upload_to="picture/")

class Exp(models.Model):
    name=models.CharField(max_length=30)
    type=models.CharField(max_length=30)
    amount=models.CharField(max_length=30,default=False)
    cashtype=models.CharField(max_length=30,default=False)
    remarks=models.CharField(max_length=30,default=False)



