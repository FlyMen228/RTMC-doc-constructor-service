import os

from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from django.contrib import messages

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