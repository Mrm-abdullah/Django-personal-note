#--------------- admin.py ---------------#
""" 
from django.db import models

from .models import Name
class NameAdmin(admin.ModelAdmin):
    list_display = ('',)    # model field gulo likho

admin.site.register(Name, NameAdmin)
@admin.register(Name, NameAdmin) """

