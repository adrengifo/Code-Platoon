Day 3
=====================
### Video Resources (India Platoon)
- [Week 7 Videos](https://www.youtube.com/playlist?list=PLu0CiQ7bzwEQJfDSlMPArBnfNbNvyya5P)

Today, we're going to be focusing on the built-in Django admin panel, styling our app using Bootstrap, and the concept of base layouts. We'll build a blog app where authors can CRUD posts.

Let's create a fresh project:

```bash
$ cd ~/Desktop
$ django-admin startproject mysite
$ cd mysite
$ python -m venv venv
$ source venv/bin/activate
$ pip install django
```

## Blog Models
Let's get our blog app set up:

```bash
$ python manage.py startapp blog
```

We get our usual Django skeleton and now, we're going to get our models set up. We'll say that a blog has an author, title, text, and published_date. In `blog/models.py`, let's write:

```python
from django.conf import settings
from django.db import models

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
```

Let's get a migration into the database:

```bash
$ python manage.py makemigrations blog
```

Oops - we get an error! We forgot to register our app to the project directory. Do that before going forward.

# Django Admin
One of the best features of Django is the ability to use their built-in admin dashboard to CRUD models in your database. We're going to use this today in `blog/admin.py`:

```python
from django.contrib import admin # brings in the admin ability
from .models import Post # brings in your Post model from the models.py file

admin.site.register(Post) # registers Post with your admin ability
```

Next, let's run all the migrations with your admin functionality and fire up the server:

```bash
$ python manage.py migrate
$ python manage.py runserver
```

If you visit http://localhost:8000/admin, you have a built-in dashboard. Try logging in and you realize that you haven't created a superuser yet:

```bash
$ python manage.py createsuperuser
```

Run through your setup, log in, and create 2-3 blog posts. It's super easy to CRUD blog posts as a super administrator and sometimes, this is all that you need. We'll create forms later to CRUD blog posts without being a super administrator.

## URLs / Views
First, we need to register your blog's URLs with the project's URLs:

```python
# urls.py
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('blog.urls')),
]
```

Next, create `blog/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
```

In `blog/views.py`, we need to get all of the code related to our views going:

```python
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
```

We do all of the controller logic before passing off the objects from the database into the templates: `blog/templates/blog/post_list.html`
```html
<div>
  <h1><a href="{% url 'post_list' %}">My Blog</a></h1>
</div>

{% for post in posts %}
  <div>
      <h2><a href="">{{ post.title }}</a></h2>
      <p>published: {{ post.published_date }}</p>
      <p>{{ post.text|linebreaksbr }}</p>
  </div>
{% endfor %}
```

Visit http://localhost:8000/posts and see your ugly code. Let's style it in the next section.

## Styling
Our website is functional, but it's also hideous. We are going to add Bootstrap to make it look nice with just a few lines of code. Let's add a few things to our `post_list.html` to get us started:

```html
<head>
  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
</head>

<div>
  <h1><a href="{% url 'post_list' %}">My Blog</a></h1>
</div>

{% for post in posts %}
  <div>
      <h2><a href="">{{ post.title }}</a></h2>
      <p>published: {{ post.published_date }}</p>
      <p>{{ post.text|linebreaksbr }}</p>
  </div>
{% endfor %}
```

Next, we will need to create our first static file for custom CSS to make it look pretty under `blog/static/css/blog.css`:

```css
h1 a, h2 a {
    color: #C25100;
}

body {
    padding-left: 15px;
}
```

In our `post_list.html` file, we need to tell the file that we want to load some static files and will be bringing in external stylesheets:

```html
{% load static %}
<html>
  <head>
    <title>My Blog</title>
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="{% static 'css/blog.css' %}">
  </head>

  <div>
    <h1><a href="{% url 'post_list' %}">My Blog</a></h1>
  </div>

  {% for post in posts %}
    <div>
        <h2><a href="">{{ post.title }}</a></h2>
        <p>published: {{ post.published_date }}</p>
        <p>{{ post.text|linebreaksbr }}</p>
    </div>
  {% endfor %}
</html>
```

Restart the server and see your slightly better looking website. It's good, but we want to make it look better. Let's bring in an external font to our header by adding `<link href="//fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext" rel="stylesheet" type="text/css">` to `post_list.html`'s head and `font-family: 'Lobster';` to the CSS for the h1/h2 tags. If you refresh the page now, it's got some fancy script going on.

We want to optimize our CSS by breaking down our page into different sections and writing CSS for those sections. We'll be creating a CSS for our header and for our post list. Let's wrap those `div`'s with class names in `post_list.html` and add a few CSS classes:

```html
{% load static %}
<html>
  <head>
    <title>My Blog</title>
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    <link href="//fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext" rel="stylesheet" type="text/css">
  </head>

  <div class="page-header">
    <h1><a href="{% url 'post_list' %}">My Blog</a></h1>
  </div>

  <div class="content container">
    <div class="row">
        <div class="col-md-8">
            {% for post in posts %}
                <div class="post">
                    <div class="date">
                        <p>published: {{ post.published_date }}</p>
                    </div>
                    <h2><a href="">{{ post.title }}</a></h2>
                    <p>{{ post.text|linebreaksbr }}</p>
                </div>
            {% endfor %}
        </div>
    </div>
  </div>
</html>
```
Finally, let's change `blog.css`:
```css
.page-header {
    background-color: #C25100;
    margin-top: 0;
    padding: 20px 20px 20px 40px;
}

.page-header h1, .page-header h1 a, .page-header h1 a:visited, .page-header h1 a:active {
    color: #ffffff;
    font-size: 36pt;
    text-decoration: none;
}

.content {
    margin-left: 40px;
}

h1, h2, h3, h4 {
    font-family: 'Lobster', cursive;
}

.date {
    color: #828282;
}

.save {
    float: right;
}

.post-form textarea, .post-form input {
    width: 100%;
}

.top-menu, .top-menu:hover, .top-menu:visited {
    color: #ffffff;
    float: right;
    font-size: 26pt;
    margin-right: 20px;
}

.post {
    margin-bottom: 70px;
}

.post h1 a, .post h1 a:visited {
    color: #000000;
}
```
If you refresh the page, it looks amazing! Take a breather before moving onto the next section on templating.

## Templating
Template extending is the act of writing HTML/CSS one time (writing a template) and using it in other files/pages (extending). Think of Amazon - on every page, there's similar code at the top and bottom of the page. Do you think they write every bit of HTML/CSS for every page? No! They use a templating system to put the header/footer every time before changing the middle section.

You can also think of it as a form letter. A company will print out a templated letter and substitute in your name at the top. They don't have a new letter for each person. That same concept extends to Django. Let's start by creating `blog/templates/blog/base.html`:
```html
{% load static %}
<html>
    <head>
        <title>My Blog</title>
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
        <link href='//fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    </head>
    <body>
        <div class="page-header">
            <h1><a href="{% url 'post_list' %}">My Blog</a></h1>
        </div>

        <div class="content container">
            <div class="row">
                <div class="col-md-8">
                  {% block content %}
                  {% endblock %}
                </div>
            </div>
        </div>
    </body>
</html>
```
Right now, `base.html` and `poll_list.html` look very similar, but we've taken out the post section and are going to let that individual file take care of rendering the list of posts in `post_list.html`:
```html
{% extends 'blog/base.html' %}

{% block content %}
  {% for post in posts %}
      <div class="post">
          <div class="date">
              {{ post.published_date }}
          </div>
          <h2><a href="">{{ post.title }}</a></h2>
          <p>{{ post.text|linebreaksbr }}</p>
      </div>
  {% endfor %}
{% endblock %}
```
We've told this html file that we first want to load `base.html` and then put the `block content` into where it looks for `block content` in `base.html`. Restart your server and ensure everything is working the same as before. Though the functionality hasn't changed, we've created more reusable code for the future.

## Extending Templates
Right now, our template extending only goes to a full list of posts. Let's change that so that we are tackling an individual post. Let's start by changing the `href` in `post_list.html` to use the url helper:
```html
{% extends 'blog/base.html' %}

{% block content %}
  {% for post in posts %}
      <div class="post">
          <div class="date">
              {{ post.published_date }}
          </div>
          <h2><a href="{% url 'post_detail' post_id=post.id %}">{{ post.title }}</a></h2>
          <p>{{ post.text|linebreaksbr }}</p>
      </div>
  {% endfor %}
{% endblock %}
```

Next, create the URL in `urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:post_id>', views.post_detail, name='post_detail'),
]
```

After that, we need to create a method in the controller that will connect with the Post model in `views.py`:

```python
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})
```

Finally, let's get a template in there with `blog/post_detail.html`:
```html
{% extends 'blog/base.html' %}

{% block content %}
    <div class="post">
        {% if post.published_date %}
            <div class="date">
                {{ post.published_date }}
            </div>
        {% endif %}
        <h2>{{ post.title }}</h2>
        <p>{{ post.text|linebreaksbr }}</p>
    </div>
{% endblock %}
```

## Finally, Forms
Let's get our forms going and CRUD Post by creating `blog/forms.py`:
```python
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
```
The magic comes from `forms.ModelForm` and the `Meta` class. A form will automagically get created for us.

Let's create a link for a user to create a new blog post in `base.html`:
```html
<div class="page-header">
    <a href="{% url 'new_post' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
    <h1><a href="/">My Blog</a></h1>
</div>
```

Next, in `blog/urls.py`, we need to add that URL in:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:post_id>', views.post_detail, name='post_detail'),
    path('new', views.new_post, name='new_post'),
]
```
Two more things: the controller action and the template. First the controller action in `views.py`:
```python
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def new_post(request):
    form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form, 'type_of_request': 'new'})
```

Let's get our `post_form.html` created:
```html
{% extends 'blog/base.html' %}

{% block content %}
    <h2>{{ type_of_request }} Post</h2>
    <form method="POST" class="post-form">{% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="save btn btn-default">Save</button>
    </form>
{% endblock %}
```

Visit the page and you'll see your awesome form! Submit it and it'll do nothing. Let's edit our `new_post` function:
```python
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
import datetime
# ...

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.all()[0]
            post.published_date = datetime.datetime.now()
            post.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form, 'type_of_request': 'New'})
```

Looks like we can now Create a new blog post, Read a blog post, but what about Update and Delete? Let's knock it out. First in `post_detail.html`:
```html
{% extends 'blog/base.html' %}

{% block content %}
    <div class="post">
        {% if post.published_date %}
            <div class="date">
                {{ post.published_date }}
            </div>
        {% endif %}
        <a class="btn btn-default" href="{% url 'edit_post' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
        <h2>{{ post.title }}</h2>
        <p>{{ post.text|linebreaksbr }}</p>
    </div>
{% endblock %}
```
Let's create a URL for that in `urls.py`:
```python

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:post_id>', views.post_detail, name='post_detail'),
    path('new', views.new_post, name='new_post'),
    path('<int:post_id>/edit', views.edit_post, name='edit_post'),
]
```
A controller action comes next in `views.py`:
```python
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.all()[0]
            post.published_date = datetime.datetime.now()
            post.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form, 'type_of_request': 'Edit'})
```

Note that we don't have a form for edit specifically, we're going to reuse the form template. Try editing it - it actually works right out of the box!

Finally, let's delete a blog post if we don't like it by adding a link in the `post_detail.html` template:
```html
<a href="{% url 'delete_post' post_id=post.id %}">Delete This Post</a>
```
Let's create the route in `urls.py`:
```python
path('<int:post_id>/delete', views.delete_post, name='delete_post'),
```

Finally, the action in `views.py`:
```python
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('post_list')
```
We're done with CRUD! To turn off the virtual environment, simply run `deactivate` from the command line

### Acknowledgements
This tutorial is largely based off [Django Girls](https://tutorial.djangogirls.org/) and we thank them for open-sourcing everything!

## Assignments
- Before doing anything, make sure that you run through this tutorial and understand what's going on
- [Event Calendar](https://github.com/codeplatoon/django-event-calendar)
