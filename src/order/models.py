from django.db import models
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect

User = get_user_model()
# Create your models here.

class Order (models.Model):
    user = models.ForeignKey(
        User,
        verbose_name= "Customer",
        on_delete=models.PROTECT,
    )

    summ = models.DecimalField(
        verbose_name="Order summ",
        max_digits=8,
        decimal_places=2,
    )
    order_currency = models.ForeignKey(
        "references.Currency",
        verbose_name="Currency",
        on_delete=models.PROTECT,
    )

    def __str__(self) -> str:
            return f"Order for User { self.user.username } - { self.summ } {self.order_currency.name}"
    
    def get_absolute_url(self):
        return f"/order/success/"
    
