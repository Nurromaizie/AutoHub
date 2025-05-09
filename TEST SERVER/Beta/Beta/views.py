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


def browse_by_brand(request):
    brand_name = request.GET.get('name')
    from .models import Car  # just in case
    print("Requested brand:", brand_name)
    cars = Car.objects.filter(brand__iexact=brand_name)
    return render(request, 'main/HomepageBrowseResults.html', {
        'cars': cars,
        'active_filter': 'brand',
        'filter_value': brand_name
    })

def browse_by_price(request):
    order = request.GET.get('order')
    if order == 'high':
        cars = Car.objects.all().order_by('-price')
    elif order == 'low':
        cars = Car.objects.all().order_by('price')
    else:
        cars = Car.objects.all()

    return render(request, 'main/HomepageBrowseResults.html', {
        'cars': cars,
        'active_filter': 'price',
        'filter_value': order
    })

def browse_by_model(request):
    model_type = request.GET.get('type')
    cars = Car.objects.filter(model__iexact=model_type)
    return render(request, 'main/HomepageBrowseResults.html', {
        'cars': cars,
        'active_filter': 'model',
        'filter_value': model_type
    })

def browse_by_seat(request):
    seat_count = request.GET.get('count')
    cars = Car.objects.filter(seater=seat_count)
    return render(request, 'main/HomepageBrowseResults.html', {
        'cars': cars,
        'active_filter': 'seat',
        'filter_value': seat_count
    })




#def result_view(request):
    #query = request.GET.get('query', '')
    #return render(request, 'main/Result.html', {'query': query})