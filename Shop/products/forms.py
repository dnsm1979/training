from django import forms
from django.core.exceptions import ValidationError

from .models import Products


class ProductsForm(forms.ModelForm):
    price = forms.IntegerField(min_value=0)
    quantity = forms.IntegerField(min_value=0)
    class Meta:
        model = Products
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super(ProductsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_title(self):

        title = self.cleaned_data.get('title')
        if not self.instance:
            if Products.objects.filter(title=title).exists():
                raise ValidationError('Такой товар уже есть')
        return title