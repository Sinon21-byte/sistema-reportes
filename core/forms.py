from django import forms

OBS_CHOICES = [
    ('Con Observaciones', 'Con Observaciones'),
    ('Sin Observaciones', 'Sin Observaciones'),
]

class ReporteForm(forms.Form):
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    nombre = forms.CharField(max_length=100)
    parque = forms.CharField(max_length=100)

    inspeccion_compacto       = forms.ChoiceField(choices=OBS_CHOICES)
    comentario_compacto       = forms.CharField(
                                   required=False, widget=forms.Textarea)
    imagen_ecm                = forms.ImageField(required=False)

    inspeccion_reconectador   = forms.ChoiceField(choices=OBS_CHOICES)
    comentario_reconectador   = forms.CharField(
                                   required=False, widget=forms.Textarea)
    imagen_reconectador       = forms.ImageField(required=False)

    inspeccion_medidor        = forms.ChoiceField(choices=OBS_CHOICES)
    comentario_medidor        = forms.CharField(
                                   required=False, widget=forms.Textarea)
    imagen_medidor            = forms.ImageField(required=False)

    inspeccion_sala_control   = forms.ChoiceField(choices=OBS_CHOICES)
    comentario_sala_control   = forms.CharField(
                                   required=False, widget=forms.Textarea)
    imagen_sala_control       = forms.ImageField(required=False)

    inspeccion_linea_mt       = forms.ChoiceField(choices=OBS_CHOICES)
    comentario_linea_mt       = forms.CharField(
                                   required=False, widget=forms.Textarea)
    imagen_linea_mt           = forms.ImageField(required=False)

    inspeccion_ct             = forms.ChoiceField(choices=OBS_CHOICES)
    comentario_ct             = forms.CharField(
                                   required=False, widget=forms.Textarea)
    imagen_ct                 = forms.ImageField(required=False)

    inspeccion_inversores     = forms.ChoiceField(choices=OBS_CHOICES)
    comentario_inversores     = forms.CharField(
                                   required=False, widget=forms.Textarea)
    imagen_inversores         = forms.ImageField(required=False)

    inspeccion_modulos        = forms.ChoiceField(choices=OBS_CHOICES)
    comentario_modulos        = forms.CharField(
                                   required=False, widget=forms.Textarea)
    imagen_modulos            = forms.ImageField(required=False)

    nivel_soiling             = forms.ChoiceField(
                                   choices=[(f"{i}%",f"{i}%") for i in range(1,11)])
    imagen_soiling            = forms.ImageField()

    # fotos adicionales (hasta 10)
    foto_adicional_1          = forms.ImageField(required=False)
    foto_adicional_2          = forms.ImageField(required=False)
    # … repite hasta foto_adicional_10 …
    foto_adicional_10         = forms.ImageField(required=False)

    comentarios_supervisor    = forms.CharField(
                                   required=False, widget=forms.Textarea)
