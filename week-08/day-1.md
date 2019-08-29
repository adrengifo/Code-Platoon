Day 1
=====================
### Videos (India Platoon)
* [Playlist](https://www.youtube.com/playlist?list=PLu0CiQ7bzwETyxQsXFj_HYt9VyTViUnu8)

## 3rd Party APIs

Up to this point, we have been creating CRUD apps that, while cool, are kind of boring. There's no flashiness, no _pizzazz_. Let's change that today by creating a CRUD app that utilizes a 3rd Party API (Google Maps). Before we get started with the code, I want to take some time and explain what an API is and why we use them. 

Let's think about your everyday life. You do certain things well and that's why people pay you to do those things. For the instructors at Code Platoon, we teach software development very well. You could easily teach yourself the concepts we're teaching here, but you aren't good at teaching yourself; that's why you pay us money. The same applies for hairdressers, restaurants, automotive shops, etc. Those people do certain things really well and you pay them for their expertise so that you don't need to do things yourself. Doing things yourself will have a learning curve, a financial cost, and a time cost.

The same applies to software. Let's say we want to create an app that allows us to bring users umbrellas (for a surcharge) during days that it rains and they forget to bring an umbrella. Think about all the software that you need and choose - you can either create an app that builds the following abilities from scratch:
1. Predicting weather and/or knowing the weather in all the cities in the US
    - You probably need to also keep track of all the cities in the US to begin with
2. Create a map of the entire US
3. Research how to store / process credit card payments

**Or**

Pay companies that do these things that they do really well:
1. Weather.com for weather
2. Google for maps
3. Square for credit card processing

We utilize the data / abilities of other companies through 3rd Party (i.e., not you) APIs. API stands for Application Programming Interface - it's a broad term that basically means "This is how I interact with your application." We use APIs on a daily basis:
- You INTERFACE with your boss using professional language
- You INTERFACE with small children by speaking an octave or two higher and are much more animated
- You INTERFACE with a voice box to get food at the drive through

Let's learn how to do this with code today. We're going to create a CRUD app with landmarks and plot them on a map using Google Maps API.


## Models/Migrations
Let's get set up:
```sh
$ cd ~/Desktop
$ django-admin startproject landmarks
$ cd landmarks
$ python -m venv venv
$ source venv/bin/activate
$ pip install django
$ python manage.py startapp map
```

Register your app in `settings.py`.

In `map/models.py`, let's write:
```python
from django.conf import settings
from django.db import models

class Landmark(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.name} located at {self.address}"
```

And then get a migration to put this into the database:
```sh
$ python manage.py makemigrations map
```
Finally, migrate it into your database:
```sh
$ python manage.py migrate
```

## URLs / Views
First, we need to register your map's URLs with the project's URLs:

```python
# urls.py
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('landmarks/', include('map.urls')),
]
```

Next, create `map/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landmark_list, name='landmark_list'),
]
```

In `map/views.py`, we need to get all of the code related to our views going:

```python
from django.shortcuts import render
from .models import Landmark

def landmark_list(request):
    landmarks = Landmark.objects.all()
    return render(request, 'map/landmark_list.html', {'landmarks': landmarks})
```

We do all of the controller logic before passing off the objects from the database into the templates: `map/templates/map/landmark_list.html`
```html
<div>
  <h1><a href="{% url 'landmark_list' %}">My Landmarks</a></h1>
</div>

{% for landmark in landmarks %}
  <div>
      <h2><a href="#">{{ landmark.name }}</a></h2>
      <p>Address: {{ landmark.address }}</p>
  </div>
{% endfor %}
```

## Seeds
In the shell, let's create a few landmarks:
```python
from map.models import *
Landmark.objects.create(name='The Bean', address='201 E Randolph St, Chicago IL')
Landmark.objects.create(name='Eifel Tower', address='Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France')
Landmark.objects.create(name='Golden Gate Bridge', address='Golden Gate Bridge, San Francisco, CA')
```

Visit http://localhost:8000/landmarks and see your landmarks. Next, we need a view to view each landmark. In `map/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landmark_list, name='landmark_list'),
    path('<int:landmark_id>', views.landmark_detail, name='landmark_detail')
]
```
Then in `views.py`:
```python
from django.shortcuts import render, get_object_or_404
from .models import Landmark

def landmark_list(request):
    landmarks = Landmark.objects.all()
    return render(request, 'map/landmark_list.html', {'landmarks': landmarks})

def landmark_detail(request, landmark_id):
    landmark = get_object_or_404(Landmark, pk=landmark_id)
    return render(request, 'map/landmark_detail.html', {'landmark': landmark})
```

Create a `map/landmark_detail.html` template:

```html
<div class="landmark">
  <h2>{{ landmark.name }}</h2>
  <p>{{ landmark.address }}</p>
</div>
```

And finally, in `landmark_list.html`:
```html
<div>
  <h1><a href="{% url 'landmark_list' %}">My Landmarks</a></h1>
</div>

{% for landmark in landmarks %}
  <div>
      <h2><a href="{% url 'landmark_detail' landmark_id=landmark.id %}">{{ landmark.name }}</a></h2>
      <p>Address: {{ landmark.address }}</p>
  </div>
{% endfor %}
```

Run the server and look at your app! It sucks.


## Google Maps API

Our app sucks. Looks bad, no functionality. Boo. Let's change that by getting Google Maps into our application. First, visit https://developers.google.com/maps/documentation/ and click "Maps Embed API". You can read through all of the documentation on your own. For our pursoses, you get to go down to "Get an API Key" to get an API key. This is a unique key associated with your developer account for billing/usage purposes. You have public/private API keys - the public one is the key you'll put in the URL for most GET requests. The private key is what you'll send encoded for POST requests. If you are getting charged money for using an API, you'll have a private key that you want to protect. If anyone gets a hold of your private key, they can impersonate you and you can get charged boatloads of money. Public keys are public - don't worry about protecting these. Companies generally give public keys when they don't charge for a service (like Google Maps).

After you register for an API key, copy and paste the code and put it into your `landmark_detail.html`:
```html
<div class="landmark">
  <h2>{{ landmark.name }}</h2>
  <p>{{ landmark.address }}</p>
  <iframe width="600" height="450" frameborder="0" style="border:0" src="https://www.google.com/maps/embed/v1/place?q=place_id:ChIJXfbihLwsDogR4-iwU1rM9uM&key=AIzaSyBIf0mmwGQPgH03aJRB1Bw8mPuWOP6k-no" allowfullscreen></iframe>
</div>
```

Visit http://localhost:8000/landmarks/1 and revel in the fact that we're utilizing the Google Maps API. The address is wrong though - we have hard coded the `place_id` to the Code Platoon office. It turns out that Google Maps allows you to replace `place_id` with a query string and it'll interpret things for you. When it comes to query strings and URLs in general, you can't have any spaces. That means you need to replace all strings with the unicode for space: `%20`. In `views.py`:

```python
from django.shortcuts import render, get_object_or_404
from .models import Landmark

def landmark_list(request):
    landmarks = Landmark.objects.all()
    return render(request, 'map/landmark_list.html', {'landmarks': landmarks})

def landmark_detail(request, landmark_id):
    landmark = get_object_or_404(Landmark, id=landmark_id)
    return render(request, 'map/landmark_detail.html', {'landmark': landmark, 'address': generate_google_address(landmark.address)})

def generate_google_address(address):
    modified_address = address.replace(' ', '%20')
    return f"https://www.google.com/maps/embed/v1/place?q={modified_address}&key=AIzaSyBIf0mmwGQPgH03aJRB1Bw8mPuWOP6k-no"
```

And finally, update your `landmark_detail.html`:
```html
<div class="landmark">
  <h2>{{ landmark.name }}</h2>
  <p>{{ landmark.address }}</p>
  <iframe width="600" height="450" frameborder="0" style="border:0" src="{{ address }}" allowfullscreen></iframe>
</div>
```

While today was a simple example of using a 3rd Party API, it can and will get much more complicated. Before starting on today's work, I want you to do a few refactors:
- We are currently storing our public Google API key directly in the `generate_google_address` function. This makes for weak code as if we need to change the Google API key for any reason or use it anywhere else, we'll need to replace every occurence. A better idea is to use Django environment variables through [Django Settings](https://docs.djangoproject.com/en/2.2/topics/settings/#creating-your-own-settings). Figure out how to do this and replace our key with that setting
- Implement Update and Delete on this tutorial

## Challenges
- [Ticketmaster](https://github.com/codeplatoon/ticketmaster)
