from django.contrib import admin

from . import models


admin.site.register(models.Template)


class TemplateAdmin(admin.ModelAdmin):
    
    list_display = ["event", ]