from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_page, name='search'),
    path('about/', views.about_page, name='about'),
    path('category/', views.category_page, name='category'),
    path('result/', views.search_results, name='search_results'),
    path('sorento/', views.sorento_view, name='sorento'),
    path('ViewAllCar/', views.ViewAllCar, name='ViewAllCar'),
    path('', views.homepage, name='homepage'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('coupe/', views.coupe, name='coupe_category'),
    path('luxury/', views.luxury, name='luxury_category'),
    path('SUV/', views.SUV, name='SUV_category'),
    path('MPV/', views.MPV, name='MPV_category'),
    path('sport/', views.sport, name='sport_category'),
    path('sedan/', views.sedan, name='sedan_category'),
    path('hatchback/', views.hb, name='hatchback_category'),
    path('profile/', views.profile, name='profile'),
    path('recovery/', views.Recovery, name='ewcoveryPW'),
    path('Create/', views.NewAcc, name='newAcc'),
    path('browse/brand/', views.browse_by_brand, name='browse_by_brand'),
    path('browse/price/', views.browse_by_price, name='browse_by_price'),
    path('browse/model/', views.browse_by_model, name='browse_by_model'),
    path('browse/seater/', views.browse_by_seat, name='browse_by_seat'),
    

]
