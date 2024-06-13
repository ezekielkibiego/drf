from django.db import models

class State(models.Model):
    state_name = models.CharField(max_length=50)
    state_abbrev = models.CharField(max_length=2)
    region = models.CharField(50)
    division = models.CharField(max_length=50)
    
    def __str__(self):
        return self.state_name, self.state_abbrev
    
    
class Person(models.Model):
    id_number = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50, null=True)
    state_code = models.CharField(max_length=2)
    shirt_or_hat = models.CharField(max_length=50, null=True )
    quiz_points = models.IntegerField(null=True) 
    team = models.CharField(max_length=50, null=True)
    signup = models.DateField()
    age = models.IntegerField()
    company = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'