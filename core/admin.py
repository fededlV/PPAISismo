from django.contrib import admin
from .entities.AlcanceSismico import AlcanceSismico
from .entities.CambioEstado import CambioEstado
from .entities.ClasificacionSismo import ClasificacionSismo
from .entities.DetalleMuestraSismica import DetalleMuestraSismica
from .entities.Empleado import Empleado
from .entities.EstacionSismologica import EstacionSismologica
from .entities.Estado import Estado
from .entities.EventoSismico import EventoSismico
from .entities.OrigenDeGeneracion import OrigenDeGeneracion
from .entities.Sismografo import Sismografo
from .entities.TipoDeDato import TipoDeDato
from .entities.Usuario import Usuario
from .entities.MuestraSismica import MuestraSismica
from .entities.SerieTemporal import SerieTemporal

admin.site.register(AlcanceSismico)
admin.site.register(CambioEstado)
admin.site.register(ClasificacionSismo)
admin.site.register(DetalleMuestraSismica)
admin.site.register(Empleado)
admin.site.register(EstacionSismologica)
admin.site.register(Estado)
admin.site.register(EventoSismico)
admin.site.register(OrigenDeGeneracion)
admin.site.register(Sismografo)
admin.site.register(TipoDeDato)
admin.site.register(Usuario)
admin.site.register(MuestraSismica)
admin.site.register(SerieTemporal)



