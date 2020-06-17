from django.urls import path
from category.views import category_view

app_name = 'category'


urlpatterns = [
    path('<category>/', category_view, name='category')
]