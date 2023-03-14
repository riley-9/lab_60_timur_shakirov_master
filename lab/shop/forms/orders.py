from django import forms
from django.forms import widgets

from shop.models import Order


class OrderForm(forms.ModelForm):
    error_css_class = 'error'
    label_css_class = 'label'

    name = forms.CharField(
        label='Имя',
        max_length=100,
        required=True,
        widget=widgets.TextInput(attrs={
            'class': 'form-control mt-3',
            'style': 'max-width: 750px;',
        })
    )
    phone = forms.CharField(
        label='Телефон',
        max_length=150,
        required=False,
        widget=widgets.TextInput(attrs={
            'class': 'form-control mt-3',
            'style': 'max-width: 750px;',
        })
    )
    address = forms.CharField(
        label='Адрес',
        max_length=300,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control mt-3',
            'style': 'max-width: 750px;',
        })
    )

    class Meta:
        model = Order
        fields = [
            'name',
            'phone',
            'address'
        ]
