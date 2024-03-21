from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('make-template/', views.make_template, name='make-template')
]