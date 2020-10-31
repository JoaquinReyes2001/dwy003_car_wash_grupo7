function validarNombre() {
    var nom = document.getElementById("txtNombre").value;
    if (nom.length.trim() >= 3 && nom.length.trim() <= 80) {
        return true;
    } else {
        alert("Largo del nombre debe estar entre 3 y 80");
        return false;
    }
}
function validarApellido() {
    var ape = document.getElementById("txtApellido").value;
    if (ape.length.trim() >= 3 && ape.length.trim() <= 80) {
        return true;
    } else {
        alert("Largo del apellido debe estar entre 8 y 80");
        return false;
    }
}
function validarFormularioUsuario() {
    var resp;
    resp = validarNombre();
    if (resp == false) {
        return false;
    }
    resp = validarApellido();
    if (resp == false) {
        return false;
    }
   
}

