from django.shortcuts import render
from .models import Slider,Galeria,Insumo,MisionyVision
#Importar la tabla de usuarios
from django.contrib.auth.models import User
#importar las librerias de authentication
from django.contrib.auth import authenticate,logout,login as login_autent
#agregar un decorador que evite el ingreso a las paginas si no estas registrado
from django.contrib.auth.decorators import login_required,permission_required



# Create your views here.
def logout_vista(request):
    logout(request)
    Slider1=Slider.objects.filter(ident='slider1')
    Slider2=Slider.objects.filter(ident='slider2')
    Slider3=Slider.objects.filter(ident='slider3')
    return render(request,'web/index.html',{'lista_Slider1':Slider1,'lista_Slider2':Slider2,'lista_Slider3':Slider3})


def login(request):
    if request.POST:
        Slider1=Slider.objects.filter(ident='slider1')
        Slider2=Slider.objects.filter(ident='slider2')
        Slider3=Slider.objects.filter(ident='slider3')
        usuario=request.POST.get("txtNombreUsuario")
        password=request.POST.get("txtContraseña")
        us=authenticate(request,username=usuario,password=password)
        if us is not None and us.is_active:
            login_autent(request,us)
            return render(request,'web/index.html',{'user':us,'lista_Slider1':Slider1,'lista_Slider2':Slider2,'lista_Slider3':Slider3})
        else:
            return render(request,'web/Login.html',{'msg':'usuario no existe'})
    return render(request,'web/Login.html')

def index(request):
    Slider1=Slider.objects.filter(ident='slider1')
    Slider2=Slider.objects.filter(ident='slider2')
    Slider3=Slider.objects.filter(ident='slider3')
    return render(request,'web/index.html',{'lista_Slider1':Slider1,'lista_Slider2':Slider2,'lista_Slider3':Slider3})
@login_required(login_url='/login/')
@permission_required('misCarWash.view_insumo',login_url='/login/')
@permission_required('misCarWash.change_insumo',login_url='/login/')
def modificar(request):
    if request.POST:
        nombre = request.POST.get("txtNombreInsumo")
        precio = request.POST.get("txtPrecioInsumo")
        descr  = request.POST.get("txtDescripcion")
        stock  = request.POST.get("txtStock")

        try:
            insumo = Insumo.objects.get(nombre=nombre)
            insumo.precio = precio
            insumo.descripcion = descr
            insumo.stock = stock
            insumo.save()
            mensaje = 'Modificó'
        except:
            mensaje = 'No Modificó'
    lista = Insumo.objects.all()
    return render(request,'web/admin_insumos.html',{'lista_insumo':lista,'mensaje':mensaje})

@login_required(login_url='/login/')
def buscar(request,id):
    try:
        insumo=Insumo.objects.get(nombre=id)
        return render(request,'web/formulario_insumo_mod.html',{'insumo':insumo})
    except:
        msg='No existe insumo'
    lista=Insumo.objects.all()
    return render(request,'web/admin_insumos.html',{'lista_insumos':lista,'msg':msg})



def pagina2(request):
    lista=MisionyVision.objects.all()
    return render(request,'web/Página2.html',{'lista':lista})

def pagina3(request):
    return render(request,'web/Página3.html')

def pagina4(request):
    if request.POST:
        nombre=request.POST.get("txtNombre")
        apellido=request.POST.get("txtApellido")
        email=request.POST.get("txtEmail")
        nombreusuario=request.POST.get("txtNombreUsuario")
        contraseña1=request.POST.get("txtContraseña1")
        contraseña2=request.POST.get("txtContraseña2")
        try:
            u=User.objects.get(username=nombreusuario)
            mensaje="Usuario existe"
            return render(request,'web/Página4.html',{'msg':mensaje})
        except:
            if contraseña1!=contraseña2:
                mensaje="Contraseñas incorrectas"
                return render(request,'web/Página4.html',{'msg':mensaje})
            u = User()
            u.first_name=nombre
            u.last_name=apellido
            try:
                u=User.objects.get(email=email)
                mensaje="Email ya registrado"
                return render(request,'web/Página4.html',{'msg':mensaje})
            except:
                u.email=email
                u.username=nombreusuario
                u.set_password(contraseña1)
                u.save()
                us=authenticate(request,username=nombreusuario,password=contraseña1)
                login_autent(request,us)
                Slider1=Slider.objects.filter(ident='slider1')
                Slider2=Slider.objects.filter(ident='slider2')
                Slider3=Slider.objects.filter(ident='slider3')
                return render(request,'web/index.html',{'user':us,'lista_Slider1':Slider1,'lista_Slider2':Slider2,'lista_Slider3':Slider3})
    return render(request,'web/Página4.html')

@login_required(login_url='/login/')
@permission_required('misCarWash.view_insumo',login_url='/login/')
@permission_required('misCarWash.delete_insumo',login_url='/login/')
def eliminar_insumo(request,id):
    try:
        insumo = Insumo.objects.get(nombre=id)
        insumo.delete()
        msg='Elimino insumo'
    except:
        msg='No elimino'
    lista=Insumo.objects.all()
    return render(request,'web/admin_insumos.html',{'lista_insumo':lista,'msg':msg})


@login_required(login_url='/login/')
@permission_required('misCarWash.view_insumo',login_url='/login/')
def lista_insumos(request):
    lista=Insumo.objects.all()
    return render(request,'web/admin_insumos.html',{'lista_insumo':lista})

@login_required(login_url='/login/')
@permission_required('misCarWash.add_insumo',login_url='/login/')
def pagina5(request):
    insumos=Insumo.objects.all()
    if request.POST:
        nombre=request.POST.get("txtNombreInsumo")
        precio=request.POST.get("txtPrecioInsumo")
        descripcion=request.POST.get("txtDescripcion")
        stock=request.POST.get("txtStock")
        ins = Insumo(
            nombre=nombre,
            precio=precio,
            descripcion=descripcion,
            stock=stock
        )
        ins.save()
        mensaje='Grabo insumo'
        return render(request,'web/Página5.html',{'lista_i':insumos,'mensaje':mensaje})
    return render(request,'web/Página5.html')

def pagina6(request):
    Gal=Galeria.objects.all()
    return render(request,'web/Página6.html',{'lista_Galeria':Gal})
