from django import forms
from . import models, parser


class ParserForm(forms.Form):
    MEDIA_CHOICES = ('cars.kg', 'cars.kg')
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = ['media_type']

    def parser_data(self):
        if self.data['media_type'] == 'cars.kg':
            cars_parser = parser.parser_cars()
            for i in cars_parser:
                models.CarsModel.objects.create(**i)
