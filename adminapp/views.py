from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from adminapp.forms import AdminShopUserCreateForm, AdminShopUserEditForm, AdminProductCategoryCreateForm, \
    AdminProductUpdateForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


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
        if hasattr(self, 'page_title'):
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


@user_passes_test(lambda u: u.is_superuser)
def category_products(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    object_list = category.product_set.all()
    context = {
        'page_title': f'категория {category.name}/продукты',
        'category': category,
        'object_list': object_list
    }
    return render(request, 'adminapp/category_product_list.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        form = AdminProductUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(
                'myadmin:category_products',
                kwargs={'pk': category.pk}
            ))
    else:
        form = AdminProductUpdateForm(
            initial={
                'category': category,
            }
        )

    context = {
        'page_title': 'продукты/создание',
        'form': form,
        'category': category,
    }
    return render(request, 'adminapp/product_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = AdminProductUpdateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(
                'myadmin:category_products',
                kwargs={'pk': product.category.pk}
            ))
    else:
        form = AdminProductUpdateForm(instance=product)

    context = {
        'page_title': 'продукты/редактирование',
        'form': form,
        'category': product.category,
    }
    return render(request, 'adminapp/product_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    obj = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        obj.is_active = False
        obj.save()
        return HttpResponseRedirect(reverse(
            'myadmin:category_products',
            kwargs={'pk': obj.category.pk}
        ))

    context = {
        'title': 'продукты/удаление',
        'object': obj,
    }
    return render(request, 'adminapp/product_delete.html', context)


class ProductDetail(OnlySuperUserMixin, PageTitleMixin, DetailView):
    page_title = 'админка/категории/товары'
    model = Product
