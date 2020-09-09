from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse
from authapp.forms import ShopUserAuthenticationForm, ShopUserRegisterForm, ShopUserProfileForm


def login(request):
    redirect_url = request.GET.get('next', None)

    if request.method == 'POST':
        form = ShopUserAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                redirect_url = request.POST.get('redirect_url', None)
                auth.login(request, user)
                if redirect_url:
                    return HttpResponseRedirect(redirect_url)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = ShopUserAuthenticationForm()
    context = {
        'title': 'аутентификация',
        'form': form,
        'redirect_url': redirect_url,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def user_register(request):
    if request.method == 'POST':
        user = ShopUserRegisterForm(request.POST, request.FILES)
        if user.is_valid():
            user.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        user = ShopUserRegisterForm()
    context = {
        'page_title': 'регистрация',
        'form': user,
    }
    return render(request, 'authapp/register.html', context)


def user_profile(request):
    if request.method == 'POST':
        user = ShopUserProfileForm(request.POST, request.FILES, instance=request.user)
        if user.is_valid():
            user.save()
            return HttpResponseRedirect(reverse('main:index'))
    else:
        user = ShopUserProfileForm(instance=request.user)
    context = {
        'page_title': 'профиль',
        'form': user,
    }
    return render(request, 'authapp/profile.html', context)
