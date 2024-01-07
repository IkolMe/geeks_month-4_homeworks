from django.db import models
from django.contrib.auth.models import User


MALE = 1
FEMALE = 2
UNDEFINED = 3

GENDER_TYPE = (
    (MALE, 'М'),
    (FEMALE, 'Ж'),
    (UNDEFINED, 'Другое')
)


class CustomUser(User):
    phone_number = models.CharField(max_length=13, default='+996', verbose_name='Укажите номер телефона')
    date_of_birth = models.DateField(verbose_name='Увкажите дату рождения')
    gender = models.CharField(max_length=10, choices=GENDER_TYPE, verbose_name='Ваш пол')
