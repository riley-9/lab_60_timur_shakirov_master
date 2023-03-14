from django import forms
from django.forms import widgets

from shop.models.products import Product, CategoryChoices


class ProductForm(forms.ModelForm):
    error_css_class = 'error'
    label_css_class = 'label'

    product = forms.CharField(
        label='Продукт',
        max_length=100,
        required=True,
        widget=widgets.TextInput(attrs={
            'class': 'form-control mt-3',
            'style': 'max-width: 750px;',
        })
    )
    description = forms.CharField(
        label='Описание',
        max_length=2000,
        required=False,
        widget=widgets.Textarea(attrs={
            'class': 'form-control mt-3',
            'style': 'max-width: 750px;',
        })
    )
    photo = forms.CharField(
        label='Фото',
        max_length=1000,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control mt-3',
            'style': 'max-width: 750px;',
        })
    )
    category = forms.ChoiceField(
        choices=CategoryChoices.choices,
        label='Категория',
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'max-width: 220px;',
            })
    )
    rest = forms.IntegerField(
        label='Остаток',
        required=True,
        widget=widgets.Input(
            attrs={
                'class': 'form-control',
                'style': 'max-width: 400px;',
            }
        ),
        min_value=0, error_messages={'min_value': 'Остаток не должен быть меньше 0'}
    )
    price = forms.DecimalField(
        label='Стоимость',
        required=True,
        widget=widgets.Input(
            attrs={
                'class': 'form-control',
                'style': 'max-width: 400px;',
            }
        ),
        min_value=1.00, error_messages={'min_value': 'Стоимость не должна быть меньше 1.00'},
        max_digits=7,
        decimal_places=2
    )

    class Meta:
        model = Product
        fields = [
            'product',
            'description',
            'photo',
            'category',
            'rest',
            'price'
        ]


class SearchForm(forms.Form):
    search = forms.CharField(
        label='Поиск',
        max_length=250,
        required=False
    )

    class Meta:
        model = Product
        fields = [
            'product'
        ]
