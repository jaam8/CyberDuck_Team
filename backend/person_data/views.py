from django.shortcuts import render
from .forms import PersonDataForm, PassportDataForm, SnilsForm

def login(request):
    error = ''
    if request.method == 'POST':
        person_data = PersonDataForm(request.POST)
        passport_data = PassportDataForm(request.POST)
        snils_data = SnilsForm(request.POST)
        if person_data.is_valid() and passport_data.is_valid() and snils_data.is_valid():
            passport_data = passport_data.save()
            snils_data = snils_data.save()
            person_data = person_data.save()
            person_data.passport_data = passport_data
            person_data.snils_data = snils_data
            person_data.save()
    else:
            error = 'какая-то ошибка'

    person_data = PersonDataForm()
    passport_data = PassportDataForm()
    snils_data = SnilsForm()

    data = {
        'person_data': person_data,
        'passport_data': passport_data,
        'snils_data': snils_data,
        'error': error,
    }
    return render(request, 'form.html', context=data)