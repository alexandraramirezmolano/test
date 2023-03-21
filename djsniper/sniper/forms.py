from django import forms
from .models import NFTProject, Category


class ProjectForm(forms.ModelForm):
    class Meta:
        model = NFTProject
        fields = ['name', 'contract_address', 'number_of_nfts', 'image', 'category', 'supply', 'price', 'chain', 'description', 'contract_abi']
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
        
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        
        # update widget attributes
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Name'})
        self.fields['contract_address'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contract Address'})
        self.fields['image'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Image'})
        self.fields['number_of_nfts'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Number of NFTs'})
        self.fields['supply'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Supply'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Price'})
        self.fields['chain'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Chain'})
        self.fields['contract_abi'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contract ABI', 'rows': 5})
        self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Category'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Description', 'rows': 5})
        
        # divide the fields into two columns
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control col-md-6 flex-column'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ConfirmForm(forms.Form):
    hidden = forms.HiddenInput()
