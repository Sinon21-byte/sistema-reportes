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

    # Para cada inspección:
    inspeccion_compacto = forms.ChoiceField(choices=OBS_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    comentario_compacto = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','rows':3}))
    imagen_ecm = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={
        'class':'form-control','accept':'image/*','capture':'environment'
    }))

    inspeccion_reconectador = forms.ChoiceField(choices=OBS_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    comentario_reconectador = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','rows':3}))
    imagen_reconectador = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={
        'class':'form-control','accept':'image/*','capture':'environment'
    }))

    inspeccion_medidor = forms.ChoiceField(choices=OBS_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    comentario_medidor = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','rows':3}))
    imagen_medidor = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={
        'class':'form-control','accept':'image/*','capture':'environment'
    }))

    inspeccion_sala_control = forms.ChoiceField(choices=OBS_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    comentario_sala_control = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','rows':3}))
    imagen_sala_control = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={
        'class':'form-control','accept':'image/*','capture':'environment'
    }))

    inspeccion_linea_mt = forms.ChoiceField(choices=OBS_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    comentario_linea_mt = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','rows':3}))
    imagen_linea_mt = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={
        'class':'form-control','accept':'image/*','capture':'environment'
    }))

    inspeccion_ct = forms.ChoiceField(choices=OBS_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    comentario_ct = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','rows':3}))
    imagen_ct = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={
        'class':'form-control','accept':'image/*','capture':'environment'
    }))

    inspeccion_inversores = forms.ChoiceField(choices=OBS_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    comentario_inversores = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','rows':3}))
    imagen_inversores = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={
        'class':'form-control','accept':'image/*','capture':'environment'
    }))

    inspeccion_modulos = forms.ChoiceField(choices=OBS_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    comentario_modulos = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','rows':3}))
    imagen_modulos = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={
        'class':'form-control','accept':'image/*','capture':'environment'
    }))

    nivel_soiling = forms.ChoiceField(choices=[(f"{i}%",f"{i}%") for i in range(1,11)], widget=forms.Select(attrs={'class':'form-control'}))
    imagen_soiling = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        'class':'form-control','accept':'image/*','capture':'environment'
    }))

    # Fotos adicionales 1–10
    for i in range(1, 11):
        vars()[f'foto_adicional_{i}'] = forms.ImageField(
            required=False,
            widget=forms.ClearableFileInput(attrs={
                'class':'form-control','accept':'image/*','capture':'environment'
            })
        )

    comentarios_supervisor = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','rows':4}))
