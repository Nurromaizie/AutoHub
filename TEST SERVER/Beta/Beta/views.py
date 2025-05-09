from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Car
from django.db.models import Q

def search_results(request):
    query = request.GET.get('query', '')
    sort = request.GET.get('sort')
    seat = request.GET.get('seat')
    transmission = request.GET.get('transmission')
    model = request.GET.get('model')

    filters = Q(name__icontains=query) | Q(brand__icontains=query)

    if seat:
        filters &= Q(seats=seat)
    if transmission:
        filters &= Q(transmission__iexact=transmission)
    if model:
        filters &= Q(body_type__iexact=model)

    results = Car.objects.filter(filters)

    if sort == 'low':
        results = results.order_by('price')
    elif sort == 'high':
        results = results.order_by('-price')

    return render(request, 'main/result.html', {
        'query': query,
        'results': results
    })

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

def suv_category(request):
    suvs = Car.objects.filter(body_type__iexact="SUV")
    return render(request, 'main/SUV.html', {'cars': suvs})

def MPV(request):
    return render(request, 'main/MPV.html')

def sport_category(request):
    suvs = Car.objects.filter(body_type__iexact="Sport")
    return render(request, 'main/Sport.html', {'cars': suvs})

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

def Login(request):
    return render(request, 'main/Login.html')


def browse_by_brand(request):
    brand_name = request.GET.get('name', '')
    cars = Car.objects.filter(
        Q(brand__icontains=brand_name) | Q(name__icontains=brand_name)
    )
    return render(request, 'main/HomepageBrowseResults.html', {
        'cars': cars,
        'active_filter': 'brand',
        'filter_value': brand_name
    })

def browse_by_price(request):
    order = request.GET.get('order')  # <== looks for '?order=low' or '?order=high'

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
    model_type = request.GET.get('name')
    cars = Car.objects.filter(body_type__icontains=model_type)

    return render(request, 'main/HomepageBrowseResults.html', {
        'cars': cars,
        'active_filter': 'model',
        'filter_value': model_type
    })

def browse_by_seat(request):
    seat_count = request.GET.get('count')
    cars = Car.objects.filter(seats=seat_count)
    return render(request, 'main/HomepageBrowseResults.html', {
        'cars': cars,
        'active_filter': 'seat',
        'filter_value': seat_count
    })




#def result_view(request):
    #query = request.GET.get('query', '')
    #return render(request, 'main/Result.html', {'query': query})