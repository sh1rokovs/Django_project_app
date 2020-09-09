from django.urls import path
import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.index, name='index'),
    path('add/product/<int:pk>/', basketapp.add_product, name='add_product'),
    path('change/<int:pk>/quantity/<int:quantity>/', basketapp.change),
    path('delete/basket/item/<int:pk>/', basketapp.delete_product, name='delete_product'),
]
