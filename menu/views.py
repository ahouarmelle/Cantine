from django.shortcuts import render, redirect
from menu.forms.menu_form import MenuForm
from menu.models.menu_model import MenuModel


def index(request):
    rech_menu = request.GET.get('rech')
    if rech_menu:
        menus = MenuModel.objects.filter(plat__icontains=rech_menu)
        context= { 'menus': menus,
                  'rech_menu': rech_menu
                  }
    else:
        menus = MenuModel.objects.all()
        menu_count = MenuModel.objects.count()
        context = {
            'menus':menus,
            'menu_count': menu_count
        }
    return render(request, "menu/index.html", context)


def add(request):
    context={"title":"Ajouter un menu"}

    if request.method == "POST":
        print(request.POST)
        form =MenuForm(request.POST)
        context["form"] = form
        if form.is_valid():
            print("form is valid")
            print(form.cleaned_data)
            form.save()
            return redirect('menu:index')
        else:
            return render(request,"menu/add.html")

    
    form = MenuForm()
    context["form"] = form

    return render(request,"menu/add.html",context)


def update(request, id ):
    menu = MenuModel.objects.get(id=id)

    context = {"title":"Modifier un menu"}


    if request.method == "POST":
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('menu:index')
        
    form = MenuForm(instance = menu)

    context["form"] = form

    return render(request,"menu/add.html",context)

def delete(request ,id):
    student = MenuModel.objects.get(id = id)
    student.delete()
    return redirect('menu:index')
