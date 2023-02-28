from django.contrib import admin
from .models import *


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'anatasoin', 'year')
    search_fields = ('name', 'anatasoin', 'year')
    list_editable = ('name', 'anatasoin', 'year')
    list_filter = ('name', 'anatasoin', 'year')
    list_per_page = 20
