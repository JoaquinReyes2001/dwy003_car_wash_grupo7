from django.contrib import admin
from django.urls import path,include
from .views import index,pagina2,pagina3,pagina4,pagina5,pagina6,login,logout_vista,lista_insumos,eliminar_insumo,buscar,modificar
urlpatterns = [
    path('',index,name='IND'),
    path('pagina2/',pagina2,name='PAG2'),
    path('pagina3/',pagina3,name='PAG3'),
    path('pagina4/',pagina4,name='PAG4'),
    path('pagina5/',pagina5,name='PAG5'),
    path('pagina6/',pagina6,name='PAG6'),
    path('login/',login,name='LOGIN'),
    path('logout_vista/',logout_vista,name='LOGOUT'),
    path('lista_insumos/',lista_insumos,name='LISTAI'),
    path('eliminar_in/<id>/',eliminar_insumo,name='ELIMINARINSUMO'),
    path('buscar/<id>/',buscar,name='BUSCAR'),
    path('modificar/',modificar,name='MODIFICAR'),
]
