from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse
from authapp.forms import ShopUserAuthenticationForm, ShopUserRegisterForm, ShopUserProfileForm


def login(request):
    if request.method == 'POST':
        form = ShopUserAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = ShopUserAuthenticationForm()
    context = {
        'title': 'аутентификация',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    pass
