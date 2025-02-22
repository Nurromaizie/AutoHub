from django.shortcuts import render

def home(request):
    return render(request, 'project/index.html')  # Include "project/"
