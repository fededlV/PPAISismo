from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime, timedelta
from core.entities.Estado import Estado
from core.entities.AlcanceSismo import AlcanceSismo
from core.entities.ClasificacionSismo import ClasificacionSismo
from core.entities.OrigenDeGeneracion import OrigenDeGeneracion
from core.entities.Empleado import Empleado
from core.entities.EventoSismico import EventoSismico
from core.entities.CambioEstado import CambioEstado
from core.entities.EstacionSismologica import EstacionSismologica
from core.entities.Sismografo import Sismografo
from core.entities.SerieTemporal import SerieTemporal
from core.entities.TipoDeDato import TipoDeDato


class Command(BaseCommand):
    help = 'Carga datos de prueba para el sistema de monitoreo sísmico'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Iniciando carga de datos de prueba...'))

        # Crear Estados
        estados = [
            {'ambito': 'EventoSismico', 'nombreEstado': 'AutoDetectado'},
            {'ambito': 'EventoSismico', 'nombreEstado': 'EnRevision'},
            {'ambito': 'EventoSismico', 'nombreEstado': 'Revisado'},
            {'ambito': 'EventoSismico', 'nombreEstado': 'Bloqueado'},
            {'ambito': 'EventoSismico', 'nombreEstado': 'Rechazado'},
        ]
        
        for estado_data in estados:
            estado, created = Estado.objects.get_or_create(**estado_data)
            if created:
                self.stdout.write(f'  ✓ Estado creado: {estado.nombreEstado}')

        # Crear Alcances de Sismo
        alcances = [
            {'nombre': 'Local', 'descripcion': 'Sismo con alcance local, afecta una zona específica'},
            {'nombre': 'Regional', 'descripcion': 'Sismo con alcance regional, afecta varias provincias'},
            {'nombre': 'Nacional', 'descripcion': 'Sismo con alcance nacional, afecta todo el país'},
            {'nombre': 'Internacional', 'descripcion': 'Sismo con alcance internacional, afecta múltiples países'},
        ]
        
        for alcance_data in alcances:
            alcance, created = AlcanceSismo.objects.get_or_create(**alcance_data)
            if created:
                self.stdout.write(f'  ✓ Alcance creado: {alcance.nombre}')

        # Crear Clasificaciones de Sismo
        clasificaciones = [
            {'nombre': 'Superficial', 'kmProfundidadDesde': 0.0, 'kmProfundidadHasta': 70.0},
            {'nombre': 'Intermedio', 'kmProfundidadDesde': 70.0, 'kmProfundidadHasta': 300.0},
            {'nombre': 'Profundo', 'kmProfundidadDesde': 300.0, 'kmProfundidadHasta': 700.0},
        ]
        
        for clasificacion_data in clasificaciones:
            clasificacion, created = ClasificacionSismo.objects.get_or_create(**clasificacion_data)
            if created:
                self.stdout.write(f'  ✓ Clasificación creada: {clasificacion.nombre}')

        # Crear Orígenes de Generación
        origenes = [
            {'descripcion': 'Ruptura de falla tectónica', 'nombre': 'Tectónico'},
            {'descripcion': 'Actividad volcánica', 'nombre': 'Volcánico'},
            {'descripcion': 'Colapso de cavidades subterráneas', 'nombre': 'Colapso'},
            {'descripcion': 'Actividad humana como minería o explosiones', 'nombre': 'Inducido'},
        ]
        
        for origen_data in origenes:
            origen, created = OrigenDeGeneracion.objects.get_or_create(**origen_data)
            if created:
                self.stdout.write(f'  ✓ Origen creado: {origen.nombre}')

        # Crear Empleados
        empleados = [
            {
                'nombre': 'Juan Carlos',
                'apellido': 'Rodríguez',
                'mail': 'juan.rodriguez@sismologia.gov.ar',
                'telefono': '+54-11-4567-8901'
            },
            {
                'nombre': 'María Elena',
                'apellido': 'González',
                'mail': 'maria.gonzalez@sismologia.gov.ar',
                'telefono': '+54-11-4567-8902'
            },
            {
                'nombre': 'Carlos Alberto',
                'apellido': 'Fernández',
                'mail': 'carlos.fernandez@sismologia.gov.ar',
                'telefono': '+54-11-4567-8903'
            },
        ]
        
        for empleado_data in empleados:
            empleado, created = Empleado.objects.get_or_create(
                mail=empleado_data['mail'],
                defaults=empleado_data
            )
            if created:
                self.stdout.write(f'  ✓ Empleado creado: {empleado.nombre} {empleado.apellido}')

        # Crear Estaciones Sismológicas
        estaciones = [
            {
                'nombre': 'Estación Buenos Aires',
                'latitud': -34.6118,
                'longitud': -58.3960
            },
            {
                'nombre': 'Estación Mendoza',
                'latitud': -32.8908,
                'longitud': -68.8272
            },
            {
                'nombre': 'Estación San Juan',
                'latitud': -31.5375,
                'longitud': -68.5364
            },
        ]
        
        for estacion_data in estaciones:
            estacion, created = EstacionSismologica.objects.get_or_create(**estacion_data)
            if created:
                self.stdout.write(f'  ✓ Estación creada: {estacion.nombre}')

        # Crear Tipos de Dato
        tipos_dato = [
            {'descripcion': 'Velocidad del suelo', 'nombre': 'Velocidad'},
            {'descripcion': 'Aceleración del suelo', 'nombre': 'Aceleración'},
            {'descripcion': 'Desplazamiento del suelo', 'nombre': 'Desplazamiento'},
        ]
        
        for tipo_data in tipos_dato:
            tipo, created = TipoDeDato.objects.get_or_create(**tipo_data)
            if created:
                self.stdout.write(f'  ✓ Tipo de dato creado: {tipo.nombre}')

        # Crear Sismógrafos
        for estacion in EstacionSismologica.objects.all():
            for tipo_dato in TipoDeDato.objects.all():
                sismografo_data = {
                    'frecuenciaMuestreo': 100.0,
                    'nombre': f'Sismógrafo {tipo_dato.nombre} - {estacion.nombre}',
                    'estacionSismologica': estacion,
                    'tipoDeDato': tipo_dato
                }
                sismografo, created = Sismografo.objects.get_or_create(
                    nombre=sismografo_data['nombre'],
                    defaults=sismografo_data
                )
                if created:
                    self.stdout.write(f'  ✓ Sismógrafo creado: {sismografo.nombre}')

        # Crear Series Temporales
        for sismografo in Sismografo.objects.all()[:3]:  # Solo para los primeros 3 sismógrafos
            serie_data = {
                'fechaHoraInicio': timezone.now() - timedelta(hours=2),
                'fechaHoraFin': timezone.now() - timedelta(hours=1),
                'sismografo': sismografo
            }
            serie, created = SerieTemporal.objects.get_or_create(**serie_data)
            if created:
                self.stdout.write(f'  ✓ Serie temporal creada para: {sismografo.nombre}')

        # Crear Eventos Sísmicos
        eventos_data = [
            {
                'fechaHoraOcurrencia': timezone.now() - timedelta(hours=3),
                'fechaHoraFin': timezone.now() - timedelta(hours=2),
                'latitudEpicentro': -34.5,
                'longitudEpicentro': -58.4,
                'latitudHipocentro': -34.51,
                'longitudHipocentro': -58.41,
                'valorMagnitud': 4.2,
            },
            {
                'fechaHoraOcurrencia': timezone.now() - timedelta(days=1),
                'fechaHoraFin': timezone.now() - timedelta(days=1, hours=23),
                'latitudEpicentro': -32.9,
                'longitudEpicentro': -68.8,
                'latitudHipocentro': -32.91,
                'longitudHipocentro': -68.81,
                'valorMagnitud': 5.8,
            },
            {
                'fechaHoraOcurrencia': timezone.now() - timedelta(days=2),
                'fechaHoraFin': timezone.now() - timedelta(days=2, hours=23),
                'latitudEpicentro': -31.5,
                'longitudEpicentro': -68.5,
                'latitudHipocentro': -31.51,
                'longitudHipocentro': -68.51,
                'valorMagnitud': 3.9,
            }
        ]

        estado_autodetectado = Estado.objects.get(nombreEstado='AutoDetectado')
        alcance_local = AlcanceSismo.objects.get(nombre='Local')
        clasificacion_superficial = ClasificacionSismo.objects.get(nombre='Superficial')
        origen_tectonico = OrigenDeGeneracion.objects.get(nombre='Tectónico')
        empleado_supervisor = Empleado.objects.first()

        for i, evento_data in enumerate(eventos_data):
            evento_data.update({
                'estadoActual': estado_autodetectado,
                'alcanceSismo': alcance_local,
                'clasificacion': clasificacion_superficial,
                'origenGeneracion': origen_tectonico,
                'analistaSuperior': empleado_supervisor if i == 1 else None,  # Solo el segundo evento tiene analista
            })
            
            evento, created = EventoSismico.objects.get_or_create(
                fechaHoraOcurrencia=evento_data['fechaHoraOcurrencia'],
                defaults=evento_data
            )
            if created:
                self.stdout.write(f'  ✓ Evento sísmico creado: Magnitud {evento.valorMagnitud}')
                
                # Agregar series temporales al evento
                series = SerieTemporal.objects.all()[:2]  # Primeras 2 series
                evento.serieTemporal.set(series)
                
                # Crear cambio de estado inicial
                cambio_estado = CambioEstado.objects.create(
                    empleado=empleado_supervisor,
                    estado=estado_autodetectado,
                    fechaHoraInicio=evento.fechaHoraOcurrencia,
                    fechaHoraFin=None
                )
                evento.cambioEstado.add(cambio_estado)

        self.stdout.write(
            self.style.SUCCESS(
                f'\n¡Datos de prueba cargados exitosamente!'
                f'\n- {Estado.objects.count()} Estados'
                f'\n- {AlcanceSismo.objects.count()} Alcances de Sismo'
                f'\n- {ClasificacionSismo.objects.count()} Clasificaciones'
                f'\n- {OrigenDeGeneracion.objects.count()} Orígenes de Generación'
                f'\n- {Empleado.objects.count()} Empleados'
                f'\n- {EstacionSismologica.objects.count()} Estaciones Sismológicas'
                f'\n- {Sismografo.objects.count()} Sismógrafos'
                f'\n- {SerieTemporal.objects.count()} Series Temporales'
                f'\n- {EventoSismico.objects.count()} Eventos Sísmicos'
                f'\n- {CambioEstado.objects.count()} Cambios de Estado'
            )
        )
