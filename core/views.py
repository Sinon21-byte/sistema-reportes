from django.shortcuts import render
from django.http import HttpResponse
from .forms import ReporteForm
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
from django.conf import settings
from django.core.mail import EmailMessage
from io import BytesIO
from PIL import Image

def formulario_view(request):
    if request.method == 'POST':
        form = ReporteForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data

            # --- Generar el DOCX en memoria ---
            tpl_path = settings.BASE_DIR / 'core' / 'plantillas' / 'reporte.docx'
            doc = DocxTemplate(tpl_path)

            # Contexto de texto
            context = {
                'fecha': cd['fecha'],
                'nombre': cd['nombre'],
                'parque': cd['parque'],
                # ... otros campos ...
            }

            # Helper para imágenes
            def mkimg(name):
                f = cd.get(name)
                if not f: return None
                img = Image.open(f)
                img.thumbnail((120*11.8, 105*11.8))
                bio = BytesIO()
                img.save(bio, format=img.format or 'PNG')
                bio.seek(0)
                return InlineImage(doc, bio, width=Mm(120), height=Mm(105))

            # Añade las imágenes al contexto (ejemplo)
            context.update({
                'imagen_ecm': mkimg('imagen_ecm'),
                # ... resto de campos imagen ...
            })

            # Fotos adicionales
            fotos = [mkimg(f'foto_adicional_{i}') for i in range(1,11) if cd.get(f'foto_adicional_{i}')]
            context['foto_adicional'] = fotos

            # Render y guarda a buffer
            doc.render(context)
            buf = BytesIO()
            doc.save(buf)
            buf.seek(0)
            report_bytes = buf.getvalue()

            # --- Enviar email ---
            subject = f"Reporte inspección {cd['parque']} realizado por {cd['nombre']}"
            body = "Reporte adjunto"
            to = ['nicolas.maruri@aedilestalinay.com']

            email = EmailMessage(
                subject=subject,
                body=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=to,
            )
            email.attach(
                filename=f"informe_{cd['parque']}.docx",
                content=report_bytes,
                mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            )
            email.send(fail_silently=False)

            # --- Devolver el .docx para descarga también si quieres ---
            resp = HttpResponse(
                report_bytes,
                content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            )
            resp['Content-Disposition'] = 'attachment; filename="informe_reporte.docx"'
            return resp

    else:
        form = ReporteForm()

    return render(request, 'core/formulario.html', {'form': form})
