from django.contrib import admin
from .models import NoteAPI
# Register your models here.

@admin.register(NoteAPI)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['NoteID', 'subject', 'description']
