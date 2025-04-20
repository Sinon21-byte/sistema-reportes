from django import forms

OBS_CHOICES = [
    ('Con Observaciones', 'Con Observaciones'),
    ('Sin Observaciones', 'Sin Observaciones'),
]

class ReporteForm(forms.Form):
    fecha = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date', 'class': 'form-control'
    }))
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    parque = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    destinatario = forms.EmailField(            # ← Nuevo campo
        required=False,
        label='Enviar copia a (email)',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ejemplo@dominio.com'
        })
    )

    # … el resto de tus campos sigue igual …
    inspeccion_compacto = forms.ChoiceField(
        label='Inspección ECM',
        choices=OBS_CHOICES,
        widget=forms.Select(attrs={'class':'form-control'})
    )
    comentario_compacto = forms.CharField(
        label='Comentario ECM',
        required=False,
        widget=forms.Textarea(attrs={'class':'form-control','rows':3})
    )
    imagen_ecm = forms.ImageField(
        label='Imagen ECM',
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class':'form-control','accept':'image/*'
        })
    )
    # … resto de campos sin cambios …
    comentarios_supervisor = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class':'form-control','rows':4})
    )
