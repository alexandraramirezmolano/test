from django import forms
from djsniper.sniper.models import NFTProject, Category


class DeveloperProjectForm(forms.ModelForm):
    developer = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

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
        super(DeveloperProjectForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nombre'})
        self.fields['contract_address'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contract Address'})
        self.fields['image'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Imagen'})
        self.fields['number_of_nfts'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Cantidad de bonos'})
        self.fields['supply'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Bonos disponibles'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Precio unitario'})
        self.fields['chain'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Chain'})
        self.fields['contract_abi'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contract ABI', 'rows': 5})
        self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Categoría'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Descripción', 'rows': 5})
        
        # divide the fields into two columns
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control col-md-6 flex-column'
