from django.shortcuts import render 
from .models import Course

def course_list(request): 
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def register_student(request, course_id): 
    print(course_id)
    course = Course.objects.get(pk=course_id) 
    if request.method == 'POST':
        name = request.POST.get('name') 
        email = request.POST.get('email')
        student, created = course.students.get_or_create(name=name, email=email) 
        if created:
            message = f'{student.name} registered successfully for {course.name}.' 
        else:
            message = f'{student.name} is already registered for {course.name}.'
        return render(request, 'registration_confirmation.html', {'message': message}) 
    return render(request, 'student_registration.html', {'course': course})

# def course_list(request): 
#     courses = [
#         {'id': 1, 'name': 'Introduction to Python', 'instructor': 'John Doe'},
#         {'id': 2, 'name': 'Web Development with Django', 'instructor': 'Jane Smith'},
#         {'id': 3, 'name': 'Data Science with Pandas', 'instructor': 'Alice Johnson'},
#         ]
#     return render(request, 'course_list.html', {'courses': courses})