from django.contrib import admin

from .models import FootGraph

class FootGraphAdmin(admin.ModelAdmin):
    list_display = ('per', 'league', 'position')

# Register your models here.

admin.site.register(FootGraph, FootGraphAdmin)
 