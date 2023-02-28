from django.contrib import admin
from .models import *


@admin.register(Task)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed')
    search_fields = ('title', 'completed')
    list_editable = ('title', 'completed')
    list_filter = ('title', 'completed')
    list_per_page = 10
