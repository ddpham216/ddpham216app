from django.urls import path
from .views import generate_bill, manage_bill, detail_order

app_name = 'bill'

urlpatterns = [
    path('generate_bill/', generate_bill, name='create'),
    path('manage_bill/', manage_bill, name="manage"),
    path('detail_order/<pk>/', detail_order, name="detail"),
]