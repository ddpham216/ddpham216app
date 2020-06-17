from django.shortcuts import render
from product.models import Product
from django.db.models import Q


# Create your views here.
def search_view(request):
    keyword = request.GET.get('keyword')
    queryset = Product.objects.filter(Q(name__contains=keyword) | Q(description__contains=keyword))
    context = {
        'object_list': queryset,
    }
    return render(request, 'product/product_list.html', context)
