import os

from django.shortcuts import render, redirect, get_object_or_404
from django.http import request, HttpResponse
from django.contrib import messages
from django.db.models import Q

from .forms import TemplateForm
from .models import Template


def index(request: request) -> HttpResponse:
    
    return render(request, 'index.html')


def make_template(request: request) -> HttpResponse:
    
    if request.method == 'POST':

        form = TemplateForm(request.POST, request.FILES)
        
        if form.is_valid():

            template_name = form.cleaned_data['template_name']
            
            template_type = form.cleaned_data['template_type']

            template_file = request.FILES['template_file']


            save_path = os.path.join('constructor', 'documents', template_name + '.pdf')
            
            full_save_path = os.path.join(os.getcwd(), save_path)
            
            os.makedirs(os.path.dirname(full_save_path), exist_ok=True)
            
            
            with open(full_save_path, 'wb+') as destination:

                for chunk in template_file.chunks():

                    destination.write(chunk)
                  
                            
            new_template = Template(
                name = template_name,
                path_to_file = full_save_path,
                doc_type = template_type,
            )
            
            new_template.save()
            
            messages.success(request, 'Шаблон успешно сохранён!')
            
            return redirect('make-template')
            
        else:
            
            return render(request, 'constructor/make_template.html', {'form': form})
        
    else:

        form = TemplateForm()

    context = {'form': form}

    return render(request, 'constructor/make_template.html', context)


def chose_template(request: request) -> HttpResponse:
    
    return render(request, 'constructor/chose_template.html')


def search_template(request: request) -> HttpResponse:
    
    query = request.GET.get('query', '')

    if query:

        templates = Template.objects.filter(Q(name__icontains=query))

    else:

        templates = Template.objects.none()
        
    return render(request, 'constructor/chose_template.html', {'templates': templates})


def load_participants(request: request, id: int) -> HttpResponse:
    
    template = get_object_or_404(Template, pk=id)
    
    return render(request, 'constructor/load_participants.html', {'template' : template})