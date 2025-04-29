from django.shortcuts import render

def homepage(request):
    return render(request, 'project/index.html')

def viewallcars(request):
    return render(request, 'project/viewallcars.html')
