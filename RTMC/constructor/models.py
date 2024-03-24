from django.utils import timezone
from django.db import models


class Template(models.Model):
    
    name = models.CharField(verbose_name='Название документа', max_length=200, unique=True, null=True,
                            help_text='Название мероприятия + грамота, сертификат и т.п', 
                            #db_comment='Название мероприятия + грамота, сертификат и т.п'
                            )
    
    path_to_file = models.CharField(verbose_name='Относительный путь до шаблона', max_length=200, null=True,
                                    help_text='Относительный путь до хранящегося pdf файла',
                                    #db_comment='Относительный путь до хранящегося pdf файла'
                                    )
    
    DOC_TYPE = (
        ('w', 'Документ с организацией'),
        ('wo', 'Документ без организации'),
    )
    
    doc_type = models.CharField(verbose_name='Тип документа', max_length=2, choices=DOC_TYPE, default='wo', 
                                help_text='Указывается ли организация в шаблоне или нет',
                                #db_comment='Указывается ли организация в шаблоне или нет'
                                )
    
    creation_date = models.DateTimeField(verbose_name='Дата создания шаблона', default=timezone.now,
                                     help_text='Дата создания шаблона',
                                     #db_comment='Дата создания шаблона'
                                     )
    
    
    class Meta:
        
        ordering = ['pk', 'creation_date', 'name',]
        
        verbose_name = 'Шаблон'
        
        verbose_name_plural = 'Шаблоны'
        
        indexes = [models.Index(fields=['name'], name='template_name'),]
    
    
    def __str__(self) -> str:
        
        return self.name + self.creation_date