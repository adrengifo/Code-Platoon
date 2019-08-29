Day 3
=====================
### Videos (India Platoon)
* [Playlist](https://www.youtube.com/playlist?list=PLu0CiQ7bzwETyxQsXFj_HYt9VyTViUnu8)

History of the Web
-------
- [Slides](https://docs.google.com/presentation/d/1rSbHEIkfM2nOwD3YoqxOh-SUVA-Pq4LCyctKO0T9QMA/edit?usp=sharing)

Object Orientation in Javascript
-----------
We've spent quite a bit of time on Python and all of last week on Django. We're going to shift gears and move towards Javascript. If you recall, we've mentioned that once you learn one language/framework well, it's easy to translate to another class. Let's go over that here with our `Person` class:

```javascript
class Person {
  constructor(name, hometown){
    this.name = name
    this.hometown = hometown
  }

  sayHello(){
    return `${this.name} from ${this.hometown}`
  }
}

const jon = new Person('jon', 'nj');
jon.sayHello(); 
```

Let's break this down a little bit. We've created a `Person` class with a `constructor` function. That `constructor` function operates similarly to Python's `def __init__` where you pass in certain parameters that the class will need to know about itself. In our case, we need two parameters/properties (aka `props` for React apps): `name` and `hometown`. The `this.name = name` basically creates an instance variable, similar to Python's `self.name = name`, meaning that we can use `this.name` everywhere inside that particular instance of the class.

The `sayHello` function basically just returns your name and hometown. With that, let's move onto React.

Create React App
----------------
Just like we have `django admin startapp` to create new Django applications, we have a generator, `create-react-app` from Facebook which configures everything together - take a look through the [documentation](https://github.com/facebookincubator/create-react-app) when you get a chance.

We've installed Node Package Manager (NPM) when we installed Node on the first day. NPX is an updated version of NPM that comes for free with NPM. Let's install a React app by running:

```sh
$ npx create-react-app my-app
$ cd my-app
$ npm start
```

This generator has generated a bunch of folders and files for us. Let's break each one down:

- The `node_modules` folder holds all of our dependencies locally so we're not relying on the web being up and running. This includes Babel, ESLint, Mocha/Chai, etc.
- The `public` folder has a bunch of public-facing assets like the favicon (top corner of the tab which is your company's logo)
- `src` has the main meat of all of our app, especially `index.js`. This file is loaded first and is the entrypoint for our React app:

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

ReactDOM.render(<App />, document.getElementById('root'));
serviceWorker.unregister();
```

The `import React` statement contains the the core React functionality. This includes the code related to markup like you see further down the file and turning that into UI code. `import ReactDom` takes your code and actually can render that out to the page/DOM/browser. We're also relatively importing `App`, which is the file `App.js` and we're calling it into our code.

Moving onto `App.js`: 

```javascript
import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
```

This is an example of a functional component. As of March 2019, the creators of React want to start migrating over to functional components instead of class-based components for ease of development. They have very clearly stated that both are going to exist alongside each other and you will definitely need to know both. New projects will utilize functional components and old projects (the majority of what you'll be doing in real life) will use class-based components. 

This `App.js` file is bringing in React from the `react` library, the React logo from `./logo.svg`, and a CSS file. The `return` function is an example of JSX, which you can think of as the same thing as Python's Jinja2. Jinja templates are HTML with Python inside. JSX is HTML ith Javascript in it. At the beginning of React, JSX files had the `.jsx` extension (you may still see this). They quickly realized that JSX was in every single file pretty much so they made every JS file have the JSX extention and took away the `.jsx` explicitive call and made all JS files end with the `.js` extension.

Our First React App
-------------------
Let's create an actual app in React that displays a button and how many times you've clicked that button. Sounds stupid? Well, tell that to the creators of [Cookie Clicker](http://orteil.dashnet.org/cookieclicker/). They cashed out and made it big. Let's start by getting `App.js` rewritten:

```javascript
import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App"> 
      <h1> I have been clicked X times </h1>
      <button> Click me! </button>
    </div>
  );
}

export default App;
```

Let's tackle keeping track of the number of times something has been clicked. Right now, we have a placeholder `X`. Instead, we want to use the React concept of `state`:

```javascript
import React, { useState } from 'react';
import './App.css';

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="App"> 
      <h1> I have been clicked { count } times </h1>
      <button> Click me! </button>
    </div>
  );
}

export default App;
```

Let's break it down:
- `useState` is a library from React that gives us the ability to...use state.
- `const [count, setCount] = useState(0);`
  - `useState` accepts one argument and returns two things: `count` and `setCount` `count` is set to `0` and `setCount` is a function that alters `count`.
- We use curly braces to interpolate JS into our HTML. Similiarly, we used `{% %}` and `{{ }}` for Python templates. We should now see that we've clicked it 0 times.

Next, we want to record all the times that we've actually clicked the button - how do we do this? First, we need an event handler for the button. When the button has been clicked, the event handler will update the `count`:

```javascript
import React, { useState } from 'react';
import './App.css';

function App() {
  const [count, setCount] = useState(0);

  const handleClick = () => {
    setCount(count+1)
  }

  return (
    <div className="App"> 
      <h1> I have been clicked { count } times </h1>
      <button onClick={handleClick}> Click me! </button>
    </div>
  );
}

export default App;
```

Right now, our button clicker works for one button. What if we want this button functionality to be a reusable component? Let's continue practicing Single Responsibility code and learn about class-based components instead of functional components. You'll need to know both.

First, let's copy all the code from `App.js` and put it in `src/components/ButtonComponent/ButtonComponent.js`:

```javascript
import React, { useState } from 'react';
import './App.css';

function App() {
  const [count, setCount] = useState(0);

  const handleClick = () => {
    setCount(count+1)
  }

  return (
    <div className="App"> 
      <h1> I have been clicked { count } times </h1>
      <button onClick={handleClick}> Click me! </button>
    </div>
  );
}

export default App;
```

Let's turn that code into a `ButtonComponent` class:

```javascript
import React, { Component } from 'react';

class ButtonComponent extends Component {
  state = {
    count: 0
  }

  handleButtonClick = () => {
    this.setState({
      count: this.state.count + 1
    })
  }

  render(){
    return (
      <div>
        <h1> I have been clicked { this.state.count } times </h1>
        <button onClick={ this.handleButtonClick }> Click me! </button>
      </div>
    )
  }
}

export default ButtonComponent;
```

This class-based code functions the same as the code in `App.js`. There are some new things to keep track of:
- We are bringing in the `Component` library from the `react` NPM package
- `ButtonComponent` inherits (i.e., `extends`) from `Component`
- `state` is a class level dictionary that keeps track of different values you need
- We create a custom event handler called `handleButtonClick`, which is a fat arrow function. Having `handleButtonClick` as a fat arrow function binds it to the `ButtonComponent` class. This allows us to overwrite the state on `ButtonComponent` by calling `setState`.
  - `setState` allows you to directly mutate the `state` dictionary
- `render` wraps around the `return` we had in `App.js`
- Instead of calling `count` directly in the `<h1>`, we're referencing `this.state.count` (i.e., ButtonComponent's state's count)
- We're incrementing the count using `this.handleButtonClick` (i.e., ButtonComponent's handleButtonClick method)


Import this new component into `App.js`:
import React from 'react';
import ButtonComponent from './components/ButtonComponent/ButtonComponent.js'
import './App.css';

function App() {
  return (
    <div className="App"> 
      <ButtonComponent />
    </div>
  );
}

export default App;
```javascript

```

You can reuse the `ButtonComponent` over and over again. Since they are separate/independent components, each one will keep track of its own state. To demonstrate this, we can spam the screen with a lot of `ButtonComponents`:

```javascript
import React from 'react';
import ButtonComponent from './components/ButtonComponent/ButtonComponent.js'
import './App.css';

function App() {
  return (
    <div className="App"> 
      <ButtonComponent />
      <ButtonComponent />
      <ButtonComponent />
      <ButtonComponent />
      <ButtonComponent />
      <ButtonComponent />
      <ButtonComponent />
      <ButtonComponent />
      <ButtonComponent />
      <ButtonComponent />
      <ButtonComponent />
    </div>
  );
}

export default App;
```

We have a ton of buttons! But that's not very programatic. Let's use JS to iterate over collections of components to put them out on the screen:

```javascript
import React from 'react';
import ButtonComponent from './components/ButtonComponent/ButtonComponent.js'
import './App.css';

function App() {
  const createButtons = () => {
    let buttons = []
    for (let index=0; index < 100; index++) {
      buttons.push(<ButtonComponent />);
    }
    return buttons
  }

  return (
    <div className="App"> 
      {createButtons()}
    </div>
  );
}

export default App;
```

Nice! 100 buttons that each maintain their own state! If you open the console, you will notice that there's a warning called that each element should have a `key` prop. When you are creating an array of lots of React Components, you'll need a `key` prop to differentiate each individual component. Simply add the key to the ButtonComponent: `buttons.push(<ButtonComponent key={index} />);`

Good luck on today's challenges!

Challenges
----------
* [Detention](https://github.com/codeplatoon/detention)
* [Palindrome](https://github.com/codeplatoon/palindrome)
* [State Abbreviator](https://github.com/codeplatoon/state-abbreviator)