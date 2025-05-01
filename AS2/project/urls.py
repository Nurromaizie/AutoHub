from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('viewallcars/', views.viewallcars, name='viewallcars'),
    path('profile/', views.profile, name='profile'), 
    path('sorento/', views.sorento, name='sorento'),
    path('login/', views.login_view, name='login'),
]
