#For more help read : 'https://www.freecodecamp.org/news/common-django-model-fields-and-their-use-cases/'
from django.db import models
from django.core.validators import MaxValueValidator

class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MaxValueValidator(150)])
    contact = models.CharField(max_length=10, unique=True)
    isonline = models.BooleanField(default=False)
    type = models.CharField(max_length=100,choices=(("admin","admin"),("normal","normal"),("pro","pro")),default="normal")
    added_date = models.DateTimeField(auto_now=True)
    # updated_date =models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
