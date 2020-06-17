from django.db import models
from django.shortcuts import reverse

from django.contrib.auth.models import User
from order.models import OrderProduct

STATIC_BILL = (
    ('C', 'Complete'),
    ('W', 'Waiting'),
    ('R', 'Return'),
)


# Create your models here.
class Bill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orders = models.ManyToManyField(OrderProduct)
    total = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    street_address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATIC_BILL, max_length=1, default='W')

    def __str__(self):
        return self.user.username + ' ' + str(self.updated)

    def get_absolute_url(self):
        return reverse('bill:detail', kwargs={'pk': self.pk})
