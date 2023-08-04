from django import forms

from item.models import Company

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl, border'


class NewCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('company_id', 'company_name', 'director', 'email',
                  'business_area', 'turnover_per_year', 'is_active',
                  'tax')

        widgets = {
            'company_id': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'company_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'director': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'email': forms.EmailInput(attrs={
                'class': INPUT_CLASSES
            }),
            'business_area': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'turnover_per_year': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'tax': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'is_active': forms.NullBooleanSelect(attrs={
                'class': INPUT_CLASSES
            }),
        }


class EditCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('company_name', 'director', 'email',
                  'business_area', 'turnover_per_year',
                  'is_active', 'tax')

        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'director': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'email': forms.EmailInput(attrs={
                'class': INPUT_CLASSES
            }),
            'business_area': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'turnover_per_year': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'tax': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'is_active': forms.NullBooleanSelect(attrs={
                'class': INPUT_CLASSES
            }),
        }
