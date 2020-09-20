from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from adminapp.forms import AdminShopUserCreateForm, AdminShopUserEditForm, AdminProductCategoryCreateForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory


# @user_passes_test(lambda x: x.is_superuser)
# def index(request):
#    users_list = get_user_model().objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#   context = {
#       'page_title': 'админка/пользователи',
#       'users_list': users_list
#   }
#   return render(request, 'adminapp/shopuser_list.html', context)

class OnlySuperUserMixin:
    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PageTitleMixin:
    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        data['page_title'] = self.page_title
        return data


class ShopUsersList(OnlySuperUserMixin, PageTitleMixin, ListView):
    page_title = 'админка/пользователи'
    model = get_user_model()


@user_passes_test(lambda x: x.is_superuser)
def user_create(request):
    if request.method == 'POST':
        user_form = AdminShopUserCreateForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('myadmin:index'))
    else:
        user_form = AdminShopUserCreateForm()

    context = {
        'title': 'пользователи/создание',
        'user_form': user_form
    }

    return render(request, 'adminapp/user_create.html', context)


@user_passes_test(lambda x: x.is_superuser)
def user_update(request, pk):
    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = AdminShopUserEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('myadmin:user_update', args=[edit_user.pk]))
    else:
        edit_form = AdminShopUserEditForm(instance=edit_user)
    context = {
        'page_title': 'пользователи/редактирование',
        'user_form': edit_form
    }
    return render(request, 'adminapp/user_create.html', context)


@user_passes_test(lambda x: x.is_superuser)
def user_delete(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)

    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('myadmin:index'))
    context = {
        'page_title': 'пользователи/удаление',
        'user_delete': user,
    }
    return render(request, 'adminapp/user_delete.html', context)


# @user_passes_test(lambda x: x.is_superuser)
# def categories_read(request):
#   context = {
#      'page_title': 'админка/пользователи',
#       'categories_list': ProductCategory.objects.all()
#   }
#   return render(request, 'adminapp/productcategory_list.html', context)


class CategoriesRead(OnlySuperUserMixin, PageTitleMixin, ListView):
    page_title = 'админка/категории'
    model = ProductCategory


class CategoryCreate(OnlySuperUserMixin, PageTitleMixin, CreateView):
    page_title = 'админка/категории/создание'
    model = ProductCategory
    success_url = reverse_lazy('myadmin:categories_read')
    # fields = '__all__'
    form_class = AdminProductCategoryCreateForm


class CategoryUpdate(OnlySuperUserMixin, PageTitleMixin, UpdateView):
    page_title = 'админка/категории/редактирование'
    model = ProductCategory
    success_url = reverse_lazy('myadmin:categories_read')
    form_class = AdminProductCategoryCreateForm


class CategoryDelete(OnlySuperUserMixin, PageTitleMixin, DeleteView):
    page_title = 'админка/категории/удаление'
    model = ProductCategory
    success_url = reverse_lazy('myadmin:categories_read')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

