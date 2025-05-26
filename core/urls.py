from django.urls import path
from .boundaries import PantallaRevision


urlpatterns = [
    path('', PantallaRevision.home, name='home'),
    path('tomarOpcSeleccionada/', PantallaRevision.tomarOpcSeleccionada, name='tomarOpcSeleccionada'),
    path('tomarEvento/', PantallaRevision.tomarEvento, name='tomarEvento'),
    path('obtenerDatoslasificacion', PantallaRevision.obtenerDatosClasificacion, name='obtenerDatosClasificacion'),
]