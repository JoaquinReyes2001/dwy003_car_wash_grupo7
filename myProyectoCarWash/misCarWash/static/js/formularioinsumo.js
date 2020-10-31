
function validarNombreInsumo(){
    var nominsumo = document.getElementById("txtNombreInsumo").value;
    if (nominsumo.length.trim() >= 3 && nominsumo.length.trim()<= 120) {
        return true;
    } else {
        alert("Largo del nombre del insumo debe estar entre 3 y 120");
        return false;
    }
}
function validarPrecioInsumo(){
    var precioinsumo = document.getElementById("txtPrecioInsumo").value;
    if (precioinsumo>=1) {
        return true;
    } else {
        alert("El precio mínimo del insumo es de 1 peso");
        return false;
    }
}

function validarDescripcion(){
    var des = document.getElementById("txtDescripcion").value;
    if(des.length.trim()>0){
    if (des.length.trim() >= 3 && des.length.trim() <=200) {
        return true;
    } else {
        alert("Largo de la descripción debe estar entre 3 y 200");
        return false;
    }
    }
    else{
        return true;
    }
}

function validarStock(){
    var stock = document.getElementById("txtStock").value;
    if (stock>=0) {
        return true;
    } else {
        alert("El stock mínimo del insumo es de 0");
        return false;
    }
}





function validarFormularioInsumo() {
    var resp;
    resp = validarNombreInsumo();
    if (resp == false) {
        return false;
    }
    resp = validarPrecioInsumo();
    if (resp == false) {
        return false;
    }
    resp = validarDescripcion();
    if (resp == false) {
        return false;
    }
    resp=validarStock();
    if (resp == false) {
        return false;
    }
}


