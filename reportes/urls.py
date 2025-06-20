from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Tu formulario en la raíz
    path('', views.formulario_view, name='formulario'),
]

# Esto sirve MEDIA_URL durante el DEBUG para que InlineImage funcione
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
