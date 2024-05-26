from django.shortcuts import render, redirect
from . import forms
from datetime import datetime


def company_info(request):

    if request.method == 'POST':
        organization_data = forms.OrganizationForm(request.POST)
        notarised_of_attorney_data = forms.NotarisedOfAttorneyForm(request.POST)

        if organization_data.is_valid() and notarised_of_attorney_data.is_valid():

            organization_data = organization_data.cleaned_data
            notarised_of_attorney_data = notarised_of_attorney_data.cleaned_data

            for key, value in notarised_of_attorney_data.items():
                if isinstance(value, datetime):
                    notarised_of_attorney_data[key] = value.strftime('%Y-%m-%d')

            request.session['organization_data'] = organization_data
            request.session['notarised_of_attorney_data'] = notarised_of_attorney_data

            return redirect('personal_info', permanent=True)

    organization_data = forms.OrganizationForm
    notarised_of_attorney_data = forms.NotarisedOfAttorneyForm

    data = {
        'organization': organization_data,
        'notarised_of_attorney': notarised_of_attorney_data,
    }
    return render(request, 'form_org.html', context=data)


def personal_info(request):
    error = ''
    if request.method == 'POST':
        passport_data = forms.PassportDataForm(request.POST)
        snils_data = forms.SnilsForm(request.POST)
        person_data = forms.PersonDataForm(request.POST)

        if person_data.is_valid() and passport_data.is_valid() and snils_data.is_valid():
            passport_data = passport_data.save()
            snils_data = snils_data.save()
            person_data = person_data.save(commit=False)
            person_data.passport_data = passport_data
            person_data.snils = snils_data

            organization_data = request.session.get('organization_data')
            notarised_of_attorney_data = request.session.get('notarised_of_attorney_data')
            person_data.organization = organization_data
            person_data.notarised_of_attorney = notarised_of_attorney_data

            person_data.save()

            request.session.pop('organization_data', None)
            request.session.pop('notarised_of_attorney_data', None)

            return redirect('success', permanent=True)
        else:
            error = 'какая-то ошибка'
            return redirect('fall', permanent=True)

    person_data = forms.PersonDataForm()
    passport_data = forms.PassportDataForm()
    snils_data = forms.SnilsForm()

    data = {
        'person_data': person_data,
        'passport_data': passport_data,
        'snils_data': snils_data,
    }
    return render(request, 'form_reg.html', context=data)


def success(request):
    return render(request, 'success_page.html')