from django.shortcuts import render, redirect
from .forms import PersonDataForm, PassportDataForm, SnilsForm, OrganizationForm, NotarisedOfAttorneyForm


def register_physical(request):
    if request.method == 'POST':
        person_form = PersonDataForm(request.POST)
        passport_form = PassportDataForm(request.POST)
        snils_form = SnilsForm(request.POST)
        notarised_of_attorney = NotarisedOfAttorneyForm(request.POST)
        if (person_form.is_valid() and passport_form.is_valid()
            and snils_form.is_valid() and notarised_of_attorney.is_valid()):
            person_form.passport_data = passport_form
            person_form.snils = snils_form
            person_form.proxy_id = notarised_of_attorney
            notarised_of_attorney.save()
            passport_form.save()
            snils_form.save()
            person_form.save()
            return redirect('personal_info', permanent=True)
    else:
        person_form = PersonDataForm()
        passport_form = PassportDataForm()
        snils_form = SnilsForm()
        notarised_of_attorney = NotarisedOfAttorneyForm()

    return render(request, 'physical_face.html', {
        'person_data': person_form,
        'passport_data': passport_form,
        'snils_data': snils_form,
        'notarised_of_attorney': notarised_of_attorney,
    })


def register_legal(request):
    if request.method == 'POST':
        organization = OrganizationForm(request.POST)
        notarised_of_attorney = NotarisedOfAttorneyForm(request.POST)
        if organization.is_valid() and notarised_of_attorney.is_valid():
            organization.save()
            notarised_of_attorney.save()
            return redirect('success', permanent=True)
    else:
        organization = OrganizationForm()
        notarised_of_attorney = NotarisedOfAttorneyForm()

    return render(request, 'legal_face.html', {
        'organization': organization,
        'notarised_of_attorney': notarised_of_attorney
    })


def main(request):
    return render(request, 'main.html')


def success(request):
    return render(request, 'success_page.html')


def choice(request):
    return render(request, 'main.html')


def physical_face(request):
    if request.method == 'POST':
        passport_data = forms.PassportDataForm(request.POST)
        snils_data = forms.SnilsForm(request.POST)
        person_data = forms.PersonDataForm(request.POST)
        organization_data = forms.OrganizationForm(request.POST)
        notarised_of_attorney_data = forms.NotarisedOfAttorneyForm(request.POST)

        if person_data.is_valid() and passport_data.is_valid() and snils_data.is_valid() \
                and organization_data.is_valid() and notarised_of_attorney_data.is_valid():
            passport_data = passport_data.save()
            snils_data = snils_data.save()
            person_data = person_data.save(commit=False)
            person_data.passport_data = passport_data
            person_data.snils = snils_data
            organization_data = organization_data.save()
            notarised_of_attorney_data = notarised_of_attorney_data.save()

            person_data.organization = organization_data
            person_data.notarised_of_attorney = notarised_of_attorney_data

            person_data.save()

            return redirect('success', permanent=True)
        else:
            return redirect('fall', permanent=True)

    person_data = forms.PersonDataForm()
    passport_data = forms.PassportDataForm()
    snils_data = forms.SnilsForm()
    organization_data = forms.OrganizationForm()
    notarised_of_attorney_data = forms.NotarisedOfAttorneyForm()

    context = {
        'person_data': person_data,
        'passport_data': passport_data,
        'snils_data': snils_data,
        'organization': organization_data,
        'notarised_of_attorney': notarised_of_attorney_data,
    }
    return render(request, 'physical_face.html', context)


def legal_face(request):
    if request.method == 'POST':
        passport_data = forms.PassportDataForm(request.POST)
        snils_data = forms.SnilsForm(request.POST)
        person_data = forms.PersonDataForm(request.POST)
        organization_data = forms.OrganizationForm(request.POST)
        notarised_of_attorney_data = forms.NotarisedOfAttorneyForm(request.POST)

        if person_data.is_valid() and passport_data.is_valid() and snils_data.is_valid() \
                and organization_data.is_valid() and notarised_of_attorney_data.is_valid():
            passport_data = passport_data.save()
            snils_data = snils_data.save()
            person_data = person_data.save(commit=False)
            person_data.passport_data = passport_data
            person_data.snils = snils_data
            organization_data = organization_data.save()
            notarised_of_attorney_data = notarised_of_attorney_data.save()

            person_data.organization = organization_data
            person_data.notarised_of_attorney = notarised_of_attorney_data

            person_data.save()

            return redirect('success', permanent=True)
        else:
            return redirect('fall', permanent=True)

    person_data = forms.PersonDataForm()
    passport_data = forms.PassportDataForm()
    snils_data = forms.SnilsForm()
    organization_data = forms.OrganizationForm()
    notarised_of_attorney_data = forms.NotarisedOfAttorneyForm()

    context = {
        'person_data': person_data,
        'passport_data': passport_data,
        'snils_data': snils_data,
        'organization': organization_data,
        'notarised_of_attorney': notarised_of_attorney_data,
    }
    return render(request, 'legal_face.html', context)
