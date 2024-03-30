from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.defaults import page_not_found


urlpatterns = [
    path('', include('constructor.urls'), name='main'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]

# Для тестировки 404
if settings.DEBUG:
    
    urlpatterns += [
        path('test-404/', page_not_found, kwargs={'exception': Exception("Page not Found")}),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)