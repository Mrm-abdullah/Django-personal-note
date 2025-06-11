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


# StackedInline > duiata model aksathe rakha
from django.contrib import admin
from store.models import Category, Product, ProductImages

class ProductImagesAdmin(admin.StackedInline):
    model = ProductImages
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ('mainimage', 'name','category','preview_text','detail_text', 'price','old_price')

admin.site.register(Product, ProductAdmin)