import os

from django.core.exceptions import ValidationError


def validate_pdf(file):
    
    if not file.name.endswith('.pdf'):
        
        raise ValidationError('Загруженный файл должен быть в формате PDF.')
    



def validate_csv(file):
    
    if not file.name.endswith('.csv'):
        
        raise ValidationError('Загруженный файл должен быть в формате CSV.')