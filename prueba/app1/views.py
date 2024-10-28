from django.shortcuts import render,redirect
from app1.models import Usuario
from app1.forms import FormUsuario

def index (request):
    return render (request,'app1/index.html')

def registrar(request):
    form=FormUsuario()
    if request.method=='POST':
        form=FormUsuario(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    data={'form':form}
    return render(request,'app1/registrar.html',data)

def lista(request):
    usuarios=Usuario.objects.all()
    data={'usuarios':usuarios}
    return render(request,'app1/listado.html',data)

def eliminar(request,id):
    proyect_instance=Usuario.objects.get(id=id)
    proyect_instance.delete()
    return redirect('/listado')

def actualizar(request,id):
    usuario=Usuario.objects.get(id=id)
    form=FormUsuario(instance=usuario)
    if request.method=='POST':
        form=FormUsuario(request.POST,instance=usuario)
        if form.is_valid():
            form.save()
        return redirect ('/')
    data={'form':form}
    return render (request,'app1/registrar.html',data)


    
