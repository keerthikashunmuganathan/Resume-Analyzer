from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .resume_parser import extract_text
from .analyzer import analyze_resume

# Create your views here.

@csrf_exempt
def analyze(request):
    if request.method=="POST":
        try:
            file = request.FILES['resume']
            job_description = request.POST.get('job_description', '')
            resume_text = extract_text(file)
            result = analyze_resume(resume_text, job_description)
            
            return JsonResponse(result)
        except Exception as e:
            return JsonResponse({"Error": str(e)}, status=500)
    return JsonResponse({"error": "POST request required"}, status=400)    