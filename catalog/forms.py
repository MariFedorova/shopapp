from django import forms

from catalog.models import Product, Version

stop_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class MixinForm:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ProductForm(MixinForm, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('user',)



    def clean_name(self):
        name = self.cleaned_data['name']
        for word in stop_words:
            if word in name.lower():
                raise forms.ValidationError('Нельзя использовать такие продукты')
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        for word in stop_words:
            if word in description.lower():
                raise forms.ValidationError('Нельзя использовать такое описание')
        return description


class VersionForm(MixinForm, forms.ModelForm):
    class Meta:
        model = Version
        exclude = ('product',)
