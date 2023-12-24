from django.db import models


# Create your models here.
class Item(models.Model):
    GENRE = (
        ('Драма', 'Драма'),
        ('Ужасы', 'Ужасы'),
        ('Экшен', 'Экшен'),
        ('Слэшер', 'Слэшер'),
        ('Криминал', 'Криминал'),
    )
    name = models.CharField(max_length=54)
    image = models.ImageField(upload_to='')
    duration = models.IntegerField()
    genre = models.CharField(max_length=54, choices=GENRE)
    description = models.TextField(null=True)
    trailer = models.URLField(null=True)
    watch = models.URLField(null=True)

    def __str__(self):
        return self.name
