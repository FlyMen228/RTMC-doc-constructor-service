from django.urls import path, re_path

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('get-document/', views.get_document, name='get-document'),
    path('search-document', views.search_document, name='search-document'),
    path('construct-document/', views.construct_document, name='construct-document'),
    path('make-template/', views.make_template, name='make-template'),
    path('chose-template/', views.chose_template, name='chose-template'),
    path('search-template', views.search_template, name='search-template'),
    re_path(r'^load-participants/(?P<id>\d+)/$', views.load_participants, name='load-participants'),
]