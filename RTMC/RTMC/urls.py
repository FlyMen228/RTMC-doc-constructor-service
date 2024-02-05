from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('Сonstructor.urls')),
    path('admin/', admin.site.urls),
    path('Сonstructor/', include('Сonstructor.urls')),
]