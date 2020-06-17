from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.http import HttpResponse
import datetime

from order.models import OrderProduct
from .models import Bill


# Create your views here.

@login_required(login_url='account:login')
def generate_bill(request):
    total = 0

    orders = OrderProduct.objects.filter(user=request.user, checkout=False)

    bill, create = Bill.objects.get_or_create(
        user=request.user,
        timestamp=datetime.datetime.now(),
        country = request.POST.get('country'),
        city = request.POST.get('city'),
        district = request.POST.get('district'),
        street_address = request.POST.get('street'),
        phone = request.POST.get('phone'),
    )

    if create:
        for obj in orders:
            print(obj)
            total += obj.get_final_price()
            bill.orders.add(obj)
            bill.total = total
            bill.save()
            obj.country = request.POST.get('country')
            obj.city = request.POST.get('city')
            obj.district = request.POST.get('district')
            obj.street_address = request.POST.get('street')
            obj.phone = request.POST.get('phone')
            obj.save()
            obj.checkout_order()

    context = {
        'bill': bill,
        'orders': bill.orders.all(),
        'name_of_user': request.user.first_name + ' ' + request.user.last_name,
    }

    return render(request, 'checkout/confirmation.html', context)


@login_required(login_url='account:login')
def manage_bill(request):
    order = OrderProduct.objects.filter(user=request.user, checkout=True)

    print(order)

    context = {
        'orders': order,
    }
    return render(request, 'bill/bill.html', context)


@login_required(login_url='account:login')
def detail_order(request, pk):
    order = OrderProduct.objects.get(user=request.user, pk=pk)
    if order.user != request.user:
        return HttpResponse("Error!")
    context = {
        'object': order,
        'name_of_user': request.user.last_name + ' ' + request.user.first_name
    }
    return render(request, "bill/detail_view.html", context)
