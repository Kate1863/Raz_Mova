from django.db import models
from references.models import Writer, Serie, Genre, PublishingHouse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone


ACTIVE_CHOICES = (("Yes", "YES"), ("No", "NO"))



class Book(models.Model):
    title = models.CharField(
        verbose_name="Title",
        max_length=50)
    writer = models.ManyToManyField(
        Writer, 
        verbose_name="Writer", 
        related_name="books")
    cover = models.ImageField(
        verbose_name="Cover", 
        upload_to="book_images/%Y/%m/%d")
    price = models.DecimalField(
        verbose_name="Price", 
        max_digits=6, decimal_places=2)
    serie = models.ForeignKey(
        Serie, 
        verbose_name="Serie", 
        on_delete=models.PROTECT, 
        related_name="books")
    genre = models.ManyToManyField(
        Genre, 
        verbose_name="Genre", 
        related_name="books")
    year_of_publishing = models.IntegerField(
        verbose_name="Year of publishing")
    page = models.IntegerField(
        verbose_name="Pages")
    
    format = models.CharField(
        verbose_name="Format", 
        max_length=50)
    isbn = models.PositiveBigIntegerField(
        verbose_name="ISBN",
        validators=[
            MinValueValidator(0000000000000),
            MaxValueValidator(9999999999999),
        ],
    )
    weight = models.IntegerField(
        verbose_name="Weight")
    age = models.IntegerField(
        verbose_name="Age restrictions")
    publishing_house = models.ForeignKey(
        PublishingHouse, 
        verbose_name="Publishing House", 
        on_delete=models.PROTECT, 
        related_name="books"
    )
    quantity = models.IntegerField(
        verbose_name="Quantity")
    available = models.CharField(
        verbose_name="Available for order",
        max_length=3,
        choices=ACTIVE_CHOICES,
        default="Yes",
    )
    rating = models.PositiveIntegerField(
        verbose_name="Rating (1-10)",
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
    )
    date_of_entry = models.DateTimeField(
        verbose_name="Date of entry", 
        default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Book({self.pk}): {self.title}"

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    


# URL-шаблоны и (templates) для отображения этих карточек товаров в магазине





