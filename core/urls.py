from django.urls import path
from .boundaries.PantallaRevision import PantallaRevision

PantallaRevision = PantallaRevision()
# core/urls.py
urlpatterns = [
    path('opcRegistrarResRevisionMan/', PantallaRevision.opcRegistrarResRevisionMan, name='opcRegistrarResRevisionMan'), # llama al 1
    path('tomarEvento/', PantallaRevision.tomarEvento, name='tomarEvento'), # llama al 13
    path('tomarRechazoVisualizacion/', PantallaRevision.tomarRechazoVisualizacion, name='tomarRechazoVisualizacion'),
    path('permitirModificarDatos/', PantallaRevision.permitirModificarDatos, name='permitirModificarDatos'),
    path('solicitarAccion/', PantallaRevision.solicitarAccion, name='solicitarAccion'),
    path('tomarAccionRechazarEvento/', PantallaRevision.tomarAccionRechazarEvento, name='tomarAccionRechazarEvento'),
]