from django import forms
from djsniper.sniper.models import NFTProject


class EnterpriseProjectForm(forms.ModelForm):
    private = forms.BooleanField(label='Privado', required=False)

    class Meta:
        model = NFTProject
        fields = ['name', 'image', 'category', 'supply', 'price', 'description', 'enterprise_id', 'private', 'developer_id']
        labels = {
            'name': 'Nombre',
            'image': 'Imagen',
            'category': 'Categoría',
            'supply': 'Disponibles',
            'price': 'Precio unitario',
            'description': 'Descripción',
            'private': '¿Es privado?',
            'developer_id' : 'Desarrollador',
            'enterprise_id' : ''
        }
        error_messages = {
            'name': {'required': 'Por favor, introduzca un nombre para el proyecto.'},
            'price': {'required': 'Por favor ingrese un precio para el proyecto'},
            'description': {'required': 'Por favor ingrese una descripción para el proyecto'},
        }

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        super(EnterpriseProjectForm, self).__init__(*args, **kwargs)
        self.fields['enterprise_id'].initial = request.user.id
        # Update widget attributes
        self.fields['name'].widget.attrs.update({'class': 'form-control  mt-2', 'placeholder': 'Nombre'})
        self.fields['image'].widget.attrs.update({'class': 'form-control mt-2', 'placeholder': 'Imagen'})
        self.fields['supply'].widget.attrs.update({'class': 'form-control mt-2', 'placeholder': 'Bonos disponibles'})
        self.fields['price'].widget.attrs.update({'class': 'form-control mt-2', 'placeholder': 'Precio unitario'})
        self.fields['category'].widget.attrs.update({'class': 'form-control mt-2', 'placeholder': 'Categoría'})
        self.fields['description'].widget.attrs.update({'class': 'form-control mt-2', 'placeholder': 'Descripción'})
        self.fields['enterprise_id'].widget.attrs.update({'class': 'form-control mt-2', 'placeholder': 'Descripción', 'style': 'display: none'})
        self.fields['developer_id'].widget.attrs.update({'class': 'form-control mt-2','placeholder': 'Desarrollador'})
        self.fields['private'].widget.attrs.update({'class': 'form-check-input mt-2'})
