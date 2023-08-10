from django.shortcuts import render
from django.http import HttpResponse
from .data import animals, families

def display_all_animals(request):
    response = ""
    for animal in animals:
        response += f"Name: {animal['name']}, Legs: {animal['legs']}, Weight: {animal['weight']}kg, Height: {animal['height']}cm, Speed: {animal['speed']}km/h<br>"
    return HttpResponse(response)

def display_all_families(request):
    response = ", ".join([family['name'] for family in families])
    return HttpResponse(response)

def display_one_animal(request, animal_id):
    animal = next((a for a in animals if a['id'] == animal_id), None)
    if not animal:
        return HttpResponse("Animal not found.")
    
    response = f"Name: {animal['name']}, Legs: {animal['legs']}, Weight: {animal['weight']}kg, Height: {animal['height']}cm, Speed: {animal['speed']}km/h"
    return HttpResponse(response)

def display_animal_per_family(request, family_id):
    family_name = next((f['name'] for f in families if f['id'] == family_id), None)
    if not family_name:
        return HttpResponse("Family not found.")
    
    animals_in_family = [a for a in animals if a['family'] == family_id]
    response = "<br>".join([f"Name: {animal['name']}" for animal in animals_in_family])
    return HttpResponse(response)
