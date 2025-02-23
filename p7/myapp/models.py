from django.db import models
from django.forms import ModelForm
# Create your models here. 
class Course(models.Model):
    course_code=models.CharField(max_length=40) 
    course_name=models.CharField(max_length=100) 
    course_credits=models.IntegerField()
    def __str__ (self):
        return f"Course:{self.course_code.upper()}-{self.course_name}-{self.course_credits}"

class Student(models.Model): 
    student_usn=models.CharField(max_length=20) 
    student_name=models.CharField(max_length=100) 
    student_sem=models.IntegerField() 
    enrolment=models.ManyToManyField(Course)
    def __str__ (self):
        enrolled_courses = ", ".join(course.course_name for course in self.enrolment.all())
        return f"{self.student_usn} - {self.student_name} - Semester: {self.student_sem} - Enrolled in:{enrolled_courses}"
    
class Project(models.Model): 
    student=models.ForeignKey(Student,on_delete=models.CASCADE) 
    ptopic=models.CharField(max_length=200) 
    plangauges=models.CharField(max_length=200) 
    pduration=models.IntegerField()
    def __str__(self):
        return f"{self.student}--{self.ptopic}-{self.plangauges}-{self.pduration}"
    
class ProjectReg(ModelForm): 
    required_css_class="required" 
    class Meta:
        model=Student 
        fields=['student_usn','student_name','student_sem','enrolment']

class ProjectRegistration(ModelForm): 
    required_css_class="required"
    class Meta: 
        model=Project
        fields=['student','ptopic','plangauges','pduration']