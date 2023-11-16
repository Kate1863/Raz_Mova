# Generated by Django 4.2.5 on 2023-10-19 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3, verbose_name='Currency name ISO3')),
                ('description', models.TextField(blank=True, max_length=300, null=True, verbose_name='Description currency')),
            ],
        ),
    ]