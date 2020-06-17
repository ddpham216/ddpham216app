from django.contrib.auth.decorators import login_required
from django.db import models
from django.utils.text import slugify
from random import randint
from unidecode import unidecode
from django.shortcuts import reverse

CATEGORY = (
    ('TS', 'TShirt'),
    ('DR', 'Dress'),
    ('SH', 'Shoes'),
)


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='product/')
    stock = models.IntegerField()
    category = models.CharField(choices=CATEGORY, max_length=2, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.CharField(max_length=500, null=True)
    featured = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug is None:
            slug = unidecode(self.name + ' ' + str(randint(1, 1000000)))
            self.slug = slugify(slug)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product:detail', kwargs={'slug': self.slug})

    def get_add_to_cart(self):
        return reverse('product:add_to_cart', kwargs={
            'slug': self.slug,
        })

    def get_reduce_to_cart(self):
        return reverse('product:reduce_to_cart', kwargs={
            'slug': self.slug,
        })
