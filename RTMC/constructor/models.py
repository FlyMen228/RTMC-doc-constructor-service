from django.utils import timezone
from django.db import models


class Template(models.Model):
    
    id = models.AutoField(verbose_name='ID', primary_key=True)
    
    name = models.CharField(verbose_name='Название шаблона', max_length=200, unique=True, null=True,
                            help_text='Название мероприятия + грамота, сертификат и т.п')
    
    path_to_file = models.CharField(verbose_name='Путь до шаблона на локальном диске', max_length=200, null=True,
                                    help_text='Полный путь до хранящегося на локальном диске pdf файла')
    
    DOC_TYPE = (
        ('w', 'Шаблон с организацией'),
        ('wo', 'Шаблон без организации'),
    )
    
    doc_type = models.CharField(verbose_name='Тип документа', max_length=2, choices=DOC_TYPE, default='wo', 
                                help_text='Указывается ли организация в шаблоне или нет')
    
    creation_datetime = models.DateTimeField(verbose_name='Дата и время создания шаблона', default=timezone.now,
                                             help_text='Дата создания шаблона')
    
    
    class Meta:
        
        ordering = ['id', '-creation_datetime',]
        
        verbose_name = 'Шаблон'
        
        verbose_name_plural = 'Шаблоны'
        
        indexes = [models.Index(fields=['name'], name='template_name'),]
    
    
    def __str__(self) -> str:
        
        return self.name