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

            # … generación del reporte en memoria (igual que antes) …
            tpl_path = settings.BASE_DIR / 'core' / 'plantillas' / 'reporte.docx'
            doc = DocxTemplate(tpl_path)
            # … context con textos …
            # … mkimg helper …
            # … context.update con mkimg incluyendo 'imagen_soiling' …
            # … foto_adicional …
            doc.render(context)
            buf = BytesIO(); doc.save(buf); buf.seek(0)
            report_bytes = buf.getvalue()

            # 7) Envío de email **solo si el usuario puso un destinatario**
            to_addr = cd.get('destinatario')
            if to_addr:
                try:
                    subject = f"Reporte inspección {cd['parque']} realizado por {cd['nombre']}"
                    body = "Reporte adjunto"
                    email = EmailMessage(subject, body, settings.DEFAULT_FROM_EMAIL, [to_addr])
                    email.attach(
                        filename=f"informe_{cd['parque']}.docx",
                        content=report_bytes,
                        mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
                    )
                    email.send(fail_silently=True)  # fail_silently para no crashear
                except Exception:
                    # opcional: loggear el fallo pero no interrumpir
                    pass

            # 8) Devolver siempre el .docx para descarga
            response = HttpResponse(
                report_bytes,
                content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            )
            response['Content-Disposition'] = f'attachment; filename="informe_{cd["parque"]}.docx"'
            return response

    else:
        form = ReporteForm()

    return render(request, 'core/formulario.html', {'form': form})
