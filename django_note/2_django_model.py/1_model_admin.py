#--------------- admin.py ---------------#
""" 
from django.db import models

from .models import Name
class NameAdmin(admin.ModelAdmin):
    list_display = ('',)    # model field gulo likho

admin.site.register(Name, NameAdmin)
@admin.register(Name, NameAdmin) """


# update
from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.get_fields()]
    search_fields = ('user__username', 'full_name')  # প্রয়োজনে সার্চ অপশন
    list_filter = ('country', 'date_joined')  # প্রয়োজনে ফিল্টার

admin.site.register(Profile, ProfileAdmin)