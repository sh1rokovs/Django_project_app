from django.urls import path
import neworderapp.views as neworderapp

app_name = 'neworderapp'

urlpatterns = [
    path('', neworderapp.OrderList.as_view(), name='index'),
    path('create/', neworderapp.OrderCreate.as_view(), name='order_create'),
    path('read/<int:pk>/', neworderapp.OrderDetail.as_view(), name='order_read'),
    path('update/<int:pk>/', neworderapp.OrderUpdate.as_view(), name='order_update'),
    path('delete/<int:pk>/', neworderapp.OrderDelete.as_view(), name='order_delete'),
    path('forming/complete/<int:pk>/', neworderapp.order_forming_complete, name='order_forming_complete'),
]
