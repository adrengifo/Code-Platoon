Day 1
=====================
### Video Resources (India Platoon)
- [Week 7 Videos](https://www.youtube.com/playlist?list=PLu0CiQ7bzwEQJfDSlMPArBnfNbNvyya5P)

# Introduction to Django
Django is the web framework for Python. As we've mentioned countless times, a library is nothing more than thousands of lines of code that someone else wrote ahead of time to make your job as a developer easier. A framework is merely a bunch of libraries woven together. In today's web, we generally have a framework taking care of the backend (e.g., Django, Rails, Node) and a framework taking care of the frontend (e.g., React, Angular, Backbone). Fullstack solutions like Ruby on Rails and Django are available, but are too slow for the modern web user.

Today, we're going to get started with using Django as a full stack framework, handling both the front and back end of our application. Later, we'll learn how to run Django just as an API (backend) layer and use it in conjunction with React on the frontend.

## Setup
This tutorial is largely based off of [the official docs](https://docs.djangoproject.com/en/2.1/intro/tutorial01/). A few things have been removed for brevity and others have been added to account for our current level of knowledge. If you prefer to use their tutorial, feel free to do so.

We need to see if we've got Django already installed before anything else:
```bash
$ python -m django --version
```

If you see a version number, you're all set and have installed Django in the past. If not, you'll see `No module named django`. In that case, let's go ahead and

```bash
$ pip install Django
```

or try this if you get an error

```bash
$ pip3 install django
```

Next, let's create an project called `mysite` in our Desktop (or wherever you typically store code):

```
$ django-admin startproject mysite
$ cd mysite
$ python -m venv venv
$ source venv/bin/activate
$ pip install django
```

We have to install Django again because our virtual environment does not have it installed. We needed to install Django globally on our computer in order to run the `django-admin` command. We've got the beginnings of our Django app. Here's the breakdown of each file with explanations from the Django documentation and our explanation from us on how we interpret the Django documentation:

- `manage.py`
  - **Docs**: A command-line utility that lets you interact with this Django project in various ways
  - **Us**: It's code that allows you to use your terminal to interact with your app. This includes running migrations, interacting with the console, and starting the server. Don't worry about this file - it's given to us for free
- `mysite/__init__.py`
  - **Docs**: An empty file that tells Python that this directory should be considered a Python package
  - **Us**: It's a file with dunder (double underscores) in the filename that Python needs in order to run this properly
- `mysite/settings.py` 
  - **Docs**: Settings/configuration for this Django project
  - **Us**: This is the file that will tell Django things like which database to use, what apps are installed, etc.
- `mysite/urls.py` 
  - **Docs**: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.
  - **Us**: This is the file where you declare (write) all your routes. Think of this as the phone operator of an organization. You call the operator and tell them what you want. Then, the operator directs to you to where you need to go
- `mysite/wsgi.py` 
  - **Docs**: An entry-point for WSGI-compatible web servers to serve your project
  - **Us**: A file that you need that you don't need know too much about. It's what we need to fire the app up on different types of servers

**Let's fire up the server:** `python manage.py runserver 8000` (or just `python manage.py runserver` if you know that you always want to use the 8000 port). Next, visit http://localhost:8000 and see what you get!

**Don't worry about any unapplied migrations yet. We're not using our database just yet** 

## Poll App / Views
Open a second terminal window. In the same directory / level as `manage.py`, run:

```bash
$ cd mysite
$ source venv/bin/activate
$ python manage.py startapp polls
```

A quick sidebar - we ran `startproject` earlier and we are now running `startapp`. The difference between these two is that a `project` consists of many `apps`. An `app` can belong to many `projects`.

In `polls/views.py`, let's put the following code inside:
```python
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

We created a request method called `index` inside the `views` file. Next, we need to register this page in `polls/urls.py` **(you need to create this file)**. Create that file and paste the following code in there:

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

Finally, we will connect our recently created `urls.py` to `mysite/urls.py`. **Delete the code that is already in the `urls.py` file and replace it with the code below**:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

Whoa, a lot of code just now - let's break it down. We started off earlier with creating a project called `mysite`. Projects can consist of many apps. We then created a `polls` app which is at the same level as `mysite`. Whenever anyone hits any route (aka endpoint) with `/polls`, the `mysite/urls.py` file will direct them to the `polls` app, specifically the `urls` file. From there, it'll send the user to `index` method in `views.py`.

In `polls/urls.py`, let's break down the `path` method that we imported. `path` takes in 4 arguments. 2 of them are required and 2 of them are optional. In order, they are `route`, `view`, and `kwargs` / `name`. `route` is the path that you enter in the URL. `view` is the file that handles the logic behind what shows up on your screen. `views.index` means "Look at the index method in the `views.py` file." Finally, we passed in `name=index` to give us a `named route` to use later on.

Visit http://localhost:8000/polls to see what you get!

## Setting up our Database
Most companies use PostgreSQL as their production database. For the sake of simplicity today, we are going to use SQLite. SQLite is extraordinarily lightweight - it's essentially a file that you interact with using SQL.

Let's ensure that the `ENGINE` reads `'ENGINE': 'django.db.backends.sqlite3'` in `mysite/settings.py` before running:
```bash
$ python manage.py migrate
```

### Models & Migrations
Django's architecture is based off the MVC framework - Model, View, Controller. The Controller layer can be seen as the brains of the app; it handles the logic. The View layer is responsible for everything that a user sees, and the Model layer is what connects your Python objects to the database.

![django architecture](/week-07/django-architecture.png)

In Django, we declare all of our models in one file: `models.py`. In polls/models.py, let's write:

```python
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

We've got two tables in our polls app: question and choice. A question has `question_text` and a `published_date`, and has many choices. A choice belongs to a question through the `ForeignKey(Question`, has `choice_text` and `votes`.

Next, we have to hook up our polls app to `mysite`'s configuration in `mysite/settings.py`:
```python
INSTALLED_APPS = [
    'polls',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Now we're ready to migrate the code we wrote into `models.py`:
```bash
$ python manage.py makemigrations polls
```

A new file was created for us: `polls/migrations/0001_initial.py`. Every time that you run `python manage.py makemigrations`, it will detect differences and save it was a numbered migration under your `migrations` folder. This allows you to store changes to your models and ultimately your database schema over time. 

Finally, to get our code into the database:
```bash
$ python manage.py migrate
```

### Playing with the Django shell
To get us started, let's install Django Extensions:

```bash
$ pip install django-extensions
```
Then in `settings.py`, add it to your `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'django_extensions',
    ...
]
```

Finally, let's get the shell loaded up:
```
$ python manage.py shell_plus
```
This gives us access to the Python shell, but with our entire app loaded into it! We can interact with the database using Python code"

```python
Question.objects.all() # should return an empty collection, which makes sense since we have nothing in the database yet. Let's create a question record.

from django.utils import timezone
question = Question(question_text="What's new?", pub_date=timezone.now())
question.save()
question.id
question.question_text
question.pub_date

# If you want to change the attributes, go ahead and overwrite them, then call save()
question.question_text = 'What is up?'
question.save()

# Now if you wanted to get all the questions
Question.objects.all()
```

You'll notice that the result we get back (`<Question: Question object (1)>`) is not descriptive and sucks. In `polls/models.py`, we are going to add a `__str__` method in for Question and Choice. All dunder methods are built in to Django; the dunder `str` method is a method we're going to overwrite so that we get a better description of each object.

```python
# polls/models.py
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return f"ID: {self.id} Question Text: {self.question_text}"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return f"ID: {self.id} Choice Text: {self.choice_text}"
```

Fire up a new console and run some commands. A bunch of commands can be found [here](https://docs.djangoproject.com/en/2.1/topics/db/queries/):

```python
Question.objects.all() # note how you get a much more descriptive representation than what you got before

question = Question.objects.get(id=1)
question.choices.all() # verifying that we have no choices for our questions
```

What the heck is `choices`? Remember `related_name` from the Associations challenge? This is where it comes into play. If you don't have a `related_name`, you need to type `tablename_set` in order to get from one Python object to another. Let's add `related_name='choices'` to our `Choice` model and try running `question.choices.all`. You should see the same `QuerySet` as a result.

```python
question.choices.all() # verifying that we have no choices for our questions
# Let's create 3 choice objects that are linked to our question variable
question.choices.create(choice_text='Not much', votes=0)
question.choices.create(choice_text='The sky', votes=0)
choice = question.choices.create(choice_text='Just hacking again', votes=0)

# Now we can go from a question to a choice and vice versa
question.choices.all()
choice.question
```

## Additional Views
We're going to add 3 new routes:
- `/polls/:question_id` (view a particular question)
- `/polls/:question_id/results` (view the results of that particular question)
- `/polls/:question_id/vote` (vote on the choices on that question)

In `polls/urls.py`, let's register these routes and their corresponding methods:
```python
from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

Next, create the following methods in `polls/views.py`:
```python
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}.")

def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
```
Visit those routes with `question_id` as 1 and see what you get!

### Templating
Of course, having plain text is not terribly useful. We want to create templates in HTML (the View layer of MVC) where we can pass in Python objects of data. Under your `polls` directory, create a `templates` folder, and under that directory, create a `polls` folder, and under that directory create an `index.html` file:

```html
<h1> All Polls </h1>
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

Next, we'll update the `index` view in `polls/views.py` to account for this:
```python
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    data = { 'latest_question_list': latest_question_list }
    return render(request, 'polls/index.html', data)

def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}.")

def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
```

If you were to visit http://localhost:8000/polls, you'd see all of the questions we've written thus far. Let's move onto the detail function in our `polls/views.py` file which will be `/polls/1` page:


```python
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    data = { 'latest_question_list': latest_question_list }
    return render(request, 'polls/index.html', data)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    data = { 'question': question }
    return render(request, 'polls/detail.html', data)

def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
```

In our **`polls/templates/polls`** directory create a file called `detail.html`:

```
<h1> Details about Question {{ question.id }} </h1>
<h2> {{ question.question_text }} </h2>
<ul>
{% for choice in question.choices.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

### Django Helper Methods
Helper methods are methods that help you write code faster / better. Let's stop for a second and look at our `/index` HTML and see what we can refactor:
```
<h1> All Polls </h1>
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```
Right in the middle of the page we see that we've hardcoded the URL. Anytime you hardcode (force the code to operate a certain way), you have written brittle/unscaleable code. Instead let's use Django's helpers to improve our code. First, let's create a "named route" (`name=`) so that we don't need to hardcode. 
```python
# polls/urls.py
from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```
And now let's change the view code in `polls/templates/polls/index.html`
```
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```
Let's break down what we just did. In our `urls.py`, we namespaced our app with `app_name` so that when we say `polls:detail`, there is no doubt about which app is using the named route `detail`. Remember that a Django project can have many apps and that one of those other apps could have `detail`. With `polls:detail`, there is no doubt of which route we're using. For `detail` specifically, the route is `/polls/<int:question_id>`. We are passing that id number into the named route so that it automatically populates the URL.

### Forms in Django
Let's create a form so that people can vote on a question. In `polls/templates/polls/detail.html`, put the following code:

```html
<h1> Details about Question {{ question.id }} </h1>
<h2> {{ question.question_text }} </h2>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choices.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
{% endfor %}
<input type="submit" value="Vote">
</form>
```
There are a few things to note with this form:
1. We are outputting error messages if they are present
2. We are explicitly declaring that the method for our form is `POST` because we are _sending_ information
3. We're creating a bunch of radio button options in one loop to account for each `choice` for our `question`. Each radio button has an unique `id` using `forloop.counter` (comes for free with Python)

If you refresh your page (`/polls/1`), you'll see your choices come on the screen. Submit it and you'll be direceted to a page that simply says "You are voting on question 1". That's because we haven't accounted for the `POST` request in our code yet. If you look in your `urls.py`, you'll see that we defined the route but the action in `views.py` isn't really doing anything yet. We need to fix that up!

```python
# polls/views.py
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    data = { 'latest_question_list': latest_question_list }
    return render(request, 'polls/index.html', data)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist): 
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

We've rewritten a lot of code. Let's break down the differences:
```python
from django.http import HttpResponse, HttpResponseRedirect # brings in the ability to redirect the user
from django.shortcuts import get_object_or_404, render # same as before
from django.urls import reverse # The reverse library gives us the ability to read the previous URL and just use reverse in our code so that we don't need to hard code the URL

from .models import Question, Choice # bring in the Choice model because we need it to talk to the DB

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # get the question from the database using the id number found in the URL
    try: # try to do this
        selected_choice = question.choices.get(pk=request.POST['choice']) # find the choice that the user submitted in the form
    except (KeyError, Choice.DoesNotExist): # couldn't find the selected_choice above will raise an error. using "except" will catch that error from blowing up the app
        return render(request, 'polls/detail.html', { # re-display the question voting form
            'question': question,
            'error_message': "You didn't select a choice.", # these two are local variables that the view needs. this "error_message" is specifically for that
            # {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %} line of code
        })
    else:
        selected_choice.votes += 1 # add 1 to the number of votes for that selected choice
        selected_choice.save() # save it to the database
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))      
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
```

When we vote, we get redirected to the results page which just has some text in it. Let's alter that:
```python
# polls/views.py
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
```
`results` is telling us to create a `results.html` file in our `polls/templates/polls` directory:
```
<h1> Details about Question {{ question.id }} </h1>
<h2> {{ question.question_text }} </h2>

<ul>
{% for choice in question.choices.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
{% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>
```

### Wrapping Up
If you take a step back, we've created a small app where you can vote on a poll question. While you can't create/read/update/destroy any new questions/choices, we've done quite a bit. Over the next two days, we'll be writing CRUD apps in Django but today is meant to give you an understanding its basic file structure and how to hook up everything.

## Assignments
- Before doing anything, make sure that you run through this tutorial and understand what's going on
- [Posts and Comments](https://github.com/codeplatoon/posts-and-comments)
