from django.shortcuts import render, redirect
from .models import Actividad,Carpeta
from .forms import ActividadForm, CarpetaForm
from django.contrib import messages

def index_2(request):
    carpetas = Carpeta.objects.order_by("carpeta")
    context = {'carpetas': carpetas}
    if request.method== "POST":
        form = CarpetaForm(request.POST)
        if form.is_valid():
            nue_carp=form.save(commit=False)
            nue_carp.save()
            id_act=nue_carp.id
            messages.success(request, "La carpeta fue creada con exito")
            return redirect('items:carpeta', car_id=id_act)
    return render(request, 'items/index_2.html', context)


    return render(request, 'items/index_2.html', context)

def carpeta(request, car_id):
    carpeta_actual=Carpeta.objects.get(id=car_id)
    actividades=Actividad.objects.filter(carpeta=carpeta_actual).order_by("hecho", "id")
    context= {"carpeta_actual":carpeta_actual,"actividades":actividades}
    if request.method == "POST":
        post = request.POST.copy()
        post['carpeta'] = carpeta_actual
        form = ActividadForm(data=post)
        if form.is_valid():
            print("entro en el is_valid")
            form.save()
            messages.success(request, 'La Actividad fue añadida con exito')
            return render (request, 'items/carpeta.html', context)
    return render(request, 'items/carpeta.html', context)

def eliminar_carpeta(request, car_id):
    carp= Carpeta.objects.get(id=car_id)
    carp.delete()
    messages.warning(request, "La carpeta fue eliminada")
    return redirect('items:index_2')

def editar_carpeta(request, car_id):
    car=Carpeta.objects.get(id=car_id)
    if request.method != "POST":
        form=CarpetaForm(instance=car)
    else:
        form= CarpetaForm(instance=car, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('items:index_2')
    context={'form':form,'carpeta':car.id}
    return render(request, 'items/editar_carpeta.html', context)



def index(request):
    todo= Actividad.objects.order_by("hecho", "id")
    context= {'todo': todo}
    if request.method == "POST":
        form = ActividadForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'La Actividad fue añadida con exito')
            return render (request, 'items/index.html', context)
    return render (request, 'items/index.html', context)

  #  return render(request, 'items/index.html')
def eliminar (request, actividad_id):
    actividad= Actividad.objects.get(id=actividad_id)
    car_act=actividad.carpeta.id
    actividad.delete()
    messages.warning(request, "La actividad fue eliminada")
    return redirect('items:carpeta', car_id=car_act)

def marcarHecho(request, act_id):
    act=Actividad.objects.get(id=act_id)
    act.hecho=True
    act.save()
    return redirect("items:carpeta", car_id=act.carpeta.id)

def desmarcarHecho (request, act_id):
    act=Actividad.objects.get(id=act_id)
    act.hecho=False
    act.save()
    return redirect("items:carpeta", car_id=act.carpeta.id)

def editar (request, act_id):
    act=Actividad.objects.get(id=act_id)
    if request.method != "POST":
        form=ActividadForm(instance=act)
    else:
        form= ActividadForm(instance=act, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("items:carpeta", car_id=act.carpeta.id)
    context={'form':form,'actividad':act_id}
    return render(request, 'items/editar.html', context)

        


def crear_carpeta(request):
    if request.method == "POST":
        form = CarpetaForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.success("La carpeta fue creada con exito")
    return render( request, "items/index_2")