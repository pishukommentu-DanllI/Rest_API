# Generated by Django 4.1.2 on 2023-02-28 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_yaer_book_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='pages',
        ),
        migrations.AlterField(
            model_name='book',
            name='anatasoin',
            field=models.CharField(max_length=255, verbose_name='аннотации'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=255, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.IntegerField(verbose_name='год выпуска'),
        ),
    ]
