from django.db import models 
class Course(models.Model):
    course_code=models.CharField(max_length=10) 
    course_name=models.CharField(max_length=30) 
    course_credits=models.IntegerField()
class Student(models.Model): 
    student_usn=models.CharField(max_length=20) 
    student_name=models.CharField(max_length=20) 
    student_sem=models.IntegerField() 
    enrolment=models.ManyToManyField(Course)