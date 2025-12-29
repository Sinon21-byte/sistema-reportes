import logging
import threading
from io import BytesIO

from django.conf import settings
from django.core.mail import EmailMessage
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
from PIL import Image

from .email_utils import send_email_with_logging

logger = logging.getLogger(__name__)


def queue_inspection_report(data, images, photos):
    thread = threading.Thread(
        target=_generate_and_send_inspection_report,
        args=(data, images, photos),
        daemon=True,
    )
    thread.start()


def queue_activities_report(data, photos):
    thread = threading.Thread(
        target=_generate_and_send_activities_report,
        args=(data, photos),
        daemon=True,
    )
    thread.start()


def _generate_and_send_inspection_report(data, images, photos):
    dest = data.get('destinatario')
    if not dest:
        return

    try:
        tpl = settings.BASE_DIR / 'core' / 'plantillas' / 'reporte.docx'
        doc = DocxTemplate(tpl)

        context = {
            'fecha': data['fecha'],
            'nombre': data['nombre'],
            'parque': data['parque'],
            'inspeccion_compacto': data['inspeccion_compacto'],
            'comentario_compacto': data.get('comentario_compacto', ''),
            'inspeccion_reconectador': data['inspeccion_reconectador'],
            'comentario_reconectador': data.get('comentario_reconectador', ''),
            'inspeccion_medidor': data['inspeccion_medidor'],
            'comentario_medidor': data.get('comentario_medidor', ''),
            'inspeccion_sala_control': data['inspeccion_sala_control'],
            'comentario_sala_control': data.get('comentario_sala_control', ''),
            'inspeccion_linea_mt': data['inspeccion_linea_mt'],
            'comentario_linea_mt': data.get('comentario_linea_mt', ''),
            'inspeccion_ct': data['inspeccion_ct'],
            'comentario_ct': data.get('comentario_ct', ''),
            'inspeccion_inversores': data['inspeccion_inversores'],
            'comentario_inversores': data.get('comentario_inversores', ''),
            'inspeccion_modulos': data['inspeccion_modulos'],
            'comentario_modulos': data.get('comentario_modulos', ''),
            'nivel_soiling': data['nivel_soiling'],
            'comentarios_supervisor': data.get('comentarios_supervisor', ''),
        }

        for key, content in images.items():
            context[key] = _build_image(doc, content)

        context['foto_adicional'] = [
            _build_image(doc, content) for content in photos if content
        ]

        doc_bytes = _render_docx(doc, context)
        _send_report_email(
            subject=(
                f"Reporte inspección {data['parque']} realizado por {data['nombre']}"
            ),
            file_name=_build_file_name(data),
            dest=dest,
            doc_bytes=doc_bytes,
        )
    except Exception:
        logger.exception("Error al generar el reporte de inspección para %s.", dest)


def _generate_and_send_activities_report(data, photos):
    dest = data.get('destinatario')
    if not dest:
        return

    try:
        tpl = settings.BASE_DIR / 'core' / 'plantillas' / 'reporte2.docx'
        doc = DocxTemplate(tpl)

        context = {
            'fecha': data['fecha'],
            'nombre': data['nombre'],
            'parque': data['parque'],
            'resumen': data.get('resumen', ''),
        }

        context['foto_adicional'] = [
            _build_image(doc, content) for content in photos if content
        ]

        doc_bytes = _render_docx(doc, context)
        _send_report_email(
            subject=(
                f"Reporte actividades {data['parque']} realizado por {data['nombre']}"
            ),
            file_name=_build_file_name(data),
            dest=dest,
            doc_bytes=doc_bytes,
        )
    except Exception:
        logger.exception("Error al generar el reporte de actividades para %s.", dest)


def _build_image(doc, content):
    if not content:
        return None
    img = Image.open(BytesIO(content))
    img.thumbnail((int(120 * 11.8), int(105 * 11.8)))
    bio = BytesIO()
    img.save(bio, format=img.format or 'PNG')
    bio.seek(0)
    return InlineImage(doc, bio, width=Mm(120), height=Mm(105))


def _render_docx(doc, context):
    doc.render(context)
    buf = BytesIO()
    doc.save(buf)
    return buf.getvalue()


def _build_file_name(data):
    return (
        f"{data['fecha'].strftime('%y-%m-%d')}_"
        f"{data['parque']}_{data['nombre_archivo']}.docx"
    )


def _send_report_email(subject, file_name, dest, doc_bytes):
    mail = EmailMessage(
        subject=subject,
        body="Reporte adjunto",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[dest],
    )
    mail.attach(
        filename=file_name,
        content=doc_bytes,
        mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    )
    send_email_with_logging(mail)
