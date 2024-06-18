from django import forms
from django.core.exceptions import ValidationError

from .models import Sellers


class SellersForm(forms.ModelForm):
    class Meta:
        model = Sellers
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super(SellersForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_title(self):
        phone = self.cleaned_data.get('phone')
        if Sellers.objects.filter(phone=phone).exists():
            raise ValidationError('Такой телефон уже есть')
        return phone