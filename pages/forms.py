from django import forms

from .models import NewsEmailModel


class NewsEmailForm(forms.ModelForm):
    class Meta:
        model = NewsEmailModel
        fields = ('email',)
