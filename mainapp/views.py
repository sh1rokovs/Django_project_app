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
    context = {
        'page_title': 'продукты',
        'categories': get_menu(),
    }
    return render(request, 'mainapp/products.html', context)


def catalog(request, pk):
    if int(pk) == 0:
        category = {'pk': 0, 'name': 'Все'}
        products = Product.objects.all()
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = Product.objects.filter(category=category)
    context = {
        'page_title': 'каталог',
        'categories': get_menu(),
        'category': category,
        'products': products,
    }
    return render(request, 'mainapp/catalog.html', context)
