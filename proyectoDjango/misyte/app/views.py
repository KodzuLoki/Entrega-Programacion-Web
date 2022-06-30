import imp
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Marca
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializer, MarcaSerializer

#Vistas

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self):
        productos = Producto.objects.all()

        nombre = self.request.GET.get('nombre')

        if nombre:
            productos = productos.filter(nombre=nombre)

        return productos



def home(request):
    return render(request, 'app/home.html')

def quienesSomos(request):
    return render(request, 'app/quienesSomos.html')

def nuestrosMininos(request):
    return render(request, 'app/nuestrosMininos.html')

def formulario(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "mensaje guardado"
        else:
            data["form"] = formulario


    return render(request, 'app/formulario.html', data)

def productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/productos.html', data)

@permission_required('app.add_producto')
def agregar_producto(request):
    data={
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto registrado")
        else:
            data["form"] = formulario

    return render(request, 'app/producto/agregar.html', data)

@permission_required('app.view_producto')
def listar_productos(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 2)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': productos,
        'paginator': paginator
    }
    return render(request, 'app/producto/listar.html',data)

@permission_required('app.change_producto')
def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)

    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar_productos")
        data["form"] = formulario


    return render(request, 'app/producto/modificar.html', data)

@permission_required('app.delete_producto')
def eliminar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_productos")

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(usarname=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            messages.success(request, "Registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)