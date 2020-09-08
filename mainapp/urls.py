from django.urls import path, re_path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('contact/', mainapp.contact, name='contact'),
    path('products/', mainapp.products, name='products'),
    path('category/<int:pk>/products/', mainapp.catalog, name='catalog'),
    path('product/<int:pk>/', mainapp.product_list, name='product_list'),
]
