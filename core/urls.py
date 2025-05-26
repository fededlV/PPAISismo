from django.urls import path
from .boundaries import PantallaRevision


urlpatterns = [
    path('', PantallaRevision.home, name='home'),
    path('tomarOpcSeleccionada/', PantallaRevision.tomarOpcSeleccionada, name='tomarOpcSeleccionada'),
    path('tomarEvento/', PantallaRevision.tomarEvento, name='tomarEvento'),
    path('tomarRechazoVisualizacion/', PantallaRevision.tomarRechazoVisualizacion, name='tomarRechazoVisualizacion'),
    path('permitirModificarDatos/', PantallaRevision.permitirModificarDatos, name='permitirModificarDatos'),
    path('solicitarAccion/', PantallaRevision.solicitarAccion, name='solicitarAccion'),
    path('tomarAccionRechazarEvento/', PantallaRevision.tomarAccionRechazarEvento, name='tomarAccionRechazarEvento'),
]