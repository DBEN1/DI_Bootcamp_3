from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Profile

@csrf_exempt
def create_profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        profile = Profile(name=name, email=email)
        profile.save()
        return JsonResponse({'status': 'success', 'message': 'Profile created successfully'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def delete_profile(request, id):
    try:
        profile = Profile.objects.get(id=id)
        if profile:
            profile.delete()
            return JsonResponse({'status': 'success', 'message': 'Profile deleted successfully'})
    except Profile.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Profile not found'})

