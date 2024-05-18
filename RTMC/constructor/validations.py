import os

from django.core.exceptions import ValidationError


def validate_pdf_format(file):
    
    extention = os.path.splitext(file.name)[1]
    
    valid_extention = ['pdf',]
    
    if not extention.lower() in valid_extention:
        
        raise ValidationError('Неподдерживаемый формат файла. Загрузите .pdf файл!')


def validate_csv_format(file):
    
    extention = os.path.splitext(file.name)[1]
    
    valid_extention = ['csv',]
    
    if not extention.lower() in valid_extention:
        
        raise ValidationError('Неподдерживаемый формат файла. Загрузите .csv файл!')