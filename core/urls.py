from django.urls import path
from .boundaries import PantallaRevision
from .views import tomarEvento


urlpatterns = [
    path('', PantallaRevision.home, name='home'),
    path('tomarOpcSeleccionada/', PantallaRevision.tomarOpcSeleccionada, name='tomarOpcSeleccionada'),
    path('tomarEvento/<int:evento_id>/', tomarEvento, name='tomarEvento'),
]