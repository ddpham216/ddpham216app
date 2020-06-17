from django.shortcuts import render
from django.core.paginator import Paginator

from product.models import Product


def index(request):
    featured_list = Product.objects.filter(featured=True)
    paginator = Paginator(featured_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'index.html', context)