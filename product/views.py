from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from product.models import Product
from order.models import OrderProduct


# Create your views here.
class ProductList(ListView):
    model = Product
    template_name = 'product/product_list.html'


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/product_detail.html'


@login_required(login_url='account:login')
def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order, create = OrderProduct.objects.get_or_create(
        user=request.user,
        product=product,
    )

    if not create:
        order.quantity += 1
        order.save()

    return redirect('order:cart')


@login_required(login_url='account:login')
def reduce_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order, create = OrderProduct.objects.get_or_create(
        user=request.user,
        product=product,
    )

    if not create:
        order.quantity -= 1
        order.save()
        if order.quantity < 1:
            order.delete()

    return redirect('order:cart')
