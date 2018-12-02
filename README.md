#setup anaconda or miniconda pythone.<br/>
  this will help us to create a virtual environment that contains the newer version of the package<br/>

  #to use a virtual environment with Conda we use this command to crate environment<br/><br/>
  #it encouraged to use virtual environments for project to keep them self-contained and not run into issues when packages update.<br/>
    $conda crate --name myEnv<br/>
<br/><br/><br/>
  #to use created environment we need to activate the environment<br/>
    $activate myEnv<br/><br/>
  #to deactivate environment<br/><br/>
    $deactivate myEnv<br/>
<br/><br/>
#to install django<br/>
  $conda install django<br/>
  #OR<br/>
  $pip install django<br/>
#anything installed with pip or conda when environment is activated, will only be installed for this environment<br/>
<br/>
#crate your first project in current work directory<br/>
  $django-admin startproject first_project<br/>
<br/>
#packages will contain files<br/>
  #__init__.py : Blank python script. due to this special name let's python know that this directory can be treated as a package<br/>
  #setting.py :  Stores project settings<br/>
  #urls.py : store all the url patterns for project. Basically the different pages of web Application<br/>
  #wsgi.py : this acts as the web server gateway interface. it will help to deploy our web app to production<br/>
  #manage.py : will be associated with many commands as we build our web app<br/>

#to run server we use manage.py as which will provide us development server location something like "http://127.0.0.1:8080/"<br/>
  $python manage.py runserver<br/>
<br/>
#migration WARNING<br/>
  #this has to do with databases and how to connect them to django. Since migration allows us to move databases from one design to another
  and viseversa.<br/>

#Django project is a collection of applications and Configuration that when combined together will make up the full web application.<br/>
#Django applicaiton is created to perform a particular functionality for entire web application. These apps can be
plugged into other django projects, so we can reuse them.<br/>
<br/>
#Crate Hello world applicaition<br/>
  $python manage.py startapp first_app<br/>
<br/>
  #this creates application with files like :<br/>
    #__init__.py<br/>
    #admin.py : we can register our models here which django will then use them with Djangos admin interface.<br/>
    #apps.py : we can place application specific Configuration<br/>
    #models.py : store the apoplications data models.<br/>
    #tests.py : store test functions to test code.<br/>
    #views.py : handles request and return response<br/>
    #migration folder : directory stores database specific information as it relates to the models.<br/>
<br/>
#after created applicaiton we need to register our own applicaiton. we do this by placing name of our application<br/>
#under "INSTALLED_APPS" object (i.e list)<br/>
<br/>
#next is to modify "views.py" file under our applications<br/>
  #firstly import "HttpResponse" objec from "jango.http" model as<br/>
    "from django.http import HttpResponse"<br/>
  #create function that takes parameter and return "HttpResponse" with some string<br/>
    def index(request):<br/>
      return HttpResponse("Hello World!")<br/>

#at last we need add function calls in "urls.py" file that will map urls into functions<br/>
  path('',view.index) #here path is imported from "django.urls"<br/>


#finally run server again.<br/>


<H2>Models</H2>
    <p> we use models to incorporate a database into a Django project. By Default Django comes with SQLite.
    Engine parameter can be edited in settings.py file for Database. To create an actual model, we use a class structure inside of the relevant applications models.py file.
    <i> class Topic(models.Model):<br/>
    </t>topic_name = models.CharField(max_length=25, unique=True)</i><br/><br/>
     We use subclass of Django class <br/>
    <i>django.db.models.Models
    </i><br/>
    Each attribute of the class represents a field which is just like a column name with constraints in SQL.

    After models creation we need to migrate the database. This is basically letting django do the heavy lifting of creating sql database that correspond to models we created. this can be done with simple command.<br/>
      <i>python manage.py migrate</i><br/>
      <br/>
      registering the changes to apps example:"first_app"<br/>
      <i>python manage.py makemigrations first_app</i><br/><br/>
      again once more migrate<br/>
      <i> pythone manage.py migrate</i><br/><br/>

      we can use models with admin interface.it helps to interact with the database. But, this requires registration of models in our admin.py file.
      <i>from django.contrib import admin<br/>
      from app.models import Model1, Model2<br/><br/>
      admin.site.register(Model1)<br/>
      admin.site.register(Model2)</i><br/><br/>

      in order to fully use the database and Admin interface we need to create a superuser. this can be done as :<br/>
      <i>python manage.py createsuperuser</i><br/>

      to populate test data we can i have used <b><a href="https://faker.readthedocs.io/en/master/">Faker</a></b> and created a script.
      we can install Faker by <br/>
      <i>$pip install Faker</i>
      it may not work in some cases as i suffered, Instead we can use <br/>
      <i>python -m pip install Faker</i>

      <h2>Model-Templates-Views</h2>
      Django operates MTV which helps to achieving the goal of serving dynamic content oto a user based off the connection of the models, view, and templates.<br/>
      First: In the views.py file we have to import models that we will need to use <br/>
      Second: Use the view to query the model for data that will need<br/>
      Third: pass result from the model to the template
    </p>
