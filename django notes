#setup anaconda or miniconda pythone.
  this will help us to create a virtual environment that contains the newer version of the package.

  #to use a virtual environment with Conda we use this command to crate environment
  #it encouraged to use virtual environments for project to keep them self-contained and not run into issues when packages update.
    $conda crate --name myEnv

  #to use created environment we need to activate the environment
    $activate myEnv
  #to deactivate environment
    $deactivate myEnv

#to install django
  $conda install django
  #OR
  $pip install django
#anything installed with pip or conda when environment is activated, will only be installed for this environment

#crate your first project in current work directory
  $django-admin startproject first_project

#packages will contain files
  #__init__.py : Blank python script. due to this special name let's python know that this directory can be treated as a package
  #setting.py :  Stores project settings
  #urls.py : store all the url patterns for project. Basically the different pages of web Application
  #wsgi.py : this acts as the web server gateway interface. it will help to deploy our web app to production
  #manage.py : will be associated with many commands as we build our web app

#to run server we use manage.py as which will provide us development server location something like "http://127.0.0.1:8080/"
  $python manage.py runserver

#migration WARNING
  #this has to do with databases and how to connect them to django. Since migration allows us to move databases from one design to another
  and viseversa.

#Django project is a collection of applications and Configuration that when combined together will make up the full web application.
#Django applicaiton is created to perform a particular functionality for entire web application. These apps can be
plugged into other django projects, so we can reuse them.

#Crate Hello world applicaition
  $python manage.py startapp first_app

  #this creates application with files like :
    #__init__.py
    #admin.py : we can register our models here which django will then use them with Djangos admin interface.
    #apps.py : we can place application specific Configuration
    #models.py : store the apoplications data models.
    #tests.py : store test functions to test code.
    #views.py : handles request and return response
    #migration folder : directory stores database specific information as it relates to the models.

#after created applicaiton we need to register our own applicaiton. we do this by placing name of our application
#under "INSTALLED_APPS" object (i.e list)

#next is to modify "views.py" file under our applications
  #firstly import "HttpResponse" objec from "jango.http" model as
    "from django.http import HttpResponse"
  #create function that takes parameter and return "HttpResponse" with some string
    def index(request):
      return HttpResponse("Hello World!")

#at last we need add function calls in "urls.py" file that will map urls into functions
  path('',view.index) #here path is imported from "django.urls"


#finally run server again.
