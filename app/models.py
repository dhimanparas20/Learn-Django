#For more help read : 'https://www.freecodecamp.org/news/common-django-model-fields-and-their-use-cases/'
from django.db import models
from django.contrib.auth.hashers import make_password,check_password

class Professor(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    doj = models.DateField()
    contact = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return self.fname
    

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=6)
    professor = models.OneToOneField(Professor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)
        
    def check_password(self, raw_password):
        # Check if the provided password matches the hashed password
        return check_password(raw_password, self.password)    