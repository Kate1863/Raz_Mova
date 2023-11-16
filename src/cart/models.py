from django.db import models
from catalog.models import Book
from django.db.models import Sum
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

#STATUSES = (
        #("NEW"),
        #("IS_PROCESSED")
        #("IN_WORK"),
        #("ISSUED"),
        #("CLOSED")
    #)
class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        verbose_name=("Customer"),
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    created = models.DateTimeField(
        verbose_name="Created Date",
        auto_now=False,
        auto_now_add=True,
        )
    
    def __str__(self):
        return f"cart({self.pk})"
    
class ProductInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
         verbose_name=("Cart"),
        on_delete=models.CASCADE,
        related_name="products",
        )
    
    product = models.ForeignKey(
        Book, 
        verbose_name=("Product"), 
        on_delete=models.PROTECT, 
        related_name="carts"
        )

    quantity = models.PositiveIntegerField(
        verbose_name=("Quantity"), 
        default=1
        )

    price = models.DecimalField(
        verbose_name='Price',
        max_digits=6,
        decimal_places=2
        )
    def __str__(self):
        return f"Product({self.pk}): {self.product.title} - Quantity:{self.quantity}"
