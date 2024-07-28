from django.urls import path
from .views import construct_csv_from_model, construct_pdf_from_model
urlpatterns = [
    path('csv/', construct_csv_from_model, name='construct_csv'), 
    path('pdf/', construct_pdf_from_model, name='construct_pdf'),
]