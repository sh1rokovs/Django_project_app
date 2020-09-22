import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from mainapp.models import ProductCategory, Product


def get_menu():
    return ProductCategory.objects.all()


def index(request):
    context = {
        'page_title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


def contact(request):
    locations = [
        {
            'city': 'Moscow',
            'phone': '+7903231123',
            'email': 'user@example.com',
            'address': 'Bulvar street',
        },
        {
            'city': 'Nizhniy',
            'phone': '+790814212312',
            'email': 'lux@example.com',
            'address': 'Klun street',
        },
        {
            'city': 'Kazan',
            'phone': '8908111111312',
            'email': 'fabri@example.com',
            'address': 'Labr street',
        }
    ]
    context = {
        'page_title': 'контакты',
        'locations': locations,
    }
    return render(request, 'mainapp/contact.html', context)


def products(request):
    get_hot_product = hot_product()
    # _related_products = related_products(get_hot_product)  // оптимизация
    context = {
        'page_title': 'продукты',
        'get_hot_product': get_hot_product,
        # 'related_products': _related_products,
    }
    return render(request, 'mainapp/products.html', context)


def product_list(request, pk):
    context = {
        'page_title': 'продукт',
        'product': get_object_or_404(Product, pk=pk)
    }
    return render(request, 'mainapp/product_list.html', context)


def catalog(request, pk, page=1):
    if pk == 0:
        category = {'pk': 0, 'name': 'Все товары'}
        products = Product.objects.all()
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = Product.objects.filter(category=category)

    products_paginator = Paginator(products, 2)
    try:
        products = products_paginator.page(page)
    except PageNotAnInteger:
        products = products_paginator.page(1)
    except EmptyPage:
        products = products_paginator.page(products_paginator.num_pages)

    context = {
        'page_title': 'каталог',
        'category': category,
        'products': products,
    }
    return render(request, 'mainapp/catalog.html', context)


def hot_product():
    product = Product.objects.all()
    return random.choice(product)
    # products_id = Product.objects.values_list('id', flat=True)    //
    # hot_product_id = random.choice(products_id)                  //оптимизированный вариант
    # return Product.objects.get(pk=hot_product_id)                //
