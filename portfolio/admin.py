
from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    '''
    Add extended fields to Admin Panel
    '''
    readonly_fields = ('created', 'updated')

admin.site.register(Project, ProjectAdmin)
