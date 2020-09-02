from django.urls import path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('user/register/', authapp.user_register, name='user_register'),
    path('user/profile/', authapp.user_profile, name='user_profile'),
]
