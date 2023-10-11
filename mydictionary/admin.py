from django.contrib import admin

from mydictionary.models import Word

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('english', 'translate')
    fields = ('english', 'translate')
