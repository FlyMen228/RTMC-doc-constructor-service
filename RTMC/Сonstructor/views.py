from django.shortcuts import render
from django.http import request, HttpResponse


def index(request: request) -> HttpResponse:
    
    return HttpResponse('yeap')