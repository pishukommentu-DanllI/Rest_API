# Generated by Django 4.1.2 on 2023-02-28 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_book_pages_alter_book_anatasoin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.DateField(),
        ),
    ]
