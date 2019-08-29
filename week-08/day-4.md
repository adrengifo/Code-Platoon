Day 4
=====================
### Videos (India Platoon)
* [Playlist](https://www.youtube.com/playlist?list=PLu0CiQ7bzwETyxQsXFj_HYt9VyTViUnu8)

Basic React
--------
Let's walk through a challenge called [Mute Button](https://github.com/codeplatoon/mute-button) together. The main purpose of this app is to teach us about React `props`, `state`, and how to organize our code efficiently.

To summarize our `original_readme`, we are trying to toggle between two different images on the page based on a user's clicks. The images can be found in the `icons` folder.

After cloning our app down and `cd`-ing into that repo, we are going to make it a React app by running `create-react-app app` and dragging the contents of our `app` folder into our original `mute-button` folder. Please keep the `README` from `mute-button` instead of `app`.

Starting out, we're going to hop into our `App.js`. Let's start with a class-based component this time. We'll need to set our `state` to control whether that variable has been clicked or not:
```javascript
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  state = {
    isMuted: false // let's just set it to false to begin with
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>
    );
  }
}

export default App;
```

Next, we will create a function called `toggleMute` that we'll attach to an event handler `onClick` for the image:

```javascript
import React, { Component } from 'react';
import './App.css';

class App extends Component {
  state = {
    isMuted: false // let's just set it to false to begin with
  }

  toggleMute = () => {
    this.setState({
      isMuted: !this.state.isMuted // opposite of whatever it is currently set as
    })
  }

  render() {
    console.log(this.state) // what is state before it hits the onClick?
    return (
      <div className="App">
        <div onClick={this.toggleMute}>test</div>
      </div>
    );
  }
}

export default App;
```

Let's run this and see what happens in the console - you should see `state` changing every time you click the `test` text on the screen.

Now, let's create another component to handle the mute button. Similarly to Django, if you have a bunch of the same thing (i.e., models, migrations, templates, views), then we want to have them in their own separate folder. For us, we'll create a `components` folder under `src`. Each specific component will have its own folder, and inside that folder will be the component itself and the corresponding test file.

We're going to create `src/components/MuteButton/MuteButton.js` with the following code:

```javascript
import React, { Component } from 'react';

class MuteButton extends React.Component {
  render() {
    if (this.props.isMuted === true) {
      return (
        <div> ON </div> // just getting some text on the screen for now
      )
    }

    return (
      <div> OFF </div>
    )
  }
}

export default MuteButton;
```

From there, let's import our `MuteButton` component into `App.js` and also change the rendering code: `import MuteButton from './components/MuteButton/MuteButton'` and call it in the render:

```javascript
import React, { Component } from 'react';
import './App.css';
import MuteButton from './components/MuteButton/MuteButton'

class App extends Component {
  state = {
    isMuted: false // let's just set it to false to begin with
  }

  toggleMute = () => {
    this.setState({
      isMuted: !this.state.isMuted // opposite of whatever it is currently set as
    })
  }

  render() {
    console.log(this.state) // what is state before it hits the onClick?
    return (
      <div className="App">
        <MuteButton isMuted={this.state.isMuted} />
      </div>
    );
  }
}

export default App;
```

Great - we lost the click functionality! Fear not - we need to pass a callback to the `toggleMute` function so that when it's clicked it actually fires the event. That being said, event handlers cannot be directly attached to React components. We want to pass the entire function with the context of `App.js` down to `MuteButton`:

```javascript
// inside App.js
<MuteButton isMuted={this.state.isMuted} toggleMute={this.toggleMute}/>
```

`MuteButton.js` should read something like:
```javascript
import React, { Component } from 'react';

class MuteButton extends React.Component {
  render() {
    if (this.props.isMuted === true) {
      return (
        <div onClick={this.props.toggleMute}> ON </div>
      )
    }

    return (
      <div onClick={this.props.toggleMute}>  OFF </div>
    )
  }
}

export default MuteButton;
```

At this point, you should be able to toggle between `OFF` and `ON` quite easily. Our final step is to display the image instead of the text on the page. We first need to move the entire `icons` folder into `src` as that is where everything is compiled from. You can import images just like you would React components.

`MuteButton.js` should now look like this:

```javascript
import React, { Component } from 'react';
import OnIcon from '../../icons/on.svg'
import OffIcon from '../../icons/off.svg'

class MuteButton extends React.Component {
  render() {
    if (this.props.isMuted === true) {
      return (
        <div onClick={this.props.toggleMute}> <img src={OffIcon} alt='AudioOff' /> </div>
      )
    }

    return (
      <div onClick={this.props.toggleMute}> <img src={OnIcon} alt='AudioOn' /> </div>
    )
  }
}

export default MuteButton;
```

That's it! We can click the image it toggles between muted and not muted. 


# Destructuring
Let's clean this up a little bit. If we have a lot of props getting passed down, it gets ugly because we have to write `this.props` so many times. Because `this.props` is a javascript object, we can use a concept called [destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) to declare new variables like this:

```javascript
let myObject = {
  "city": "Chicago",
  "school": "Code Platoon",
  "numberOfStudents": 11,
  "somethingWeDontNeed": "lorem ipsum"
}

city // undefined for now
school // undefined for now
numberOfStudents // undefined for now
somethingWeDontNeed // undefined for now

const {city, school, numberOfStudents} = myObject
// Javascript will look inside of myObject to find keys that match up with the variables you've declared in curly braces and set them equal to them

city // "chicago"
school // "Code Platoon"
numberOfStudents // 11
somethingWeDontNeed // still undefined because we didn't list it in the const above, despite it being in myObject
```
Let's apply this syntax within our `render()` function:

```javascript
import React, { Component } from 'react';
import OnIcon from '../../icons/on.svg'
import OffIcon from '../../icons/off.svg'

class MuteButton extends React.Component {
  render() {
    const {isMuted, toggleMute} = this.props
    if (isMuted === true) {
      return (
        <div onClick={toggleMute}> <img src={OffIcon} alt='AudioOff' /> </div>
      )
    }

    return (
      <div onClick={toggleMute}> <img src={OnIcon} alt='AudioOn' /> </div>
    )
  }
}

export default MuteButton;
```
There, that's easier to read! You will eventually want to be able to write both class-based and functional components; for now, you can stick with one or do both if you like. Below is what the code would look like with purely functional components:

```javascript
// App.js
import React, { useState } from 'react';
import './App.css';
import MuteButton from './components/MuteButton/MuteButton'

function App() {
  const [isMuted, setIsMuted] = useState(false); // let's just set it to false to begin with

  const toggleMute = () => {
    setIsMuted(!isMuted)
  }

  console.log(isMuted) // what is state before it hits the onClick?
  return (
    <div className="App">
      <MuteButton isMuted={isMuted} toggleMute={toggleMute}/>
    </div>
  );

}

export default App;
```

```javascript
// MuteButton.js
import React from 'react';
import OnIcon from '../../icons/on.svg'
import OffIcon from '../../icons/off.svg'

function MuteButton(props) {
  const {isMuted, toggleMute} = props
  if (isMuted === true) {
    return (
        <div onClick={toggleMute}> <img src={OffIcon} alt='AudioOff' /> </div>
      )
    }
    
    return (
      <div onClick={toggleMute}> <img src={OnIcon} alt='AudioOn' /> </div>
  )
}

export default MuteButton;
```

Challenges
----------
* [Whack-A-Mole](https://github.com/codeplatoon/whack-a-mole)
* [Mad Lib](https://github.com/codeplatoon/mad-lib)
* [Hangman](https://github.com/codeplatoon/hangman)
