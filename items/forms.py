from django.forms import ModelForm
from django import forms
from .models import Actividad, Carpeta

class ActividadForm (forms.ModelForm):
    class Meta:
        model = Actividad
        fields =['nombre', 'hecho', 'carpeta']

class CarpetaForm (forms.ModelForm):
    class Meta:
        model= Carpeta
        fields =['carpeta']
    
    