from django import forms
from django.core.exceptions import ValidationError

from .models import Positions


class PositionsForm(forms.ModelForm):
    class Meta:
        model = Positions
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super(PositionsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_title(self):
        phone = self.cleaned_data.get('phone')
        if Positions.objects.filter(phone=phone).exists():
            raise ValidationError('Такой телефон уже есть')
        return phone