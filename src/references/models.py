from django.db import models
from django.http import HttpResponse
# Create your models here.

class Currency(models.Model):
    name = models.CharField(
        verbose_name='Currency name ISO3',
        max_length=3,
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name='Description currency',
        max_length=300,
        null=True,
        blank=True,
    )
    def __str__(self) -> str:
        return self.name

class Writer(models.Model):
    name = models.CharField(
        verbose_name="Name", 
        max_length=50
        )
    description = models.TextField(
        verbose_name="Description",
        max_length=300, 
        blank=True, 
        null=True,
        )
    
    def __str__(self):
        return f"Writer({self.pk}) {self.name}"

class Genre(models.Model):
    genre = models.CharField(
        verbose_name="Genre",
        max_length=50,)
    description = models.TextField(
        verbose_name="Description",
        max_length=300,
        null=True,
        blank=True
        )    

    def __str__(self):
        return self.genre
    
class Serie(models.Model):
    name = models.CharField(
        verbose_name="Serie", 
        max_length=200
        )

    def __str__(self)->str:
        return self.name

class PublishingHouse(models.Model):
    name = models.CharField(
        verbose_name="Publishing House", 
        max_length=50
        )
    description = models.TextField(
        verbose_name="Description", 
        max_length=300, 
        blank=True, 
        null=True
        )

    def __str__(self):
        return self.name

