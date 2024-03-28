from django.contrib import admin

from . import models


class TemplateAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'name', 'doc_type', 'creation_datetime')

    list_filter = ('doc_type', 'creation_datetime')
    
    search_fields = ('name',)
        

admin.site.register(models.Template, TemplateAdmin)