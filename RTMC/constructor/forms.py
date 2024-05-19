from django import forms

from .validations import validate_csv_format, validate_pdf_format


class TemplateForm(forms.Form):

    TEMPLATE_TYPE_CHOICES = (
        ('wo', 'Шаблон без организации'),
        ('w', 'Шаблон с организацией'),
    )

    template_type = forms.ChoiceField(choices=TEMPLATE_TYPE_CHOICES, required=True)

    template_name = forms.CharField(label='Название шаблона', required=True)
    
    template_file = forms.FileField(label='Файл шаблона', required=True, validators=[validate_pdf_format])
    
    
class LoadParticipantForm(forms.Form):
    
    fullname = forms.CharField(label='ФИО участника', required=True)
    
    organization_name = forms.CharField(label='Название организации', required=False)
    

class LoadParticipantsForm(forms.Form):
    
    load_file = forms.FileField(label="Файл загрузки", required=True, validators=[validate_csv_format])