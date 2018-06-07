from django import forms
from django.utils import timezone

from .models import Book


class BookForm(forms.ModelForm):
    publish_date = forms.DateField(
        widget=forms.SelectDateWidget(),
        label='Publish Date',
        initial=timezone.now()
    )
    class Meta:
        model = Book
        fields = (
            'title',
            'authors_info',
            'publish_date',
            'isbn',
            'price',
        )
