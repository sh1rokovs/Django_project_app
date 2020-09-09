from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render


@user_passes_test(lambda x: x.is_superuser)
def index(request):
    pass
