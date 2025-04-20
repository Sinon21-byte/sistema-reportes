from django.shortcuts import render
from django.http import HttpResponse
from .forms import ReporteForm
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
from django.conf import settings
from io import BytesIO
from PIL import Image

def formulario_view(request):
    if request.method == 'POST':
        form = ReporteForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data

            # 1) Carga de plantilla
            tpl_path = settings.BASE_DIR / 'core' / 'plantillas' / 'reporte.docx'
            doc = DocxTemplate(tpl_path)

            # 2) Contexto con campos de texto
            context = {
                'fecha':                   cd['fecha'],
                'nombre':                  cd['nombre'],
                'parque':                  cd['parque'],

                'inspeccion_compacto':     cd['inspeccion_compacto'],
                'comentario_compacto':     cd.get('comentario_compacto', ''),

                'inspeccion_reconectador': cd['inspeccion_reconectador'],
                'comentario_reconectador': cd.get('comentario_reconectador', ''),

                'inspeccion_medidor':      cd['inspeccion_medidor'],
                'comentario_medidor':      cd.get('comentario_medidor', ''),

                'inspeccion_sala_control': cd['inspeccion_sala_control'],
                'comentario_sala_control': cd.get('comentario_sala_control', ''),

                'inspeccion_linea_mt':     cd['inspeccion_linea_mt'],
                'comentario_linea_mt':     cd.get('comentario_linea_mt', ''),

                'inspeccion_ct':           cd['inspeccion_ct'],
                'comentario_ct':           cd.get('comentario_ct', ''),

                'inspeccion_inversores':   cd['inspeccion_inversores'],
                'comentario_inversores':   cd.get('comentario_inversores', ''),

                'inspeccion_modulos':      cd['inspeccion_modulos'],
                'comentario_modulos':      cd.get('comentario_modulos', ''),

                'nivel_soiling':           cd['nivel_soiling'],
                'comentarios_supervisor':  cd.get('comentarios_supervisor', ''),
            }

            # 3) Helper para redimensionar e insertar imágenes a 120×105 mm
            def mkimg(field_name):
                uploaded = cd.get(field_name)
                if not uploaded:
                    return None
                img = Image.open(uploaded)
                # Convertir mm→px (≈11.8 px/mm a 300 dpi)
                max_w_px = int(120 * 11.8)
                max_h_px = int(105 * 11.8)
                img.thumbnail((max_w_px, max_h_px))
                bio = BytesIO()
                fmt = img.format or 'PNG'
                img.save(bio, format=fmt)
                bio.seek(0)
                return InlineImage(doc, bio, width=Mm(120), height=Mm(105))

            # 4) Carga de imágenes principales
            context.update({
                'imagen_ecm':            mkimg('imagen_ecm'),
                'imagen_reconectador':   mkimg('imagen_reconectador'),
                'imagen_medidor':        mkimg('imagen_medidor'),
                'imagen_sala_control':   mkimg('imagen_sala_control'),
                'imagen_linea_mt':       mkimg('imagen_linea_mt'),
                'imagen_ct':             mkimg('imagen_ct'),
                'imagen_inversores':     mkimg('imagen_inversores'),
                'imagen_modulos':        mkimg('imagen_modulos'),
                'imagen_soiling':        mkimg('imagen_soiling'),
            })

            # 5) Fotos adicionales (hasta 10)
            fotos = []
            for i in range(1, 11):
                img_field = mkimg(f'foto_adicional_{i}')
                if img_field:
                    fotos.append(img_field)
            context['foto_adicional'] = fotos

            # 6) Render y envío del .docx
            doc.render(context)
            buf = BytesIO()
            doc.save(buf)
            buf.seek(0)
            resp = HttpResponse(
                buf.read(),
                content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            )
            resp['Content-Disposition'] = 'attachment; filename="informe_reporte.docx"'
            return resp

    else:
        form = ReporteForm()

    return render(request, 'core/formulario.html', {'form': form})
