from django.contrib import admin
from .models import Course, Project, Student 
admin.site.register(Project)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("course_name", "course_code", "course_credits",)
admin.site.register(Course, MemberAdmin) 
class MyAdmin(admin.ModelAdmin):
    list_display = ("student_name", "student_usn", "student_sem",) 
admin.site.register(Student, MyAdmin)