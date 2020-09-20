from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from authapp.forms import forms, ShopUserProfileForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory


class FormControlMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class AdminShopUserCreateForm(FormControlMixin, UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username', 'first_name', 'last_name', 'is_superuser',
            'is_staff', 'password1', 'password2', 'email', 'age', 'avatar'
        )

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Пользователь слишком мал!")
        return data


class AdminShopUserEditForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username', 'first_name', 'last_name', 'is_superuser',
            'is_staff', 'email', 'age', 'avatar'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class AdminProductCategoryCreateForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'
