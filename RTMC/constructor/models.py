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
                                             help_text='Дата и время создания шаблона')
    
    
    fullname_x_coordinate = models.FloatField(verbose_name='Х координата текстового поля ФИО', default=0,
                                                help_text='Определяется автоматически при загрузке шаблона')
    
    fullname_y_coordinate = models.FloatField(verbose_name='Y координата текстового поля ФИО', default=0,
                                                help_text='Определяется автоматически при загрузке шаблона')
    
    fullname_textbox_width = models.FloatField(verbose_name='Ширина текстового поля ФИО', default=0,
                                                 help_text='Определяется автоматически при загрузке шаблона')
    
    fullname_textbox_height = models.FloatField(verbose_name='Высота текстового поля ФИО', default=0,
                                                 help_text='Определяется автоматически при загрузке шаблона')
    
    
    organization_x_coordinate = models.FloatField(verbose_name='Х координата текстового поля названия организации', null=True,
                                                help_text='Определяется автоматически при загрузке шаблона')
    
    organization_y_coordinate = models.FloatField(verbose_name='Y координата текстового поля названия организации', null=True,
                                                help_text='Определяется автоматически при загрузке шаблона')
    
    organization_textbox_width = models.FloatField(verbose_name='Ширина текстового поля названия организации', null=True,
                                                 help_text='Определяется автоматически при загрузке шаблона')
    
    organization_textbox_height = models.FloatField(verbose_name='Высота текстового поля названия организации', null=True,
                                                 help_text='Определяется автоматически при загрузке шаблона')
    
    
    class Meta:
        
        ordering = ['id', '-creation_datetime',]
        
        verbose_name = 'Шаблон'
        
        verbose_name_plural = 'Шаблоны'
        
        indexes = [models.Index(fields=['name'], name='template_name'),
                   models.Index(fields=['doc_type'], name='template_doc_type'),]
    
    
    def __str__(self) -> str:
        
        return self.name
    
    
    def display_num_participants(self) -> int:
        
        return self.participant_set.count()
    
    display_num_participants.short_description = 'Количество участников'




class Participant(models.Model):
    
    fullname = models.CharField(verbose_name="ФИО", max_length=120,
                                help_text='Полное имя участника мероприятия. Не длиннее 120 символов')
    
    organization_name = models.CharField(verbose_name='Название организации участника', max_length=200, null=True, blank=True,
                                         help_text='Если в шаблоне есть поле организации, поле заполняется')
    
    creation_datetime = models.DateTimeField(verbose_name='Дата и время добавления участника мероприятия', default=timezone.now,
                                             help_text='Дата и время добавления участника мероприятия')
    
    
    template = models.ForeignKey('Template', verbose_name='Относится к документну', on_delete=models.CASCADE,
                                 help_text='Выбранный при заполнении шаблон документа')
    
    
    class Meta:
        
        ordering = ['id', '-creation_datetime']
        
        verbose_name = 'Участник мероприятия'
        
        verbose_name_plural = 'Участникик мероприятия'
        
        indexes = [models.Index(fields=['fullname'], name='participant_fullname'),
                   models.Index(fields=['template'], name='participant_template'),
                   models.Index(fields=['organization_name'], name='participant_organization_name'),]
        
    
    def __str__(self) -> str:
        
        return '%s (Мероприятие: %s). Организация: %s' % (self.fullname, self.template, self.organization_name)