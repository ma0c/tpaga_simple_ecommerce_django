# base-django

Base Django is a base application to build fastest django application.

Base provides a boilerplate to create Class Based Views and a set of useful models to use in a ready to go app.

We recommend use base with [Django CRUD generator](https://git.contraslash.com/ma0/django-crud-generator) 
(also mirrored on [github](https://github.com/contraslash/django-crud-generator)), to create CRUD segments in
minutes.
  
Try:

```bash
pip install django-crud-generator
cd your/django/project/folder
git submodule add https://github.com/contraslash/base-django base
django-crud-generator.py --django_application_folder your/application/folder --model_name YourModelName 
```

We assume you have a `base.html` file with this a main block content, example:

```html
<html>
    <head>
    
    </head>
    <body>
        {% block content %}
        
        {% endblock %}
    </body>
</html>
```

We support these CSS Frameworks:

- [Bootstrap](templates/base/bootstrap)
- [Materialize](templates/base/bootstrap)

Base uses [messages](https://docs.djangoproject.com/en/1.11/ref/contrib/messages/) Framework, with bootstrap you can use like:

```html
<html>
    ...
    <body>
        ...
        {% for message in messages %}
            <div class="alert alert-{{ message.level_tag }} alert-dismissible" role="alert">
                <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                {{ message }}
            </div>
        {% endfor %}
        {% block content %}
        
        {% endblock %}
    </body>
</html>
```

We also provide an [authentication package](https://git.contraslash.com/ma0/authentication-django), (also mirrored in
[github](https://github.com/ma0c/authentication-django)) to speed up authentication