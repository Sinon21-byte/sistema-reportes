import logging
import threading

logger = logging.getLogger(__name__)


def send_email_with_logging(message):
    try:
        message.send(fail_silently=False)
        logger.info("Reporte enviado por correo a %s.", ", ".join(message.to))
    except Exception:
        logger.exception(
            "Error al enviar el reporte por correo a %s.",
            ", ".join(message.to),
        )


def send_email_async(message):
    def _send():
        send_email_with_logging(message)

    thread = threading.Thread(target=_send, daemon=True)
    thread.start()
