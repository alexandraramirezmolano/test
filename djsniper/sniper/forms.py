from django import forms
from .models import NFTProject, Category


class ProjectForm(forms.ModelForm):
    class Meta:
        model = NFTProject
        fields = '__all__'
        widgets = {
            'contract_address': forms.TextInput(attrs={'class': 'form-control'}),
            'contract_abi': forms.Textarea(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'number_of_nfts': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'supply': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'chain': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ConfirmForm(forms.Form):
    hidden = forms.HiddenInput()
