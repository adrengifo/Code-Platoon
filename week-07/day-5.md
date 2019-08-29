Day 5
=====================
### Video Resources (India Platoon)
- [Week 7 Videos](https://www.youtube.com/playlist?list=PLu0CiQ7bzwEQJfDSlMPArBnfNbNvyya5P)

# Nested CRUD in Django
We've been creating apps that CRUD a single resource (i.e., `model`) for quite a while now. In fullstack applications, there a concept called `Nested CRUD` where you `nest` certain resources under other ones in your URL. The parent resource is the top level, followed by the child level. If you nest your URLs, you'll generally only nest 2 resources but you could theoretically nest an unlimited number of resources. You'll see this in action in just a bit.

Let's create an nested CRUD application today called `cohorts_and_students`. In this challenge, we will CRUD a `cohort` and its associated `students`. Let's go with Code Platoon's Bravo and Charlie platoons. Starting off, we'll create an app:

```sh
$ cd ~/Desktop
$ mkdir nested-crud-example && cd nested-crud-example
$ python -m venv venv
$ source venv/bin/activate
$ pip install django
$ django-admin startproject old_cohorts .
```

Let's next get our `cohorts_and_students` app set up:
```sh
$ python manage.py startapp cohorts_and_students
```

And of course, we have to register this new app with our `old_cohorts` project in `settings.py`:

```python
INSTALLED_APPS = [
  # ...
  'cohorts_and_students',
]
```

Let's get our models going in `cohorts_and_students/models.py`:

```python
from django.conf import settings
from django.db import models

class Cohort(models.Model):
    cohort_name = models.CharField(max_length=200)
    start_date = models.CharField(max_length=200) # in a real example, we'd want this to be a date field
    end_date = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.cohort_name} started on {self.start_date} and ended on {self.end_date}"

class Student(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='students')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
```

Let's run the commands to get the migrations going:
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

Let's get some data in the database before beginning:

```sh
$ python manage.py shell
...

from cohorts_and_students.models import Cohort, Student

bravo = Cohort(cohort_name='Bravo', start_date='1/4/17', end_date='5/1/17')
bravo.save()

charlie = Cohort(cohort_name='Charlie', start_date='5/27/17', end_date='8/10/17')
charlie.save()

student_1 = Student(cohort=bravo, first_name='Conlin', last_name='M')
student_1.save()

student_2 = Student(cohort=bravo, first_name='Scott', last_name='P')
student_2.save()

student_3 = Student(cohort=bravo, first_name='Mike', last_name='L')
student_3.save()

student_4 = Student(cohort=bravo, first_name='Jin', last_name='C')
student_4.save()

student_5 = Student(cohort=bravo, first_name='Darnell', last_name='G')
student_5.save()

student_6 = Student(cohort=bravo, first_name='Arthur', last_name='M')
student_6.save()
```


## URLs
First, we need to register our `cohorts_and_students`'s URLs with the project's URLs:

```python
# urls.py
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cohorts/', include('cohorts_and_students.urls')),
]
```

Next, create `cohorts_and_students/urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cohort_list, name='cohort_list'),
    path('new', views.new_cohort, name='new_cohort'),
    path('<int:cohort_id>', views.cohort_detail, name='cohort_detail'),
    path('<int:cohort_id>/edit', views.edit_cohort, name='edit_cohort'),
    path('<int:cohort_id>/delete', views.delete_cohort, name='delete_cohort'),
    # path('<int:cohort_id>/students', views.student_list, name='student_list'),
    # path('<int:cohort_id>/students/new', views.new_student, name='new_student'),
    # path('<int:cohort_id>/students/<int:student_id>', views.student_detail, name='student_detail'),
    # path('<int:cohort_id>/students/<int:student_id>/edit', views.edit_student, name='edit_student'),
    # path('<int:cohort_id>/students/<int:student_id>/delete', views.delete_student, name='delete_student'),
]
```

Whoa. We have a lot of routes. Some we have seen before and others we have not. Let's break them down:

```python
path('', views.cohort_list, name='cohort_list'), # list all the cohorts
path('new', views.new_cohort, name='new_cohort'), # form page for creating a new cohort
path('<int:cohort_id>', views.cohort_detail, name='cohort_detail'), # view details about an existing cohort
path('<int:cohort_id>/edit', views.edit_cohort, name='edit_cohort'), # form page for editing a cohort
path('<int:cohort_id>/delete', views.delete_cohort, name='delete_cohort'), # delete a cohort
# path('<int:cohort_id>/students', views.student_list, name='student_list'), # list all of the students for a cohort
# path('<int:cohort_id>/students/new', views.new_student, name='new_student'), # form page for creating a new student for a cohort
# path('<int:cohort_id>/students/<int:student_id>', views.student_detail, name='student_detail'), # view details about a student in a cohort
# path('<int:cohort_id>/students/<int:student_id>/edit', views.edit_student, name='edit_student'), # form page for editing a student for a cohort 
# path('<int:cohort_id>/students/<int:student_id>/delete', views.delete_student, name='delete_student'), # delete a student for a cohort
```

You will notice that instead of `<int:pk>` like we used in single resource CRUD, we are now using more descriptive variable names to store the numbers in our URLs like `cohort_id` and `student_id`. By doing labeling it this way, we avoid issues understanding which ID number we're talking about and which resource they refer to.

Let's create our `views.py` file as it's vitally important:
```python
# Just the methods for cohorts
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Cohort
from .forms import CohortForm

def cohort_list(request):
    cohorts = Cohort.objects.all()
    return render(request, 'cohorts/cohorts_list.html', {'cohorts': cohorts})

def cohort_detail(request, cohort_id):
    cohort = get_object_or_404(Cohort, id=cohort_id)
    return render(request, 'cohorts/cohort_detail.html', {'cohort': cohort})

def new_cohort(request):
    if request.method == "POST":
        form = CohortForm(request.POST)
        if form.is_valid():
            cohort = form.save(commit=False)
            cohort.save()
            return redirect('cohort_detail', cohort_id=cohort.id)
    else:
        form = CohortForm()
    return render(request, 'cohorts/cohort_form.html', {'form': form, 'type_of_request': 'New'})

def edit_cohort(request, cohort_id):
    cohort = get_object_or_404(Cohort, id=cohort_id)
    if request.method == "POST":
        form = CohortForm(request.POST, instance=cohort)
        if form.is_valid():
            cohort = form.save(commit=False)
            cohort.save()
            return redirect('cohort_detail', cohort_id=cohort.id)
    else:
        form = CohortForm(instance=cohort)
    return render(request, 'cohorts/cohort_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_cohort(request, cohort_id):
    cohort = get_object_or_404(Cohort, id=cohort_id)
    cohort.delete()
    return redirect('cohort_list')
```

Next, create a form in `forms.py`:
```python
from django import forms
from .models import Cohort, Student

class CohortForm(forms.ModelForm):
    class Meta:
        model = Cohort
        fields = ('cohort_name', 'start_date', 'end_date')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('cohort', 'first_name', 'last_name') 
```

Finally, let's get the `templates/cohorts/` folder going and get some files in there:

```python
# cohorts_list.html
<h1> All Cohorts </h1>

<ul>
  {% for cohort in cohorts %}
    <div>
      <li><a href="{% url 'cohort_detail' cohort_id=cohort.id %}">{{ cohort.cohort_name }}</a></li>
    </div>
  {% endfor %}
</ul>

<a href="{% url 'new_cohort' %}">Create a new cohort</a>
```

```python
# cohort_detail.html
<div>
  <h2>{{ cohort.cohort_name }}</h2>
  <p> Start Date: {{ cohort.start_date|linebreaksbr }}</p>
  <p> End Date: {{ cohort.end_date|linebreaksbr }}</p>
  <br>
  <br>
  <a href="{% url 'edit_cohort' cohort_id=cohort.id %}"> Edit cohort</a>
  <a href="{% url 'delete_cohort' cohort_id=cohort.id %}">Delete cohort</a>
</div>
```

```python
# cohort_form.html
<h2>{{ type_of_request }} Cohort</h2>
<form method="POST">{% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Save</button>
</form>
```

Fire up your server (`python manage.py runserver`) and visit http://localhost:8000/cohorts. You can now CRUD one resource. Let's do a nested CRUD in the next section.

## Nested CRUD
To begin, let's uncomment the stuff in `urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cohort_list, name='cohort_list'),
    path('new', views.new_cohort, name='new_cohort'),
    path('<int:cohort_id>', views.cohort_detail, name='cohort_detail'),
    path('<int:cohort_id>/edit', views.edit_cohort, name='edit_cohort'),
    path('<int:cohort_id>/delete', views.delete_cohort, name='delete_cohort'),
    path('<int:cohort_id>/students', views.student_list, name='student_list'),
    path('<int:cohort_id>/students/new', views.new_student, name='new_student'),
    path('<int:cohort_id>/students/<int:student_id>', views.student_detail, name='student_detail'),
    path('<int:cohort_id>/students/<int:student_id>/edit', views.edit_student, name='edit_student'),
    path('<int:cohort_id>/students/<int:student_id>/delete', views.delete_student, name='delete_student'),
]
```
Next, let's add those controller actions in `views.py`:
```python
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Cohort, Student
from .forms import CohortForm, StudentForm

# ... All of the cohort controller actions

def student_list(request, cohort_id):
    cohort = get_object_or_404(Cohort, id=cohort_id)
    students = cohort.students.all()
    return render(request, 'students/students_list.html', {'cohort': cohort, 'students': students})

def student_detail(request, cohort_id, student_id):
    cohort = get_object_or_404(Cohort, id=cohort_id)
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'students/student_detail.html', {'cohort': cohort, 'student': student})

def new_student(request, cohort_id):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('student_detail', cohort_id=cohort_id, student_id=student.id)
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form, 'type_of_request': 'New'})

def edit_student(request, cohort_id, student_id):
    cohort = get_object_or_404(Cohort, id=cohort_id)
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('student_detail', student_id=student.id, cohort_id=cohort_id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_student(request, cohort_id, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('student_list', cohort_id=cohort_id)
```

In `templates/cohorts/cohort_detail.html`, add this code to the end:
```html
<hr/>
<div>
  <a href="{% url 'student_list' cohort_id=cohort.id %}">Students in this cohort</a>
</div>
```

From here, let's create some views in `templates/students/`:
```html
# student_detail.html
<div>
  <h2>{{student.first_name}} {{student.last_name}}</h2>
  <p>Member of {{cohort.cohort_name}}</p>
  
  <br>
  <br>
  <a href="{% url 'edit_student' cohort_id=cohort.id student_id=student.id%}"> Edit Student</a>
  <a href="{% url 'delete_student' cohort_id=cohort.id student_id=student.id %}">Delete Student</a>
</div>
```

```html
# student_form.html
<h2>{{ type_of_request }} Cohort</h2>
<form method="POST">{% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Save</button>
</form>
```

```html
# students_list.html
<h1> All Students for {{ cohort.cohort_name }} </h1>
<ul>
  {% for student in students %}
    <div>
      <li><a href="{% url 'student_detail' cohort_id=cohort.id student_id=student.id %}">{{ student.first_name }}</a></li>
    </div>
  {% endfor %}
</ul>

<a href="{% url 'new_student' cohort_id=cohort.id %}">Add a new student</a>
```

And just like that, we have nested CRUD! Visit your routes and see it work!

## Assignments
- Before doing anything, make sure that you run through this tutorial and understand what's going on
- [Cars and Brands](https://github.com/codeplatoon/django-cars-and-brands)
- [Beer Reviews](https://github.com/codeplatoon/django-beer-ratings)
