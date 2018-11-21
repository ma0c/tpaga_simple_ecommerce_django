# tpaga_simple_ecommerce_django

This structure was automatically created by [Django Bootstrapper](https://pypi.org/project/django-bootstrapper/)

Default folder structure:

```bash
project_folder
├── applications
│   ├── authentication (Authentication from https://github.com/contraslash/authentication-django)
│   ├── base_template (Base template from https://github.com/contraslash/template_eventually_html5up-django)
│   └── __init__.py
├── base (base from https://github.com/contraslash/base-django)
├── manage.py
└── project_name
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## Estimated time
Understanding problem: 30m
Understanding TPaga API: 30m
Searching for a template: 30m
Integrating template in a generic way with pertinent modifications: 30m
Creating an app to manage e-commerce basic functionality: 1h
Creating a python package to integrate with TPaga API: 1h
Integrating package with e-commerce: 30m
Manage permissions to reverse payment: 30m

## Commit notes
First commit: 
Project structure using Django Bootstrapper, also base_template_app was previously created

---
Second commit:
Create a simple e-commerce app
Creating CRUD operations with of Item, Order and Order Item [django-crud-generator](https://pypi.org/project/django-crud-generator/)
Creating logic for create a random order and preparing page for checkout
---
Third commit:
Created a module to manage connections with TPaga
---
Fourth commit:
Merge tpaga module with project
Created new views to manage operators and refunds
Deployment with docker
Configure S3 as Static file server
Configure Drone to automatic builds and deploy


## Installation

First clone the full project with all submodules

```bash
git clone --recursive http://git.contraslash.com/ma0/tpaga
```

You require a virtual env for run this project

```bash
python3 -m venv tpaga_simple_ecommerce_django_env
source tpaga_simple_ecommerce_django_env/bin/activate
```

Then install the requirements

```bash
pip install -r requirements.txt
# Be carefull because requirements uses uwsgi and mysqlclient which uses SO packages 
```

Then initialize the SQLite database

```bash
python manage.py migrate
# And also create a superuser
python manage.py createsuperuser
```

Then configure the application
```bash
python manage.py shell
# And inside the shell
from tpaga_simple_ecommerce_django import setup
setup.setup()
```

Now execute the development server using environment variables to connect with TPaga

```bash
DEBUG=True TPAGA_USERNAME="your_tpaga_miniapp_username" TPAGA_PASSWORD="your_tpaga_miniapp_password" python manage.py runserver
```

```bash
docker build -t contraslash/tpaga .
docker run \
    -p 8000:8000 \
    -e DEBUG=True \
    contraslash/tpaga
```
