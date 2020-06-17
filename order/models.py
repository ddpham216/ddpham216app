from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from product.models import Product

STATUS_ORDER = (
    ('C', 'Complete'),
    ('W', 'Waiting'),
    ('R', 'Return'),
)


# Create your models here.
class OrderProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    checkout = models.BooleanField(default=False)
    time_order = models.DateTimeField(auto_now_add=True)
    total_order = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(choices=STATUS_ORDER, max_length=1, default='W')
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    district = models.CharField(max_length=50, null=True, blank=True)
    street_address = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.product.name + ' - ' + self.user.username

    def save(self, *args, **kwargs):
        if self.total_order is None:
            self.total_order = self.get_final_price()
        super(OrderProduct, self).save(*args, **kwargs)

    def get_price(self):
        return self.product.price * self.quantity

    def get_final_price(self):
        price = self.get_price()
        if self.product.discount_price is not None:
            price = price - self.product.discount_price * self.quantity
        return price

    def checkout_order(self):
        self.checkout = True
        self.save()

    def get_absolute_url(self):
        return reverse('bill:detail', kwargs={'pk': self.pk})