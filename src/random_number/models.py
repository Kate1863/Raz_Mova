from django.db import models

# Create your models here.


class Writer(models.Model):
    first_name = models.CharField(
        verbose_name="First Name", 
        max_length=50
        )
    last_name = models.CharField(
        verbose_name="Last Name", 
        max_length=50
        )
    
    genre = models.CharField(
        verbose_name="Genre",
        max_length=50,
        null=True,
        blank=True
    )    

    def __str__(self):
        return f"Writer {self.first_name} {self.last_name}"
    
