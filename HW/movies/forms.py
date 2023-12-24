from django import forms
from . import models


class MovieForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = '__all__'
