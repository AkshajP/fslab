from django.http import HttpResponse 
from datetime import datetime
def current_datetime(request): 
    now = datetime.now()
    html = f"<html><body><h1>Current Date and Time:</h1><p>{now}</p></body></html>" 
    return HttpResponse(html)
