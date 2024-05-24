from django.db import models


class PassportData(models.Model):
    series_number = models.CharField(max_length=10, verbose_name='Серия и номер паспорта')
    issue_date = models.DateField(verbose_name='Дата выдачи')
    who_issued = models.CharField(verbose_name='Кем выдан документ')
    department_code = models.CharField(max_length=7, verbose_name='Код подразделения')
    dob = models.DateField(verbose_name='Дата рождения')
    place_of_birth = models.CharField(verbose_name='Место рождения')

    def __str__(self):
        return self.series_number


class Snils(models.Model):
    number_of_snils = models.CharField(verbose_name='Номер СНИЛСа')

    def __str__(self):
        return self.number_of_snils


class PersonData(models.Model):
    objects = models.Manager()
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    patronymic = models.CharField(max_length=100, verbose_name='Отчество')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    passport_data = models.OneToOneField(PassportData, models.CASCADE, verbose_name='Паспортные данные')
    snils = models.OneToOneField(Snils, models.CASCADE, verbose_name='СНИЛС')

    def __str__(self):
        return self.last_name
