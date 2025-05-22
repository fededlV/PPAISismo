from django.urls import path
from .views import home, tomarOpcSeleccionada, tomarEvento

urlpatterns = [
    path('', home, name='home'),
    path('tomarOpcSeleccionada/', tomarOpcSeleccionada, name='tomarOpcSeleccionada'),
    path('tomarEvento/', tomarEvento, name='tomarEvento'),
]