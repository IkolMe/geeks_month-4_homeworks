from django.db import models


class CarsModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.CharField(max_length=255)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title
