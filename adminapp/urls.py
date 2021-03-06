from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.ShopUsersList.as_view(), name='index'),

    path('user/create/', adminapp.user_create, name='user_create'),
    path('user/update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('user/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),

    path('categories/read/', adminapp.CategoriesRead.as_view(), name='categories_read'),
    path('categories/create/', adminapp.CategoryCreate.as_view(), name='categories_create'),
    path('categories/<int:pk>/update/', adminapp.CategoryUpdate.as_view(), name='categories_update'),
    path('categories/<int:pk>/delete/', adminapp.CategoryDelete.as_view(), name='categories_delete'),

    path('categories/<int:pk>/product/create/', adminapp.product_create, name='product_create'),
    path('categories/product/update/<int:pk>/', adminapp.product_update, name='product_update'),
    path('categories/product/delete/<int:pk>/', adminapp.product_delete, name='product_delete'),
    path('product/<int:pk>/detail/', adminapp.ProductDetail.as_view(), name='product_read'),

    path('categories/<int:pk>/product/', adminapp.category_products, name='category_products'),
]
