from django.contrib import admin
from .models import PersonData


@admin.register(PersonData)
class PersonDataAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'phone_number']
