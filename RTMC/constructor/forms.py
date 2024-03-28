from django import forms


class TemplateForm(forms.Form):

    TEMPLATE_TYPE_CHOICES = (
        ('wo', 'Шаблон без организации'),
        ('w', 'Шаблон с организацией'),
    )

    template_type = forms.ChoiceField(choices=TEMPLATE_TYPE_CHOICES, required=True)

    template_name = forms.CharField(label='Название шаблона', required=True)
    
    template_file = forms.FileField(label='Файл шаблона', required=True)