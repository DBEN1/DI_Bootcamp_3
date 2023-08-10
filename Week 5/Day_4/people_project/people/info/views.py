from django.shortcuts import render

# Create your views here.
def display_person(request):
    name = 'Bob Smith'
    age = 35
    country = 'USA'

response = f"Name: {person['name']}<br>Age: {person['age']}<br>Email: {person['email']}"
return HttpResponse(response)