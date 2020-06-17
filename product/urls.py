from django.urls import path
from .views import ProductList, ProductDetail, add_to_cart, reduce_to_cart


app_name = 'product'

urlpatterns = [
    path('<slug>/', ProductDetail.as_view(), name='detail'),
    path('add_to_cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('reduce_to_cart/<slug>/', reduce_to_cart, name='reduce_to_cart'),
    path('', ProductList.as_view(), name='list'),
]