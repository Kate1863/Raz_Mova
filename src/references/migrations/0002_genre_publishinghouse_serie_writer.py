# Generated by Django 4.2.5 on 2023-10-19 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=50, verbose_name='Genre')),
                ('description', models.TextField(blank=True, max_length=300, null=True, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='PublishingHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Publishing House')),
                ('description', models.TextField(blank=True, max_length=300, null=True, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Serie')),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(blank=True, max_length=300, null=True, verbose_name='Description')),
            ],
        ),
    ]
