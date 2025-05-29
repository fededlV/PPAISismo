from django.urls import path
from .boundaries import PantallaRevision


urlpatterns = [
    path('opcRegistrarResRevisionMan/', PantallaRevision.opcRegistrarResRevisionMan, name='opcRegistrarResRevisionMan'),
    path('tomarEvento/', PantallaRevision.tomarEvento, name='tomarEvento'),
    path('tomarRechazoVisualizacion/', PantallaRevision.tomarRechazoVisualizacion, name='tomarRechazoVisualizacion'),
    path('permitirModificarDatos/', PantallaRevision.permitirModificarDatos, name='permitirModificarDatos'),
    path('solicitarAccion/', PantallaRevision.solicitarAccion, name='solicitarAccion'),
    path('tomarAccionRechazarEvento/', PantallaRevision.tomarAccionRechazarEvento, name='tomarAccionRechazarEvento'),
]