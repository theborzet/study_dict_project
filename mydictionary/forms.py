from django import forms

from mydictionary.models import Word

class WordCreateForm(forms.ModelForm):
    english = forms.CharField(label='Английский', widget=forms.TextInput(attrs={
        'class': "form-control py-2",
        'placeholder': "Введите слова на английском",
    }))
    translate = forms.CharField(label='Русский', widget=forms.TextInput(attrs={
        'class': "form-control py-2",
        'placeholder': "Введите перевод",
    }))
    class Meta:
        model = Word
        fields = ('english', 'translate',)