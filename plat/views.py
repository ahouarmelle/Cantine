from django.shortcuts import render, redirect
from plat.forms.plat_form import PlatForm
from plat.models.plat_model import PlatModel


def index(request):
    rech_plat = request.GET.get('rech')
    if rech_plat:
        plats = PlatModel.objects.filter(name__icontains=rech_plat)
        context= { 'plats': plats,
                  'rech_user': rech_plat
                  }
    else:
        plats = PlatModel.objects.all()
        plat_count = PlatModel.objects.count()
        context = {
            'plats':plats,
            'plat_count': plat_count
        }
    return render(request, "plat/index.html", context)


def add(request):
    context={"title":"Ajouter un plat"}

    if request.method == "POST":
        print(request.POST)
        form =PlatForm(request.POST)
        context["form"] = form
        if form.is_valid():
            print("form is valid")
            print(form.cleaned_data)
            form.save()
            return redirect('plat:index')
        else:
            return render(request,"plat/add.html")

    # context={'elev_form':elev_form}
    form = PlatForm()
    context["form"] = form

    return render(request,"plat/add.html",context)


def update(request, id ):
    plat = PlatModel.objects.get(id=id)

    context = {"title":"Modifier un plat"}


    if request.method == "POST":
        form = PlatForm(request.POST, instance=plat)
        if form.is_valid():
            form.save()
            return redirect('plat:index')
        
    form = PlatForm(instance = plat)

    context["form"] = form

    return render(request,"plat/add.html",context)

def delete(request ,id):
    student = PlatModel.objects.get(id = id)
    student.delete()
    return redirect('plat:index')