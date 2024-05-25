from django.db import models


class PassportData(models.Model):
    series_number = models.CharField(max_length=10, verbose_name='Серия и номер паспорта')
    issue_date = models.DateField(verbose_name='Дата выдачи')
    who_issued = models.CharField(max_length=50, verbose_name='Кем выдан документ')
    department_code = models.CharField(max_length=7, verbose_name='Код подразделения')
    dob = models.DateField(verbose_name='Дата рождения')
    place_of_birth = models.CharField(max_length=25, verbose_name='Место рождения')

    def __str__(self):
        return self.series_number


class Snils(models.Model):
    number_of_snils = models.CharField(max_length=11, verbose_name='Номер СНИЛСа')

    def __str__(self):
        return self.number_of_snils


class Organization(models.Model):
    inn = models.CharField(max_length=10, verbose_name='ИНН')
    ogrn = models.CharField(max_length=13, verbose_name='ОГРН')
    kpp = models.CharField(max_length=9, verbose_name='КПП')
    full_name = models.CharField(verbose_name='Полное наименование')
    legal_address = models.CharField(verbose_name='Юридический адрес')
    mailing_address = models.CharField(verbose_name='Почтовый адрес')

    def __str__(self):
        return self.full_name


class NotarisedOfAttorney(models.Model):
    name = models.CharField(verbose_name='ФИО')
    inn = models.CharField(max_length=10, verbose_name='ИНН')
    expiration_date = models.DateField(verbose_name='Дата окончания действия доверенности')

    def __str__(self):
        return self.name


class PersonData(models.Model):
    objects = models.Manager()
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    patronymic = models.CharField(max_length=100, verbose_name='Отчество')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    passport_data = models.OneToOneField(PassportData, models.CASCADE, verbose_name='Паспортные данные')
    snils = models.OneToOneField(Snils, models.CASCADE, verbose_name='СНИЛС')
    org_id = models.ForeignKey(Organization, models.PROTECT, null=True)
    proxy_id = models.OneToOneField(NotarisedOfAttorney, models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.last_name
