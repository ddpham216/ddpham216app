from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from order.models import OrderProduct


# Create your views here.

@login_required(login_url='/account/login')
def cart_view(request):
    if request.user.is_authenticated:
        order_list = OrderProduct.objects.filter(user=request.user, checkout=False)

    total = 0

    for obj in order_list:
        total += obj.get_final_price()

    context = {
        'order_list': order_list,
        'total': total,
    }

    print(order_list)

    return render(request, 'cart/cart.html', context)
