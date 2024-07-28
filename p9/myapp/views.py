import csv
from django.http import HttpResponse 
from .models import Course
from reportlab.lib.pagesizes import letter 
from reportlab.pdfgen import canvas
def construct_csv_from_model(request): 
    courses = Course.objects.all()
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="courses_data.csv"' 
    writer = csv.writer(response)
    writer.writerow(["Course Name", "Course Code", "Credits"]) 
    for course in courses:
        writer.writerow([course.course_name, course.course_code, course.course_credits]) 
    return response

def construct_pdf_from_model(request): 
    courses = Course.objects.all()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="courses_data.pdf"'
    p = canvas.Canvas(response, pagesize=letter) 
    width, height = letter
    y = height - 50
    p.setFont("Helvetica", 12) 
    p.drawString(30, y, "Course Name") 
    p.drawString(200, y, "Course Code") 
    p.drawString(400, y, "Credits")
    y -= 20
    for course in courses:
        p.drawString(30, y, course.course_name) 
        p.drawString(200, y, course.course_code) 
        p.drawString(400, y, str(course.course_credits)) 
        y -= 20

    p.showPage() 
    p.save()
    return response