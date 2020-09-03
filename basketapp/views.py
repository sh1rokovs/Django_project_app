from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from basketapp.models import BasketItem
from mainapp.models import Product


def index(request):
    products = BasketItem.objects.all()
    products1 = products[0].product_id
    products2 = Product.objects.filter(id=products1)
    products2 = products2[0].name
    products1 = products[0].quantity
    context = {
        'page_title': 'главная',
        'products': products,
        'products2': products2,
        'products1': products1,
    }
    return render(request, 'basketapp/basket.html', context)


def add_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = BasketItem.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = BasketItem(user=request.user, product=product)

    basket.quantity += 1
    basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
