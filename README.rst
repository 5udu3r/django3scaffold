
Django 3 Scaffold Package
-------------------------


   <p align="center"><img src="https://raw.githubusercontent.com/tokyodevs/django3scaffold/master/django3scaffold.png" width="2000"></p>



   <p align="center">
   <a href=""><img src="https://img.shields.io/github/issues/tokyodevs/django3scaffold" alt="Build Status"></a>
   <a href=""><img src="https://img.shields.io/github/forks/tokyodevs/django3scaffold" alt="Build Status"></a>
   <a href=""><img src="https://img.shields.io/github/stars/tokyodevs/django3scaffold" alt="Build Status"></a>
   <a href=""><img src="https://img.shields.io/github/license/tokyodevs/django3scaffold" alt="Build Status"></a>
   <a href="https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Ftokyodevs%2Fdjango3scaffold"><img src="https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Ftokyodevs%2Fdjango3scaffold" alt="Build Status"></a>
   </p>


Overview
--------

imagine that you need to build a customized admin panel from scratch or maybe you need a second panel just for your customers, regular users or something like that  , then you need this package to do it very fast. 

this package creates models and views and forms and URLs and tests and templates for crud in one single command!   

for example, you just run a single command in your command-line like this : 

    python manage.py scaffold forum --model Forum char:name char:reads


and this package generates these files for you : 

    └── forum
       ├── __init__.py
       ├── admin.py
       ├── apps.py
       ├── forms.py
       ├── migrations
       │   └── __init__.py
       ├── models.py
       ├── templates
       │   ├── base.html
       │   └── forum
       │       ├── details.html
       │       └── list.html
       ├── tests.py
       ├── urls.py
       └── views.py




Installation
------------


* 
  Install django3scaffold (ideally in your virtualenv!) using pip or simply getting a copy of the code and putting it in a directory in your codebase.


       pip install django3scaffold

* 
  Add ``django3scaffold`` to your Django settings ``INSTALLED_APPS``\ :


   INSTALLED_APPS = [
           # ...
           "django3scaffold",
       ]


* 
  Add the following to your settings.py with appropriate values:


  * IS_DEV
  * IS_PROD
  * DOMAIN_NAME
  * WWW_ROOT


        DOMAIN_NAME= 'localhost'
        WWW_ROOT = BASE_DIR
        IS_DEV = True
        IS_PROD = False


* 
  Add ``django3scaffold`` to your Django settings ``TEMPLATE_CONTEXT_PROCESSORS``\ :


      'OPTIONS': {
           'context_processors': [
               ...
               'django3scaffold.context_processors.django3scaffold_settings',
               ...

           ],

usage
-----


#. Run

To run scaffold type:


        python manage.py scaffold APPNAME --model MODELNAME [fields]


APPNAME is app name. If app does not exists it will be created.
MODELNAME is model name. Just enter model name that you want to create (for example: Blog, Topic, Post etc). It must be alphanumerical. Only one model per run is allowed!

[fields] - list of the model fields.


#. Field types

Available fields:


        char - CharField
        text - TextField
        int - IntegerFIeld
        decimal -DecimalField
        datetime - DateTimeField
        foreign - ForeignKey


All fields requires name that is provided after ``:`` sign, for example:


   char:title  text:body int:posts datetime:create_date


Two fields ``foreign`` and ``decimal`` requires additional parameters:


* 
  "foreign" as third argument takes foreignkey model, example:

    foreign:blog:Blog, foreign:post:Post, foreign:added_by:User

NOTICE: All foreign key models must alread exist in project. User and Group model are imported automatically.


* 
  decimal field requires two more arguments ``max_digits`` and ``decimal_places``\ , example:

    decimal:total_cost:10:2

NOTICE: To all models scaffold automatically adds two fields: update_date and create_date.


#. How it works?

Scaffold creates models, views (CRUD), forms, templates, admin, urls and basic tests (CRUD). Scaffold templates are using two blocks extending from base.html:


        {% extends "base.html" %}
        {% block page-title %} {% endblock %}
        {% block conent %} {% endblock %}


So be sure you have your base.html set up properly.

Scaffolding example usage
-------------------------

Let's create very simple ``forum`` app. We need ``Forum`` , ``Topic`` and ``Post`` model.


* Forum model

Forum model needs just one field ``name`` :


        python manage.py scaffold forum --model Forum char:name



* Topic model

Topics are created by site users so we need: ``created_by`` , ``title`` and ``Forum`` foreign key ( ``update_date`` and ``create_date`` are always added to models):


        python manage.py scaffold forum --model Topic foreign:created_by:User char:title foreign:forum:Forum



* Post model

Last one are Posts. Posts are related to Topics. Here we need: ``title`` , ``body`` , ``created_by`` and foreign key to ``Topic``\ :


        python manage.py scaffold forum --model Post char:title text:body foreign:created_by:User foreign:topic:Topic


All data should be in place!

Now you must add ``forum`` app to ``INSTALLED_APPS`` :

    ``
    INSTALLED_APPS = [
        # ...
        "forum",
    ]
    ``

Now you must include app in ``urls.py`` file by adding into urlpatterns:


    from django.conf.urls import url
    from django.urls import include

       urlpatterns = patterns('',

           url(r'', include('forum.urls')),

       )

Now syncdb new app and you are ready to go::
add include and url and path ro url file 
add app name to settings 
fix from django.urls import reverse in views


      python manage.py migrate --run-syncdb
      python manage.py makemigrations
      python manage.py migrate

Run your server:


   python manage.py runserver


And go to forum main page:


   http://localhost:8000/forum/


All structure are in place. Now you can personalize models, templates and urls.

At the end you can test new app by runing test:


   python manage.py test forum

   Creating test database for alias 'default'...
   .......
   ----------------------------------------------------------------------
   Ran 7 tests in 0.884s

   OK


Happy scaffolding!

This open-source app is brought to you by Tokyo Developers, Inc. ( http://tokyodevs.com/ )
