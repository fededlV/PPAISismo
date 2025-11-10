/* Helpers de UI inicial */
document.addEventListener('DOMContentLoaded', function () {
    // Ocultar el botón "Seleccionar Evento" si no hay eventos renderizados
    const seleccionarBtn = document.querySelector('form button[type="submit"]');
    const radiosEventos = document.querySelectorAll('tbody input[name="evento_id"]');
    if (seleccionarBtn && radiosEventos.length === 0) {
        seleccionarBtn.style.display = 'none';
    }
});

/*VISUALIZAR MAPA*/

function enviarOpcionMapa(opcion) {
    const visualizarBtn = document.getElementById('visualizar-mapa-btn');
    const url = visualizarBtn.getAttribute('data-url');
    const csrfToken = visualizarBtn.getAttribute('data-csrf');

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken
        },
        body: JSON.stringify({ opcion: opcion })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Respuesta del backend:', data); // Debug
        document.getElementById('modal-confirmar-mapa').style.display = 'none';
        if (data.mensaje) {
            document.getElementById('mensaje-mapa').innerHTML = data.mensaje;
        }
        
        // Si el usuario eligió "Sí", mostrar el mapa (sin depender de data.permitir)
        if (opcion === 'Si') {
            const contenedorMapa = document.getElementById('contenedor-mapa');
            const imagenMapa = document.getElementById('imagen-mapa');
            
            console.log('Mostrando mapa...'); // Debug
            
            // AQUÍ defines la ruta de tu imagen
            // Usando una de las imágenes existentes (puedes cambiarla)
            imagenMapa.src = '/static/images/13-sismicidad-7x.jpg';
            
            // O si prefieres la otra:
            // imagenMapa.src = '/static/images/48448452516_b1dcf113b5_c.webp';
            
            // Si el backend devuelve la URL de la imagen dinámicamente:
            // imagenMapa.src = data.urlMapa;
            
            contenedorMapa.style.display = 'block';
            
            // Scroll suave hacia el mapa
            setTimeout(() => {
                contenedorMapa.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            }, 100);
        }
    })
    .catch(error => {
        console.error('Error al visualizar mapa:', error);
    });
}

const btnVisualizarMapa = document.getElementById('visualizar-mapa-btn');
if (btnVisualizarMapa) {
    btnVisualizarMapa.onclick = function(e) {
        e.preventDefault();
        document.getElementById('modal-confirmar-mapa').style.display = 'flex';
    };
}
const btnSiMapa = document.getElementById('btn-si-mapa');
if (btnSiMapa) {
    btnSiMapa.onclick = function() { enviarOpcionMapa('Si'); };
}
const btnNoMapa = document.getElementById('btn-no-mapa');
if (btnNoMapa) {
    btnNoMapa.onclick = function() { enviarOpcionMapa('No'); };
}


// MODIFICAR DATOS
function enviarOpcionModificar(opcion) {
    const modificarBtn = document.getElementById('modificar-btn');
    const url = modificarBtn.getAttribute('data-url');
    const csrfToken = modificarBtn.getAttribute('data-csrf');

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken
        },
        body: JSON.stringify({ opcion: opcion })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('modal-modificar-mapa').style.display = 'none';
        if (data.mensaje) {
            document.getElementById('mensaje-modificar-datos').innerHTML = data.mensaje;
        }
    });
}

const btnModificar = document.getElementById('modificar-btn');
if (btnModificar) {
    btnModificar.onclick = function(e) {
        e.preventDefault();
        document.getElementById('modal-modificar-mapa').style.display = 'flex';
    };
}
const btnSiModificar = document.getElementById('btn-si-modificar');
if (btnSiModificar) {
    btnSiModificar.onclick = function() { enviarOpcionModificar('Si'); };
}
const btnNoModificar = document.getElementById('btn-no-modificar');
if (btnNoModificar) {
    btnNoModificar.onclick = function() { enviarOpcionModificar('No'); };
}

// RECHAZAR EVENTO
function enviarOpcionRechazarEvento(opcion) {
    const rechazarBtn = document.getElementById('rechazar-btn');
    const url = rechazarBtn.getAttribute('data-url');
    const csrfToken = rechazarBtn.getAttribute('data-csrf');

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken
        },
        body: JSON.stringify({ opcion: opcion })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('modal-rechazar-evento').style.display = 'none';
        if (data.mensaje) {
            document.getElementById('mensaje-rechazar-evento').innerHTML = data.mensaje;
        }
    });
}

const btnRechazar = document.getElementById('rechazar-btn');
if (btnRechazar) {
    btnRechazar.onclick = function(e) {
        e.preventDefault();
        document.getElementById('modal-rechazar-evento').style.display = 'flex';
    };
}
const btnSiRechazar = document.getElementById('btn-si-rechazar');
if (btnSiRechazar) {
    btnSiRechazar.onclick = function() {
        enviarOpcionRechazarEvento('Si');
        setTimeout(function() {
            window.location.href = '/opcRegistrarResRevisionMan';
        }, 500);
    };
}
const btnNoRechazar = document.getElementById('btn-no-rechazar');
if (btnNoRechazar) {
    btnNoRechazar.onclick = function() { enviarOpcionRechazarEvento('No'); };
}

