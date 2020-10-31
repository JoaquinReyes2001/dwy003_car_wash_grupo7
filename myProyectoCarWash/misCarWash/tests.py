from django.test import TestCase
import unittest
from .models import Insumo,MisionyVision
from django.contrib.auth.models import User
# Create your tests here.
class TestInsumos(unittest.TestCase):
    def test_grabar_insumo(self):
        valor = 0
        try:
            insumo = Insumo(
                nombre="Cera para vehículo",
                descripcion="Nueva cera ultra brillante",
                precio=1000,
                stock=10
            )
            insumo.save()
            valor = 1
        except:
            valor = 0
        self.assertEqual(valor,1)

    def test_eliminar_insumo(self):
        valor=0
        id="Shampoo"
        try:
            insumo=Insumo.objects.get(nombre=id)
            insumo.delete()
            valor=1
        except:
            valor=0
        self.assertEqual(valor,1)

    def test_modificar_insumo(self):
        valor=0
        nombre="Silicona"
        try:
            insumo = Insumo.objects.get(nombre=nombre)
            insumo.precio = 500
            insumo.descripcion = "Silicona en spray que entrega mayor brillo al automóvil"
            insumo.stock = 10
            insumo.save()
            valor=1
        except:
            valor=0
        self.assertEqual(valor,1)


class TestMisionVision(unittest.TestCase):
    def test_grabar_mision_vision(self):
        valor = 0
        try:
            misionyvision = MisionyVision(
                ident=2,
                mision="Agregado de nueva misión",
                vision="Agregado de nueva visión"
            )
            misionyvision.save()
            valor = 1
        except:
            valor = 0
        self.assertEqual(valor,1)


class TestUsuario(unittest.TestCase):
    def test_grabar_usuario(self):
        valor = 0
        try:
            u = User()
            u.first_name="Joaquín"
            u.last_name="Reyes"
            u.email="joacoantonio@hotmail.com"
            u.username="joaquinreyes2001"
            u.set_password("micontraseñacar123")
            u.save()
            valor = 1
        except:
            valor = 0
        self.assertEqual(valor,1)


if __name__ == "__main__":
    unittest.main()


