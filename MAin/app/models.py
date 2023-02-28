from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name='имя')
    anatasoin = models.CharField(max_length=255, verbose_name='аннотации')
    year = models.IntegerField(verbose_name='год выпуска')

    def __str__(self):
        return self.name
