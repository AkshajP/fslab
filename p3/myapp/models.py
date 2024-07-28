from django.db import models 

class Fruit(models.Model):
    name = models.CharField(max_length=100)
    def str (self): 
        return self.name
    

class Student(models.Model):
    name = models.CharField(max_length=100) 
    event = models.CharField(max_length=100) 
    selected = models.BooleanField(default=False) 
        
    def str (self):
        return self.name