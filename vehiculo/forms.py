# importar la librería estándar de Django Forms
from django import forms
# Local
from .models import VehiculoModel

class VehiculoForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta:
        model = VehiculoModel 
        fields = "__all__"