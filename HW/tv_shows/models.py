from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Tv_shows(models.Model):
    GENRE = (
        ('Хоррор', 'Хоррор'),
        ('Комедия', 'Комедия'),
        ('Драма', 'Драма'),
        ('Экшен', 'Экшен'),
        ('Фантастика', 'Фантастика'),
    )
    title = models.CharField(max_length=50, verbose_name='Введите название сериала')
    image = models.ImageField(upload_to='tv_shows/', verbose_name='Добавьте изображение')
    description = models.TextField(verbose_name='Введите описание сериала', blank=True)
    price = models.FloatField(verbose_name='Введите стоимость',
                              validators=[MinValueValidator(0),
                                          MaxValueValidator(500)])
    genre = models.CharField(max_length=50, choices=GENRE, blank=True)
    author = models.CharField(max_length=100, verbose_name='Введите имя автора сериала')
    trailer = models.URLField(verbose_name='Введите ссылку на трейлер сериала', blank=True)

    def __str__(self):
        return self.title
