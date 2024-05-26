from django.forms import ModelForm, TextInput, DateInput
from . import models


class PersonDataForm(ModelForm):
    class Meta:
        model = models.PersonData
        fields = ["last_name", "first_name",
                  "patronymic", "phone_number",]

        widgets = {
            "last_name": TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "last_name",
                'placeholder': "name@example.com",
            }),
            "first_name": TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "first_name",
                'placeholder': "name@example.com",
            }),
            "patronymic": TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "patronymic",
                'placeholder': "name@example.com",
            }),
            "phone_number": TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "phone_number",
                'placeholder': "name@example.com",
            }),
        }


class PassportDataForm(ModelForm):
    class Meta:
        model = models.PassportData
        fields = [
            "series_number", "issue_date",
            "who_issued", "department_code",
            "dob", "place_of_birth",]

        widgets = {
            "series_number": TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "series_number",
                'placeholder': "name@example.com",
            }),
            "issue_date": DateInput(attrs={
                'type': "date",
                'class': "form-control",
                'id': "issue_date",
                'placeholder': "name@example.com",
            }),
            "who_issued": TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "who_issued",
                'placeholder': "name@example.com",
            }),
            "department_code": TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "number_of_snils",
                'placeholder': "name@example.com",
            }),
            "dob": DateInput(attrs={
                'type': "date",
                'class': "form-control",
                'id': "dob",
                'placeholder': "name@example.com",
            }),
            "place_of_birth": TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "place_of_birth",
                'placeholder': "name@example.com",
            }),
        }


class SnilsForm(ModelForm):
    class Meta:
        model = models.Snils
        fields = ["number_of_snils"]

        widgets = {
            "number_of_snils": TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "number_of_snils",
                'placeholder': "name@example.com",
            }),
        }


class OrganizationForm(ModelForm):
    class Meta:
        model = models.Organization
        fields = ['inn', 'ogrn', 'kpp', 'full_name',
                  'legal_address', 'mailing_address',]

        widgets = {
            "inn": TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "inn",
                'placeholder': "name@example.com",
            }),
            "ogrn": TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "ogrn",
                'placeholder': "name@example.com",
            }),
            "kpp": TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "kpp",
                'placeholder': "name@example.com",
            }),
            "full_name": TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "full_name",
                'placeholder': "name@example.com",
            }),
            "legal_address": TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "legal_address",
                'placeholder': "name@example.com",
            }),
            "mailing_address": TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "mailing_address",
                'placeholder': "name@example.com",
            }),
        }


class NotarisedOfAttorneyForm(ModelForm):
    class Meta:
        model = models.NotarisedOfAttorney
        fields = ['name', 'inn', 'expiration_date',]

    widgets = {
        "name": TextInput(attrs={
            'type': "text",
            'class': "form-control",
            'id': "inn",
            'placeholder': "name@example.com",
        }),
        "inn": TextInput(attrs={
            'type': "text",
            'class': "form-control",
            'id': "inn",
            'placeholder': "name@example.com",
        }),
        "expiration_date": DateInput(attrs={
            'type': "date",
            'class': "form-control",
            'id': "expiration_date",
            'placeholder': "name@example.com",
        }),
    }