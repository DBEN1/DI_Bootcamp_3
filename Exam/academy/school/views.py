from django.shortcuts import render
from .models import Course

def course_details(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'course_details.html', {'course': course})
def home(request):
    return render(request, 'home.html')