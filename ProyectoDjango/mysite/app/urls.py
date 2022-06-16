from django.urls import path
from .views import home, nuestrosMininos, quienesSomos, formulario,\
     productos, agregar_producto, listar_productos, modificar_producto,\
         eliminar_producto, registro

urlpatterns = [
    path('', home, name="home"),
    path('quienesSomos/', quienesSomos, name="quienesSomos"),
    path('nuestrosMininos/', nuestrosMininos, name="nuestrosMininos"),
    path('formulario/', formulario, name="formulario"),
    path('productos/', productos, name="productos"),
    path('agregar-productos/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro/', registro, name="registro"),
]
