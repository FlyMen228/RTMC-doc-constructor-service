from django.shortcuts import render
from django.http import request, HttpResponse, HttpResponseRedirect

from .forms import TemplateForm


def index(request: request) -> HttpResponse:
    
    return render(request, 'index.html')


def make_template(request: request) -> HttpResponse:
    
    if request.method == 'POST':

        form = TemplateForm(request.POST)

        if form.is_valid():

            # Здесь можно добавить логику обработки данных, например сохранение в базу данных

            # После обработки формы, вы можете перенаправить на другую страницу

            return HttpResponseRedirect('/success-url/')

    else:

        form = TemplateForm()

    context = {'form': form}

    return render(request, 'constructor/make_template.html', context)