# Generated by Django 4.2.5 on 2023-11-04 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0002_genre_publishinghouse_serie_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Serie'),
        ),
    ]
