from django import forms

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl, border'


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('product_id', 'product_name', 'company',
                  'business_area', 'price', 'in_market',)


        widgets = {
            'product_id': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'product_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'company': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'business_area': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'in_market': forms.NullBooleanSelect(attrs={
                'class': INPUT_CLASSES
            }),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('product_name', 'company', 'price',
                  'business_area', 'in_market')

        widgets = {
            'product_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'company': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'business_area': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'in_market': forms.NullBooleanSelect(attrs={
                'class': INPUT_CLASSES
            }),
        }
