from django.shortcuts import render

from mainapp.models import ProductCategory


def index(request):
    context = {
        'page_title': 'Главная',
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
    categories = ProductCategory.objects.all()

    context = {
        'page_title': 'продукты',
        'categories': categories,
    }
    return render(request, 'mainapp/products.html', context)
