from django import forms


class TemplateForm(forms.Form):

    DOCUMENT_TYPE_CHOICES = (
        ('', 'Выберите тип шаблон...'),
        ('withoutOrg', 'Шаблон без организации'),
        ('withOrg', 'Шаблон с организацией'),
    )

    document_type = forms.ChoiceField(choices=DOCUMENT_TYPE_CHOICES)

    template_name = forms.CharField(label='Название шаблона', required=True)

    organization_name = forms.CharField(label='Название организации', required=False)