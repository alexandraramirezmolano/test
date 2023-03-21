from django import forms
from .models import NFTProject, Category


class ProjectForm(forms.ModelForm):
    class Meta:
        model = NFTProject
        fields = '__all__'
        widgets = {
            'contract_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contract Address'}),
            'contract_abi': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contract ABI'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'number_of_nfts': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of NFTs'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Image'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'supply': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Supply'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'chain': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Chain'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }
        labels = {
            'contract_address': 'Contrato',
            'contract_abi': 'ABI del Contrato',
            'name': 'Nombre',
            'number_of_nfts': 'Cantidad de bonos',
            'image': 'Imagen',
            'category': 'Categoría',
            'supply': 'Disponibles',
            'price': 'Precio unitario',
            'chain': 'Cadena',
            'description': 'Descripción',
        }
        error_messages = {
            'name': {'required': 'Por favor, introduzca un nombre para el proyecto.'},
            'number_of_nfts': {'required': 'Ingrese el número de bonos para el proyecto'},
            'price': {'required': 'Por favor ingrese un precio para el proyecto'},
            'description': {'required': 'Por favor ingrese una descripción para el proyecto'},
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ConfirmForm(forms.Form):
    hidden = forms.HiddenInput()
