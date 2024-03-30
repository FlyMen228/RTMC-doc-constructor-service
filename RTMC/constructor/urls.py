from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('make-template/', views.make_template, name='make-template'),
    path('chose-template/', views.chose_template, name='chose-template'),
    path('search-template/', views.search_template, name='search-template')
]