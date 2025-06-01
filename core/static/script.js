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
        document.getElementById('modal-confirmar-mapa').style.display = 'none';
        if (data.mensaje) {
            document.getElementById('mensaje-mapa').innerHTML = data.mensaje;
        }
    });
}

document.getElementById('visualizar-mapa-btn').onclick = function(e) {
    e.preventDefault();
    document.getElementById('modal-confirmar-mapa').style.display = 'flex';
};
document.getElementById('btn-si-mapa').onclick = function() {
    enviarOpcionMapa('Si');
};
document.getElementById('btn-no-mapa').onclick = function() {
    enviarOpcionMapa('No');
};


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

document.getElementById('modificar-btn').onclick = function(e) {
    e.preventDefault();
    document.getElementById('modal-modificar-mapa').style.display = 'flex';
};
document.getElementById('btn-si-modificar').onclick = function() {
    enviarOpcionModificar('Si');
};
document.getElementById('btn-no-modificar').onclick = function() {
    enviarOpcionModificar('No');
};

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

document.getElementById('rechazar-btn').onclick = function(e) {
    e.preventDefault();
    document.getElementById('modal-rechazar-evento').style.display = 'flex';
};
document.getElementById('btn-si-rechazar').onclick = function() {
    enviarOpcionRechazarEvento('Si');
};
document.getElementById('btn-no-rechazar').onclick = function() {
    enviarOpcionRechazarEvento('No');
};

