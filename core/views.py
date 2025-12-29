from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ReporteForm, ActividadesForm
from django.conf import settings
from .report_jobs import queue_activities_report, queue_inspection_report

def login_view(request):
    """Simple login page using credentials from settings."""
    error = False
    if request.method == 'GET':
        # Clear any existing session so the navigation
        # menu remains hidden on the login page
        request.session.flush()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == settings.USUARIO_WEB and password == settings.PASSWORD_WEB:
            request.session['authenticated'] = True
            request.session['usuario'] = username
            return redirect('formulario')
        error = True
    return render(request, 'core/login.html', {
        'error': error,
        'nombre': request.session.get('usuario')
    })

def formulario_view(request):
    if not request.session.get('authenticated'):
        return redirect('login')

    nombre = request.session.get('usuario')

    if request.method == 'POST':
        form = ReporteForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data

            def read_file(name):
                f = cd.get(name)
                if not f:
                    return None
                content = f.read()
                f.seek(0)
                return content

            report_data = {
                'fecha': cd['fecha'],
                'nombre': cd['nombre'],
                'parque': cd['parque'],
                'inspeccion_compacto': cd['inspeccion_compacto'],
                'comentario_compacto': cd.get('comentario_compacto', ''),
                'inspeccion_reconectador': cd['inspeccion_reconectador'],
                'comentario_reconectador': cd.get('comentario_reconectador', ''),
                'inspeccion_medidor': cd['inspeccion_medidor'],
                'comentario_medidor': cd.get('comentario_medidor', ''),
                'inspeccion_sala_control': cd['inspeccion_sala_control'],
                'comentario_sala_control': cd.get('comentario_sala_control', ''),
                'inspeccion_linea_mt': cd['inspeccion_linea_mt'],
                'comentario_linea_mt': cd.get('comentario_linea_mt', ''),
                'inspeccion_ct': cd['inspeccion_ct'],
                'comentario_ct': cd.get('comentario_ct', ''),
                'inspeccion_inversores': cd['inspeccion_inversores'],
                'comentario_inversores': cd.get('comentario_inversores', ''),
                'inspeccion_modulos': cd['inspeccion_modulos'],
                'comentario_modulos': cd.get('comentario_modulos', ''),
                'nivel_soiling': cd['nivel_soiling'],
                'comentarios_supervisor': cd.get('comentarios_supervisor', ''),
                'destinatario': cd.get('destinatario'),
                'nombre_archivo': cd['nombre_archivo'],
            }

            image_keys = [
                'imagen_ecm', 'imagen_reconectador', 'imagen_medidor',
                'imagen_sala_control', 'imagen_linea_mt', 'imagen_ct',
                'imagen_inversores', 'imagen_modulos', 'imagen_soiling',
            ]
            images = {key: read_file(key) for key in image_keys}
            photos = [read_file(f'foto_adicional_{i}') for i in range(1, 11)]

            queue_inspection_report(report_data, images, photos)

            # Redirigir para evitar reenvío al refrescar
            return redirect(f"{reverse('formulario')}?success=1")

    else:
        form = ReporteForm()

    mensaje_exito = request.GET.get('success') == '1'
    if mensaje_exito:
        request.session.flush()

    return render(request, 'core/formulario.html', {
        'form': form,
        'mensaje_exito': mensaje_exito,
        'nombre': nombre,
        'active_tab': 'formulario',
    })


def actividades_view(request):
    """Vista para generar el reporte de actividades"""
    if not request.session.get('authenticated'):
        return redirect('login')

    nombre = request.session.get('usuario')

    if request.method == 'POST':
        form = ActividadesForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data

            def read_file(name):
                f = cd.get(name)
                if not f:
                    return None
                content = f.read()
                f.seek(0)
                return content

            report_data = {
                'fecha': cd['fecha'],
                'nombre': cd['nombre'],
                'parque': cd['parque'],
                'resumen': cd.get('resumen', ''),
                'destinatario': cd.get('destinatario'),
                'nombre_archivo': cd['nombre_archivo'],
            }

            photos = [
                read_file(f'registro_fotografico_{i}') for i in range(1, 11)
            ]

            queue_activities_report(report_data, photos)

            return redirect(f"{reverse('actividades')}?success=1")
    else:
        form = ActividadesForm()

    mensaje_exito = request.GET.get('success') == '1'
    if mensaje_exito:
        request.session.flush()

    return render(request, 'core/reporte_actividades.html', {
        'form': form,
        'mensaje_exito': mensaje_exito,
        'nombre': nombre,
        'active_tab': 'actividades',
    })
