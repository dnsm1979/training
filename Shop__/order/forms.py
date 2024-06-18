from django import forms
from django.core.exceptions import ValidationError

from .models import Order
from client.models import Client
from products.models import Products
from sellers.models import Sellers


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

    client = forms.ModelChoiceField(required=True, queryset=Client.objects.all())
    seller = forms.ModelChoiceField(required=True, queryset=Sellers.objects.all())
    product = forms.ModelChoiceField(required=True, queryset=Products.objects.all())


    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if Order.objects.filter(phone=phone).exists():
            raise ValidationError('Такой телефон уже есть')
        return phone