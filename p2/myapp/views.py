from django.http import HttpResponse 
from datetime import datetime, timedelta
def datetime_offsets(request): 
    now = datetime.now() 
    offset_hours = 4
    four_hours_ahead = now + timedelta(hours=offset_hours) 
    four_hours_before = now - timedelta(hours=offset_hours)
    html = f"<html><body><h1>Current Date and Time with Offsets:</h1>" \
    f"<p>Current: {now}</p>" \
    f"<p>Four Hours Ahead: {four_hours_ahead}</p>" \
    f"<p>Four Hours Before: {four_hours_before}</p></body></html>" 
    return HttpResponse(html)