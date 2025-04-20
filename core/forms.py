from django import forms

OBS_CHOICES = [
    ('Con Observaciones', 'Con Observaciones'),
    ('Sin Observaciones', 'Sin Observaciones'),
]

class ReporteForm(forms.Form):
    # Metadatos
    fecha = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date',
        'class': 'form-control',
    }))
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    parque = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    # Nuevo: destinatario opcional
    destinatario = forms.EmailField(
        required=False,
        label='Enviar copia a (email)',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ejemplo@dominio.com'
        })
    )

    # Inspección equipo compacto de medida
    inspeccion_compacto = forms.ChoiceField(
        label='Inspección ECM',
        choices=OBS_CHOICES,
        widget=forms.Select(attrs={'class':'form-control'})
    )
    comentario_compacto = forms.CharField(
        label='Comentario ECM',
        required=False,
        widget=forms.Textarea(attrs={'class':'form-control','rows':3})
    )
    imagen_ecm = forms.ImageField(
        label='Imagen ECM',
        required=False,
        widget=forms.ClearableFileInput(attrs={'class':'form-control','accept':'image/*'})
    )

    # Inspección reconectador
    inspeccion_reconectador = forms.ChoiceField(choices=OBS_CHOICES,
        widget=forms.Select(attrs={'class':'form-control'}))
    comentario_reconectador = forms.CharField(required=False,
        widget=forms.Textarea(attrs={'class':'form-control','rows':3}))
    imagen_reconectador = forms.ImageField(required=False,
        widget=forms.ClearableFileInput(attrs={'class':'form-control','accept':'image/*'}))

    # Inspección medidor de energía
    inspeccion_medidor = forms.ChoiceField(choices=OBS_CHOICES,
        widget=forms.Select(attrs={'class':'form-control'}))
    comentario_medidor = forms.CharField(required=False,
        widget=forms.Textarea(attrs={'class':'form-control','rows':3}))
    imagen_medidor = forms.ImageField(required=False,
        widget=forms.ClearableFileInput(attrs={'class':'form-control','accept':'image/*'}))

    # Inspección sala de control
    inspeccion_sala_control = forms.ChoiceField(choices=OBS_CHOICES,
        widget=forms.Select(attrs={'class':'form-control'}))
    comentario_sala_control = forms.CharField(required=False,
        widget=forms.Textarea(attrs={'class':'form-control','rows':3}))
    imagen_sala_control = forms.ImageField(required=False,
        widget=forms.ClearableFileInput(attrs={'class':'form-control','accept':'image/*'}))

    # Inspección línea eléctrica MT
    inspeccion_linea_mt = forms.ChoiceField(label='Inspección LMT',
        choices=OBS_CHOICES,
        widget=forms.Select(attrs={'class':'form-control'}))
    comentario_linea_mt = forms.CharField(label='Comentario LMT', required=False,
        widget=forms.Textarea(attrs={'class':'form-control','rows':3}))
    imagen_linea_mt = forms.ImageField(label='Imagen LMT', required=False,
        widget=forms.ClearableFileInput(attrs={'class':'form-control','accept':'image/*'}))

    # Inspección transformador MT
    inspeccion_ct = forms.ChoiceField(label='Inspección CDT',
        choices=OBS_CHOICES,
        widget=forms.Select(attrs={'class':'form-control'}))
    comentario_ct = forms.CharField(label='Comentarios CDT', required=False,
        widget=forms.Textarea(attrs={'class':'form-control','rows':3}))
    imagen_ct = forms.ImageField(label='Imagen CDT', required=False,
        widget=forms.ClearableFileInput(attrs={'class':'form-control','accept':'image/*'}))

    # Inspección inversores
    inspeccion_inversores = forms.ChoiceField(choices=OBS_CHOICES,
        widget=forms.Select(attrs={'class':'form-control'}))
    comentario_inversores = forms.CharField(required=False,
        widget=forms.Textarea(attrs={'class':'form-control','rows':3}))
    imagen_inversores = forms.ImageField(required=False,
        widget=forms.ClearableFileInput(attrs={'class':'form-control','accept':'image/*'}))

    # Inspección módulos
    inspeccion_modulos = forms.ChoiceField(choices=OBS_CHOICES,
        widget=forms.Select(attrs={'class':'form-control'}))
    comentario_modulos = forms.CharField(required=False,
        widget=forms.Textarea(attrs={'class':'form-control','rows':3}))
    imagen_modulos = forms.ImageField(required=False,
        widget=forms.ClearableFileInput(attrs={'class':'form-control','accept':'image/*'}))

    # Nivel de soiling
    nivel_soiling = forms.ChoiceField(
        choices=[(f"{i}%", f"{i}%") for i in range(1,11)],
        widget=forms.Select(attrs={'class':'form-control'})
    )
    imagen_soiling = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class':'form-control','accept':'image/*'})
    )

    # Fotos adicionales 1–10
    foto_adicional_1 = forms.ImageField(required=False,
        widget=forms.ClearableFileInput(attrs={'class':'form-control','accept':'image/*'}))
    foto_adicional_2 = forms.ImageField(required=False,
        widget=forms.ClearableFileInput(attrs={'class':'form-control','accept':'image/*'}))
    foto_adicional_3 = forms.ImageField(required=False,
        widget=forms.ClearableFileInput(attrs={'class':'form-control','accept':'image/*'}))
    foto_adicional_4 = forms.ImageField(required=False,
        widget=forms.ClearableFileInput(attrs={'class':'form-control','accept':'image/*'}))
    foto_adicional_5 = forms.ImageField(required=False,
        widget=forms.ClearableFileInput(attrs={'class':'form-control','accept':'image/*'}))
    foto_adicional_6 = forms.ImageField(required=False,
        widget=forms.ClearableFileInput(attrs={'class':'form-control','accept':'image/*'}))
    foto_adicional_7 = forms.ImageField(required=False,
        widget=forms.ClearableFileInput(attrs={'class':'form-control','accept':'image/*'}))
    foto_adicional_8 = forms.ImageField(required=False,
        widget=forms.ClearableFileInput(attrs={'class':'form-control','accept':'image/*'}))
    foto_adicional_9 = forms.ImageField(required=False,
        widget=forms.ClearableFileInput(attrs={'class':'form-control','accept':'image/*'}))
    foto_adicional_10 = forms.ImageField(required=False,
        widget=forms.ClearableFileInput(attrs={'class':'form-control','accept':'image/*'}))

    # Comentarios supervisor
    comentarios_supervisor = forms.CharField(required=False,
        widget=forms.Textarea(attrs={'class':'form-control','rows':4}))
