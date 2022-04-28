

from django import forms

from .models import Capataz


class CapatazForm(forms.ModelForm):
    apellido = forms.CharField(
        label="Apellido", required=True)
    
    nombre = forms.CharField(
        label="Nombre", required=True)

    def __init__(self, *args, **kwargs):
        super(CapatazForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'pure-input-1'
            })

    class Meta:
        model = Capataz
        fields = ['apellido', 'nombre']
    
