from django.urls import path
from .boundaries.PantallaRevision import PantallaRevision
from.views import home

pantallaRevision= PantallaRevision()
# core/urls.py
urlpatterns = [
    path('', home, name='home'),
    path('opcRegistrarResRevisionMan/', pantallaRevision.opcRegistrarResRevisionMan, name='opcRegistrarResRevisionMan'), # llama al 1
    path('tomarEvento/', pantallaRevision.tomarEvento, name='tomarEvento'), # llama al 13
    
    path('permitirVisualizarMapa/', pantallaRevision.permitirVisualizarMapa, name='permitirVisualizarMapa'),
    path('tomarRechazoVisualizacion/',pantallaRevision.tomarRechazoVisualizacion, name='tomarRechazoVisualizacion'),
    
    path('permitirModificarDatos/', PantallaRevision.permitirModificarDatos, name='permitirModificarDatos'),
    path('solicitarAccion/', PantallaRevision.solicitarAccion, name='solicitarAccion'),
    path('tomarAccionRechazarEvento/', PantallaRevision.tomarAccionRechazarEvento, name='tomarAccionRechazarEvento'),
]