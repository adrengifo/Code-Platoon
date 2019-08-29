Day 4
=====================
### Video Resources (India Platoon)
- [Week 7 Videos](https://www.youtube.com/playlist?list=PLu0CiQ7bzwEQJfDSlMPArBnfNbNvyya5P)

## Authentication in Django
Up to this point, we haven't had the ability to log in or out of our application. We're going to start implementing sign up, log in, and log out with help from [WS Vincent](https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/).

On your desktop, create a project called accounts and do your usual Django setup:
```sh
$ cd ~/Desktop
$ django-admin startproject my_project
$ cd my_project
$ python -m venv venv
$ source venv/bin/activate
$ pip install django
$ python manage.py migrate
```

This is the same series of commands you've run for the past few days (i.e., you haven't done anything new), but if you look inside `settings.py`'s `INSTALLED_APPS`, there is a `'django.contrib.auth'` library that comes for free. This preinstalled library gives you much of the functionality of authentication that you need.

To get the routes for authentication, go inside `my_project/urls.py` and add this code:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
```

That one extra line of code for `accounts/` gives us the following URLs:
```
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
```

Like normal routes, we need templates. With that let's create `templates/registration/login.html` at the same level as `my_project` (i.e., not within `my_project`) to get started:
```html
<h2>Login</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Login</button>
</form>
```

We usually use templates within apps, but since this `accounts` functionality is at the project level, we have to have a templates folder at the project level. We also need to register these templates in `settings.py`:
```python
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    },
]

# at the bottom of the file
LOGIN_REDIRECT_URL = '/'
```

Just like yesterday, we want to create a base template and a homepage template that will be rendered before we do anything. First, in `my_project/urls.py`, add this code:

```python
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
]
```

Next, in the `templates/` folder you created, create two additional files. First, `base.html`:

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{% block title %}Django Auth Tutorial{% endblock %}</title>
</head>
<body>
  <main>
    {% block content %}
    {% endblock %}
  </main>
</body>
</html>
```
and `home.html`:
```html
<!-- templates/home.html -->
{% extends 'base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
{% if user.is_authenticated %}
  Hi {{ user.username }}!
  <p><a href="{% url 'logout' %}">logout</a></p>
{% else %}
  <p>You are not logged in</p>
  <a href="{% url 'login' %}">login</a>
{% endif %}
{% endblock %}
```

Now, let's edit `templates/accounts/login.html` to use our base:
```html
<!-- templates/registration/login.html -->
{% extends 'base.html' %}

{% block title %}Login{% endblock %}

{% block content %}
<h2>Login</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Login</button>
</form>
{% endblock %}
```

If you visit http://localhost:8000/accounts/login, you'll see a login page that comes for free. Before we can login, however, we'll need a user:
```sh
$ python manage.py createsuperuser
```

Try logging in! But wait, how do we log out? Let's add this into `settings.py` at the very bottom:
```python
LOGOUT_REDIRECT_URL = 'home'
```
And just like that, we can log in and out! Take a breather before jumping into signing up a user in the next section.

## Sign Up
For this section, we're going to need to create our own view and url for signup. As a result, we'll create our own dedicated app called `accounts`:

```sh
$ python manage.py startapp accounts
```

Register this in `settings.py` as an `INSTALLED_APP`:
```python
'accounts',
```

Next, in `my_project/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
```

Let's get `accounts/urls.py` set up:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]
```

As we see in `urlpatterns`, we need to set up our `SignUp` in `views.py`:
```python
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
```

That last line tells us that we need a `signup.html` template in `templates/signup.html`:
```html
{% extends 'base.html' %}

{% block title %}Sign Up{% endblock %}

{% block content %}
  <h2>Sign up</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Sign up</button>
  </form>
{% endblock %}
```

Visit http://localhost:8000/accounts/signup/, sign up, and log in! If you are interested in password reset, go through the tutorial written by WS Vincent [here](https://wsvincent.com/django-user-authentication-tutorial-password-reset/)

### Challenges
- Add sign up, login, and log out functionality to your completed...
  - [ToDo List](https://github.com/codeplatoon/django-todo)
  - [Event Calendar](https://github.com/codeplatoon/django-event-calendar)
