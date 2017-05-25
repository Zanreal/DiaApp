from django.contrib import admin

from .models import Category, Insulin
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ['name'] }

class InsulinAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ['title']}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Insulin, InsulinAdmin)