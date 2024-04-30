from django.contrib import admin

from . import models


class ParticipantInLine(admin.TabularInline):
    
    model = models.Participant
    
    extra = 0


class TemplateAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'name', 'doc_type', 'creation_datetime',)

    list_filter = ('doc_type', 'creation_datetime',)
    
    search_fields = ('name',)
    
    fieldsets = (
        ('Данные шаблона', {
            'fields': ('name', 'doc_type')
        }),
        ('Путь до файла', {
            'fields': ['path_to_file']
        }),
        ('Дата создание шаблона', {
            'fields': ['creation_datetime']
        })
    )
    
    inlines = [ParticipantInLine,]
        



class ParticipantAdmin(admin.ModelAdmin):
    
    list_display = ('fullname', 'template', 'organization_name', 'creation_datetime',)
    
    list_filter = ('creation_datetime', 'template__name',)
    
    search_fields = ('fullname', 'template__name', 'organization_name',)
    
    fieldsets = (
        (None, {
            'fields': ['template']
        }),
        ('Данные участника', {
            'fields': ('fullname', 'organization_name')
        }),
        ('Дата добавления участника', {
            'fields': ['creation_datetime']
        }),
    )


admin.site.register(models.Template, TemplateAdmin)
admin.site.register(models.Participant, ParticipantAdmin)