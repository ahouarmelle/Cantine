# Les étapes d'installation de l'application
Avant de commencer nous devons nous assurer que python est bien installé sur notre machin.
Aprés cela nous devons creer un dossier dans lequel nous allons creer notre environnement et notre projet django. Pour pourvoir creer notre environnement nous devons être à la racine de notre dossier et saisir la commande 'python -m venv nomdelenvironnement(soit env ou venv)', par la suite nous devons activer notre environnement avec '.\env\Scripts\activate'.
Nous pouvons creer notre projet django:
-On installe django 'pip install django'
-on cree le projet django 'django-admin startproject nomvotreprojet'
-on se mets a la racine de notre projet django et on cree nos applications 'python manage.py startapp nomapplication'
Apres avoir creer nos application on les definir dans le settings.py de notre projet au niveau de :
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # definir nos applications 
    'nomapplication.apps.NomapplicationConfig',
    'menu.apps.MenuConfig',
    'base.apps.BaseConfig',
    'plat.apps.PlatConfig',
    
]
Dans notre application nos allons creer un dossier 'templates ' pour nos fichier html, un dossier static pour nos fichier statique(dossier:css,js,images,...). Nous allons les definir dans notre settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], --ici--
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


#https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
--On copie ce bloc--
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

Apres cela on creer un fichier de base.html dans notre template

On va definir nos routes dans le fichier views.py de notre application et les appeles dans le fichier urls.py que nous allons creer.

Nous allons inclure nos urls dans le fichier urls.py de notre projet
exemple:
dans le fichier views d'une application
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








Connection Bd
install mysql 'pip install pymysql' et dans le init du project 
import pymysql # type: ignore
pymysql.install_as_MySQLdb()


dans le setting on fais la configuration de la bd
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cantine_db',
        'USER':'root',
        'PASSWORD':'root',
        'HOST':'localhost',
        'PORT':'3306',
    }
}



# resume du projet




