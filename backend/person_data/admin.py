from django.contrib import admin
from .models import PersonData, PassportData, Snils


@admin.register(PersonData)
class PersonDataAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'phone_number']


admin.site.register(PassportData)
admin.site.register(Snils)
