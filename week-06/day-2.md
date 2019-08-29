Day 2
=====================
### Video Resources (India Platoon)
- [Week 6 Videos](https://www.youtube.com/playlist?list=PLu0CiQ7bzwERd7yk9weQbUN5J7G11p0iv)

# Bootstrap 

As web sites become more complicated, so does the task of handling styles and layout. Enter front-end frameworks. A front-end framework is just a set a pre-defined styles and Javascript functions that help us keep styles consistent and responsive. Some popular frame-works are Google's [Materialize](https://materializecss.com/), [Foundation](https://foundation.zurb.com/), and the one we'll explore today, Twitter's [Bootstrap](https://getbootstrap.com/). It's important to note that, though frameworks can seem like magic, they are just using regular CSS and JS under the hood. We can apply these pre-written styles by adding special classes to our HTML elements. 

## Installing 

You can [install bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/) with npm (we'll do that when we get to react), but for now, we'll use something called a CDN to load Bootstrap into our `index.html` file. This just means that we provide a link to our HTML page so that it can load the Bootstrap library directly from the Twitter Bootstrap servers when it loads. 

```HTML
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>Bootstrap</title>
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>
```

From here, we'll build out a generic home page to get a sense of how Bootstrap works. 

## Navbar 

Let's start by using Bootstrap to create a [navbar](https://getbootstrap.com/docs/4.0/components/navbar/) for our webpage. Add the following code to `index.html`. 

```HTML
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Dropdown
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <a class="dropdown-item" href="#">Action</a>
          <a class="dropdown-item" href="#">Another action</a>
          <div class="dropdown-divider"></div>
          <a class="dropdown-item" href="#">Something else here</a>
        </div>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#">Disabled</a>
      </li>
    </ul>
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
  </div>
</nav>
```
There's a lot going on here. Our main parent component, `nav` holds all the HTML that makes up our navigation for the site. The important thing to note here are all the classes being applied to our different elements. Open this file in your browser to see a fully styled and positioned nav bar. We haven't written a single line of CSS yet. Instead, we tap into classes already defined by Bootstrap. 

The other great thing about Bootstrap is that it is responsize. Resize your window and you'll see that at a certain point the navbar items will dissapear and you'll have a new button appear in the upper right hand corner. Clicking it will create a drop down menu for all of our nav items. 

Let's add a few more Bootstrap elements to our HTML page. 

[Jumbotron](https://getbootstrap.com/docs/4.0/components/jumbotron/) elements can be set to a specific size or, in our case, be set to fluid so that they take up the entire window. 

```HTML
<div class="jumbotron jumbotron-fluid">
  <div class="container">
    <h1 class="display-1">Welcome</h1>
      <p class="lead">This is a modified jumbotron that occupies the entire horizontal space of its parent.</p>
  </div>
</div> 
```


[Cards]() are nice for things like articles, videos or other contained data. (Though you can use them any way you like!) Let's add three in a row. 

```HTML
<div class="card col-sm" style="width: 18rem;">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <h6 class="card-subtitle mb-2 text-muted">Card subtitle</h6>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <a href="#" class="card-link">Card link</a>
    <a href="#" class="card-link">Another link</a>
  </div>
</div>

<div class="card col-sm" style="width: 18rem;">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <h6 class="card-subtitle mb-2 text-muted">Card subtitle</h6>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <a href="#" class="card-link">Card link</a>
    <a href="#" class="card-link">Another link</a>
  </div>
</div>

<div class="card col-sm" style="width: 18rem;">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <h6 class="card-subtitle mb-2 text-muted">Card subtitle</h6>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <a href="#" class="card-link">Card link</a>
    <a href="#" class="card-link">Another link</a>
  </div>
</div>
```

Each card is styled so that the content is evenly spaced, but they are all stacked one on top of the other. It would be better if we could get them side by side. Luckily, Bootstrap comes with its own way to handle layouts that is very similar to CSS Grid. First, we need to wrap our cards in a container div. Then, we add another `div` with class `row`. (If we wanted coloumns we could add more `div`s with class `col`) This will ensure that all our cards show up side by side. 

```HTML
<div class='container'>
  <div class='row'>
  <!-- our card divs go inside  -->
  </div>
</div>
```
Bootstrap can do a lot more than what we've looked at today. Like anything else, it may take a bit of research / practice, but once you get the hang of it, it will make your life a whole lot easier. 

## Custom Styles 

We can combine our own styles with the ones that Bootstrap gives us. Create a new file `styles.css` in the same directory as `index.html`. Then, import the file in the head. Make sure you import it **after** you import Bootstrap. Then, let's remove `navbar-light bg-light` from our `nav` element. These classes were adding some color to our navbar, but we want to add our own. Next, copy the following code into `styles.css`. 

```CSS 
.navbar {
  background-color: blue 
}
```
As long as we import our own styles **after** Bootstrap's, we can override add or override any of Bootstraps defaults. 
Most modern sites use a combination of Bootstrap (or some other framework) and their own styles. 

## Challenges
* [HTTP Server Three](https://github.com/codeplatoon/http-server-three)
* [Styling With Bootstrap](https://github.com/codeplatoon/bootstrap/blob/master/readme.md)

## Resources
* [Slides](https://docs.google.com/presentation/d/18XgB39IqvBFXfJYKQdc5j2ZzlZBeOH_enugni6b__Cs/edit?usp=sharing)

