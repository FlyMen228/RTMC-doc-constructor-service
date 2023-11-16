from django.db import models


class Template(models.Model):
    
    event = models.CharField('Мероприятие', max_length=200, db_column='Мероприятие', help_text='Мероприятие, к которому относится шаблон')