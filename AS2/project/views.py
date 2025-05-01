from django.shortcuts import render

def homepage(request):
    return render(request, 'project/index.html')
def viewallcars(request):
    return render(request, 'project/viewallcars.html')
def profile(request):
    return render(request, 'project/profile.html')
def sorento(request):
    return render(request, 'project/sorento.html')
def login_view(request):
    return render(request, 'project/login.html')

