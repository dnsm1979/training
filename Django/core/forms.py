from django import forms
from .models import Branch, Feedback
from django.core.validators import ValidationError


class BranchForm(forms.Form):
    title = forms.CharField(max_length=100, min_length=2, label='Заголовок')
    text = forms.CharField(max_length=500, required=True, label='Текст', widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if Branch.objects.filter(title=title).exists():
            raise ValidationError('Такой заголовок уже есть!')
        return title

class NewsForm(forms.Form):
    title = forms.CharField(max_length=100, min_length=2, label='Заголовок')
    anons = forms.CharField(max_length=200, required=True, label='Анонс')
    text = forms.CharField(max_length=500, required=True, label='Текст', widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if Branch.objects.filter(title=title).exists():
            raise ValidationError('Такой заголовок уже есть!')
        return title

class FeedBackForm(forms.Form):
    title = forms.CharField(max_length=100, min_length=2, label='Заголовок')
    text = forms.CharField(max_length=500, required=True, label='Текст', widget=forms.Textarea)
    class Meta:
        model = Branch
        fields = ['title', 'text']


class FeedBackModelForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['title', 'text']
