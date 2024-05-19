import os

from django.shortcuts import render, redirect, get_object_or_404
from django.http import request, HttpResponse
from django.contrib import messages
from django.db.models import Q

from .forms import TemplateForm, LoadParticipantForm, LoadParticipantsForm

from .models import Template, Participant

from .scripts import split_csv


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
    
    if request.method == "POST":
        
        load_participants_form = LoadParticipantsForm(request.POST, request.FILES)
        load_participant_form = LoadParticipantForm(request.POST)
        
        if "submit_many" in request.POST:
            
            csv_file = request.FILES['load_file']
            
            participants = split_csv(csv_file)
            
            for participant in participants:
                
                new_participant = Participant(
                    fullname = participant[0],
                    organization_name = participant[1],
                    template = template
                )
                
                new_participant.save()
                
            messages.success(request, 'Участники успешно добавлены!')
            
            context = {
                'template' : template,
                'load_participant_form' : LoadParticipantForm(),
                'load_participants_form' : LoadParticipantsForm(),
            }
            
            return render(request, 'constructor/load_participants.html', context)
        
        
        if "submit_one" in request.POST:
            
            new_participant = Participant(
                fullname = load_participant_form.cleaned_data['fullname'],
                organization_name = load_participant_form.cleaned_data['organization_name'],
                template = template
            )
            
            new_participant.save()
            
            messages.success(request, 'Участник успешно добавлен!')
            
            context = {
                'template' : template,
                'load_participant_form' : LoadParticipantForm(),
                'load_participants_form' : LoadParticipantsForm(),
            }
            
            return render(request, 'constructor/load_participants.html', context)

        
        context = {
            'template' : template,
            'load_participant_form' : load_participant_form,
            'load_participants_form' : load_participants_form,
        }
        
        return render(request, 'constructor/load_participants.html', context)
        
    
    context = {
        'template' : template,
        'load_participant_form' : LoadParticipantForm(),
        'load_participants_form' : LoadParticipantsForm(),
    }
    
    return render(request, 'constructor/load_participants.html', context)