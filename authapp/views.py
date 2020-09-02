from django.shortcuts import render
from authapp.forms import MyAuthenticationForm


def login(request):
    if request.method =='POST':
        pass
    elif request.method =='GET':
        form = MyAuthenticationForm()
    context = {
        'title': 'аутентификация',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    pass


def register(request):
    pass
