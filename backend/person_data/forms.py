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
            "last_name": TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "last_name",
                'onchange': "Verify(last_name,'last_name_err')",
                'placeholder': "name@example.com",
            }),
            "first_name": TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "first_name",
                'onchange': "Verify(first_name,'first_name_err')",
                'placeholder': "name@example.com",
            }),
            "patronymic": TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "patronymic",
                'onchange': "Verify(patronymic,'patronymic_err')",
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
            "series_number": TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "series_number",
                'onchange': "Verify(series_number,'series_number_Err')",
                'placeholder': "name@example.com",
            }),
            "issue_date": DateInput(attrs={
                'type': "date",
                'class': "form-control",
                'id': "issue_date",
                'onchange': "Verify(issue_date,'issue_date_Err')",
                'placeholder': "name@example.com",
            }),
            "who_issued": TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "who_issued",
                'onchange': "Verify(who_issued,'who_issued_Err')",
                'placeholder': "name@example.com",
            }),
            "department_code": TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "number_of_snils",
                'onchange': "Verify(department_code,'department_code_Err')",
                'placeholder': "name@example.com",
            }),
            "dob": DateInput(attrs={
                'type': "date",
                'class': "form-control",
                'id': "dob",
                'onchange': "Verify(dob,'dob_Err')",
                'placeholder': "name@example.com",
            }),
            "place_of_birth": TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "place_of_birth",
                'onchange': "Verify(place_of_birth,'place_of_birth_Err')",
                'placeholder': "name@example.com",
            }),
        }


class SnilsForm(ModelForm):
    class Meta:
        model = Snils
        fields = ["number_of_snils"]

        widgets = {
            "number_of_snils": TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "number_of_snils",
                'onchange': "Verify(number_of_snils,'number_of_snils_Err')",
                'placeholder': "name@example.com",
            }),
        }