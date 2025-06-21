from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('formulario/', views.formulario_view, name='formulario'),
    path('actividades/', views.reporte_actividades_view, name='reporte_actividades'),
]