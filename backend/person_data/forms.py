from django.forms import ModelForm, TextInput, DateInput
from .models import PersonData, PassportData, Snils


class PersonDataForm(ModelForm):
    class Meta:
        model = PersonData
        fields = [
            "last_name",
            "first_name",
            "patronymic",
            "phone_number",
        ]

        widgets = {
            "last_name": TextInput(),
            "first_name": TextInput(),
            "patronymic": TextInput(),
            "phone_number": TextInput(),
        }


class PassportDataForm(ModelForm):
    class Meta:
        model = PassportData
        fields = [
            "series_number",
            "issue_date",
            "who_issued",
            "department_code",
            "dob",
            "place_of_birth",
        ]

        widgets = {
            "series_number": TextInput(),
            "issue_date": DateInput(),
            "who_issued": TextInput(),
            "department_code": TextInput(),
            "dob": DateInput(),
            "place_of_birth": TextInput(),
        }


class SnilsForm(ModelForm):
    class Meta:
        model = Snils
        fields = ["number_of_snils"]

        widgets = {
            "number_of_snils": TextInput(),
        }