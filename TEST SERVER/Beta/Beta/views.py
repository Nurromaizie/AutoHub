from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Car

def search_results(request):
    query = request.GET.get('query', '')
    results = Car.objects.filter(name__icontains=query)
    return render(request, 'main/result.html', {'query': query, 'results': results})

def search_page(request):
    return render(request, 'main/search.html')

def about_page(request):
    return render(request, 'main/About.html')

def category_page(request):
    return render(request, 'main/Category.html')  

def homepage(request):
    cars = Car.objects.all()  
    return render(request, 'main/Homepage.html', {'cars': cars})

def sorento_view(request):
    return render(request, 'main/Sorento.html')

def ViewAllCar(request):
    return render(request, 'main/ViewAllCar.html')

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'main/CarDetail.html', {'car': car})

def coupe(request):
    return render(request, 'main/Coupe.html')  

def luxury(request):
    return render(request, 'main/Luxury.html')

def SUV(request):
    return render(request, 'main/SUV.html')

def MPV(request):
    return render(request, 'main/MPV.html')

def sport(request):
    return render(request, 'main/Sport.html')

def sedan(request):
    return render(request, 'main/Sedan.html')

def hb(request):
    return render(request, 'main/Hatchback.html')

def profile(request):
    return render(request, 'main/Profile.html')

def Recovery(request):
    return render(request, 'main/RecoveryPassw.html')

def NewAcc(request):
    return render(request, 'main/CreateACC.html')




#def result_view(request):
    #query = request.GET.get('query', '')
    #return render(request, 'main/Result.html', {'query': query})