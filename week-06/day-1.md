Day 1
====================
### Video Resources (India Platoon)
- [Week 6 Videos](https://www.youtube.com/playlist?list=PLu0CiQ7bzwERd7yk9weQbUN5J7G11p0iv)

# Javascript
So far we've been using [node](https://en.wikipedia.org/wiki/Node.js) to run our javascript code in the terminal. This is a relatively new development for Javascript. Originally, it was created to run exclusively in the browser so that developers could add behavior to web pages. Since then it has become the primary language of the web. This week we'll be spending some time looking at how Javascript runs in the broswer, and how we can use it to make our web pages more dynamic. 

## The DOM
Before we can start using Javascript on our front end, we need to understand what the DOM is and how it works. When the browser recieves a webpage (HTML and CSS) it breaks it up into a tree like structure that is called the Document Object Model (DOM).

![The DOM](./images/DOM.png)

Each element in our HTML document is represented as a node in the DOM. We can use Javascript to access these nodes and manipulate them. Let's start with a simple HTML file. Create a file called `index.html` and paste the following code:

```HTML 
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>JS and The DOM</title>
</head>
<body>
  <div class='container' >
    <h1 id='heading'>Welcome to My Web Page</h1>
    <p id='article-1'>An interesting article goes here.</p>
  </div>
</body>
</html>
```
Open this file in Chrome. Then, right click anywhere on the page and select **Inspect** from the menu. This will open the Chrome Dev Tools. If you haven't used the Dev Tools before they can be a little overwhelming. It's important to get used to them, however, as they are an essential tool in a web developer's tool belt.  

<img src='./images/inspect.png' width='300px'>
<img src='./images/devtools.png' width='500px' style='padding-bottom:100px'>

We won't go over every single tab in the dev tools today, though eventually you should become familiar with all of them. Today we'll focus on the Elements tab and the Console tab. 

The Elements tab will show us the HTML structure of our web page. We can click the grey arrows next to an element to open it up and reveal its child elements. Open the `body` tag and then our container `div`. Hover your mouse over the `h1`. Notice how when we hover over an element it gets highlighted on the page. On the far right you can see the CSS that is being applied to the element. Since we haven't written any of our own styles, you'll see the ones the browser has set by default.

## Interacting with the DOM

Click over to the console tab and let's write some Javascript to interact with our page. We can access the entire DOM object with the variable `document`. Type `document` in your console and hit enter. You should get something that looks like our HTML doc. The browser parses it out for us and makes it easy to navigate, but you should get used to thinking of this like a giant Javascript object. It has attributes we can access and methods we can call on it. Most of the interacting we do with the DOM today will be through this `document` object. 

Let's use Javascript to change the color of our `h1`. First, we need to get the `h1` element. Then, we can access the `style` attribute and set the color. 

We can access elements by their tag (`'h1'`, `'div'`, etc.), class (`'.my-class-name'`), or id (`'#my-id-name'`). 

Enter the following code into the console. 

```Javascript
document.querySelector('#heading')
```
`querySelector()` will return the first element it finds. If you want all the elments for a query, say all the `span` tags or everything in a certian class, you can use `querySelectorAll()` which will return a collection. 

Once we have the element we are looking for, we can save it to a variable and access the style attribute. 
```Javascript
const heading = document.querySelector('#heading')
heading.style.color = 'red'
```

Add this code to the console and press enter. You should see the text in the `h1` change to red. 

## Events

The browser is always listening, always keeping track of user behavior. It can tell you when a user has clicked on something, when the mouse enters or leaves an element's bounds, the location of the mouse at any given time, and much more. We can tap into these events and use them to react to user behavior. We do that by calling a function called an [Event Listener](https://developer.mozilla.org/en-US/docs/Web/API/EventListener). 

Let's modify our code so that the color doesn't change until a user clicks on the `h1`. Refresh your browser and add the code below to the console and press enter. 

```javascript 
const heading = document.querySelector('#heading')

heading.addEventListener('click', function(event){
  this.style.color = 'red'
})
```
We call the `addEventListener()` function on our element and pass it two arguments. The first is the type of event we are listening for. (You can find a full list of events [here](https://developer.mozilla.org/en-US/docs/Web/API/EventListener)). The second argument is a function that we want to run when the event is triggered. This function will take one arguemnt of its own, an `event` object that holds some information about the event iteself. 

Now the color should only change after we click on the `h1`. 

## Loading JS in HTML 

The broswer console is a great place to test and try things out, but it's not really helpful when we want to write longer scripts. Make a new file `script.js` in the same directory as your `index.html` and copy this code into the file. 

We need to let our HTML file know that there is some Javascript that we want to load. 

```HTML
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>JS and The DOM</title>
</head>
<body>
  <div class='container' >
    <h1 id='heading'>Welcome to My Web Page</h1>
    <p id='article-1'>An interesting article goes here.</p>
  </div>
  <!-- We add any JS files we want to run at the bottom of our HTML file.  -->
  <script src='./script.js'></script>
</body>
</html>
```
```javascript
// script.js
const heading = document.querySelector('#heading')

heading.addEventListener('click', function(event){
  this.style.color = 'red'
})
```

We can load any number of Javascript files at the end of our HTML doc, just before the closing `body` tag. We need to put the tags at the bottom because the browser reads the HTML file top to bottom. If we had the `script` tag in the head our `const heading = document.querySelector('#heading')` line would run before the `h1` was actually created. This would cause an error. Putting our `script` tags at the bottom ensures that all the DOM elements load before our Javascript runs. 

Reload the page and click on the `h1`. We should have the same behavior as before. 

## AJAX with the Fetch API

AJAX is everywhere on the Internet and some would argue makes the user experience better for all. Whether or not you have noticed, you've probably used AJAX. Are you a Facebook user? Twitter? Youtube? You've used AJAX when you've scrolled to the bottom of the page only to find that there are more posts/tweets/videos (respectively) at the bottom. In many cases, there is the concept of infinite scroll that occurs to make your user experience better.

How about Google Maps? If you load up maps, you can zoom in and out of the page to see different businesses based on how far you've scrolled in and out. That certainly did not load up whenever you first loaded the page - based on user interaction with the website, AJAX requests are being made. Scroll over a business and see a street view photo and/or Google reviews - all AJAX!

If you Tweet and don't see your page refreshing, that's AJAX! Let's learn how to use it today. 

In the past we used a library called [JQuery](https://jquery.com/) to make AJAX calls. You may still see this in use in some legacy code. 

The more modern way, and the way we will learn today, is by using Javascript's [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) to make both GET and POST requests. 

The GET method should be used for non-destructive operations - operations where we are only getting data from the server, not changing it. For example, a search.

The POST method is used for destructive operations - operations where we are changing data on the server. For example, posting a comment.

### GETting Data with Fetch

Let's add a `div` with a class of `.response-data` to our HTML file. 

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>JS and The DOM</title>
</head>
<body>
  <div class='container' >
    <h1 id='heading'>Welcome to My Web Page</h1>
    <p id='article-1'>An interesting article goes here.</p>
  </div>
  <div class='response-data'></div>
  <!-- We add any JS files we want to run at the bottom of our HTML file.  -->
  <script src='./script.js'></script>
</body>
</html>
```
Next, let's modify `script.js` to use `fetch()` to make a GET request and return us some JSON data. We'll use the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) website. This site provides some endpoints that return placeholder data for testing fetch calls. 

```Javascript
// script.js
// first we grab our container so we can append our new data. 
const responseContainer = document.querySelector('.response-data')
// then we use fetch to make a GET request
fetch('https://jsonplaceholder.typicode.com/todos/1')
  .then(resp => resp.json())
  .then(json => {
    responseContainer.innerHTML = json.title
  }) 
```
Up to this point we are probably most comfortable with code that is synchronous, meaning it executes in order and the next line does not run until the previous line is complete. However, when we make HTTP requests, we can't always be sure how long the request will take to resolve (in some cases it may not resolve at all). Therefore, it makes more sense to write some asynchronous code ( code that does not have to wait). In the case of HTTP requests, we want to write a function to make the request, but still be able to run the rest of our code at the same time, so that we can still respond to user events, update the DOM, or even make other HTTP requests. 

To accomplish this asynchronous behavior `fetch()` uses a concept in Javascript called [Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise). A Promise is an object that sits inbetween a call and response. So when we make an HTTP requests, `fetch()` returns a promise. That promise object will eventually resolve the request (give us back some data) or return an error if the request fails or times out. That's where our `then()` functions come in. These functions take a promise and run after the promise is resolved. The code above works like this: 

- Make an HTTP GET request to https://jsonplaceholder.typicode.com/todos/1'
- This will return a promise 
- When the promise resolves the first `then()` function is called. 
- This function parses the data from JSON to a Javascript object. 
- The final `then()` takes the object and appends the `title` property to our container `div`. 

### POSTing Data

##### Forms

So far, we've learned how to **GET** data. Now, we will practice **POST** requests. We will submit this data online.
First, go to [PutsReq](http://putsreq.com/) and click 'Create a PutsReq.' This will create a little bucket for us
to send data to. Next, we need to alter the _response_ from the server so our `success` callback will fire (this is in the `PutsReq` you just made). Make sure to click **Update** after you add the code below. 

Response code:
```JavaScript
// add this code to putsreq
const msg = {data:'Hello World'};
const body = JSON.parse(request.body)
if(request.body) {
  msg['data'] = 'Hello ' + body['name'];
}

response.body = msg;
```

Great. now we can build a simple form in HTML and add some Javascript code to our `script.js` file:

```HTML
<form id="commentForm">
    <input type="text" id="comment" name="name">
    <button type="submit" id="submitComment">Submit Comment</button>
  </form>
  <div id="post-response">
  </div>
```

Read the following JavaScript code carefully. You'll need to copy the link to your putsreq bucket and add it to the code.

```JavaScript
// script.js
const form = document.querySelector('#commentForm')
const postResponseContainer = document.querySelector('#post-response')

form.addEventListener('submit', function(e){
  e.preventDefault()
  let comment = {name: e.target.elements[0].value }
  const endpoint = // paste the url for you putsreq bucket here. 

  fetch(endpoint, {
    method: 'POST', 
    headers : {
      "Content-Type": "application/json"
    }, 
    body: JSON.stringify(comment)
  }) 
  .then(response => response.json())
  .then(json => {
    postResponseContainer.innerHTML = json.data
  })
})
```
This code uses `querySelector()` to grab the form so we can get the data from it. We also grab the `div` with id `#post-response` so we can add the response to the DOM. Next, we add an event listener to our form. Instead of `click` we pass `submit`. This will fire our callback function as soon as the form is submitted. By default, a form will append the content to a url and make a request for us. We want to make the request ourselves. Calling `e.preventDefault()` will prevent the form from trying to submit the data itself. Next, we need to pull the data from the form `e.target.elements[0].value`, and put it inside of a Javascript object. 

When we use `fetch()` to make a `POST` request, we need to pass it some additional information. We do this by passing a Javascript object as a second argument. That object will define some settings for our request. From there we handle the respose the same way we did when we made a `GET` request, ultimately appending the data to our `post-response` div. 

## Challenges
* [Linkedin JS](https://github.com/codeplatoon/linkedin-js)
* [Browser Storage](https://github.com/codeplatoon/browser-storage)
* [Simple Todo](https://github.com/codeplatoon/simple-todo)
* All assignments up to this point that have not yet been completed

