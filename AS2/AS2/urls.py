from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project.urls')),  # Add this line to route the home page
    path("__reload__/", include("django_browser_reload.urls")),  # Auto-reload for templates
]
