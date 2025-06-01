# 13 Tomar eventos seleccionado
def tomarEvento(request):
    if request.method == 'POST':
        evento_id = request.POST.get('evento_id')
        gestor = GestorRevision()
        gestor.tomarEvento(evento_id)
        eventosSismicosAd = gestor.tomarOpcSeleccionada()
        alcance = mostrarAlcance(evento_id)  # Usamos el método separado
        clasificacion=mostrarClasificacion(evento_id)
        origen=mostrarDatosOrigen(evento_id)
        print(gestor.clasificarPorEstacion())
        
        return render(request, 'pantallaRevision.html', {
            'eventos': eventosSismicosAd,
            'alcance': alcance,
            'clasificacion': clasificacion,
            'origen': origen
        })
    else:
        # Si se accede por GET, redirigir a la pantalla de selección
        return redirect('tomarOpcSeleccionada')