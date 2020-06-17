from django.shortcuts import render
from product.models import Product


# Create your views here.
def category_view(request, category):
    queryset = Product.objects.filter(category=category)
    context = {
        'object_list': queryset,
    }
    return render(request, 'product/product_list.html', context)
