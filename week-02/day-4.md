Day 4
======================
### Video Resources (India Platoon)
- [Week 2 Videos](https://www.youtube.com/playlist?list=PLu0CiQ7bzwEQT_GDPFAx7E7awUWCv5zMu)

### Lecture Topics
* Object-Oriented Programming vs. Functional Programming
* Python Libraries 
* Javascript Libraries
* Debugging (Python's `embed`)

## Object-Oriented Programming vs. Functional Programming
There are generally two programming paradigms that people follow: functional programming and object-oriented programming. However loud the proponents are on both sides of the aisle, there is not a clear "winner" - it depends largely on the scale of your project, the skill level of your developers, and what you're trying to accomplish with your code. Today, we're going to take a closer look into both types of coding and see when each one shines.

Functional programming has surged in popularity in recent years due to its increased speed compared to object-oriented programming. In FP, we avoid changing state, meaning that the functions/methods we write don't impact _anything_ outside the function. There aren't any instance variables and we don't change anything about any objects. It's simply X going in and Y coming out. An example:

```python
def add(number_1, number_2):
  print(number_1 + number_2)
```

In this example, I've got 2 numbers that I pass into the `add` method. The result is the sum of those numbers. This is what's known as a "pure" function - it always produces the same output from your input and has no side effects. I can just as easily rewrite this as the following and get the same result:

```python
def add(number_1, number_2):
  print(number_2 + number_1)
```

Most of the code we've been writing thus far with our algorithms have been functional in that we provide our functions with parameters and get back a result. We've not really been working objects, keeping track of state, etc. That being said, we're going to be mostly working in the object-oriented paradigm soon.

In object-oriented programming, we organize our code into reusable classes to create new `objects`. Each object is loaded into our computer's memory and each  object keeps track of its own state. For example:

```python
class Account:
  def __init__(self): 
    self.balance = 100

  def deposit(self, amount):
    self.balance += amount

account = Account()
account.balance # 100
account.deposit(50) #150
account.balance # 150 
```

In the above example, we have an Account object that keeps track of its own balance. Our function `deposit` takes in an argument and pushes out an output, but it also alters the state of the object's `balance`. Thus, it is an `impure` function and ultimately, object oriented code.

Objected oriented code is not evil and is far more popular to program with than functional programming. For most companies and for most projects, you'll want to organize your code into objects so that you can quickly reference/alter its attributes and call its methods to update things in your database.

## Python Libraries 
* For all languages, libraries, frameworks, and packages are just thousands of lines of code that someone else wrote ahead of time to make your life as a developer easier. There is no magic here - it's just meant to make your life easier and for you to make more robust applications
* There are a number of package managers to manage the different Python libraries we will use. The two most popular ones are Pip and Anaconda. Pip is more for web development where Anaconda is more for data science and analytics. The one you choose will largely depend on what you do more of
* You can find some very useful libraries [here](https://pythontips.com/2013/07/30/20-python-libraries-you-cant-live-without/). We'll be using Django in the next few weeks and definitely some of the more data science heavy libraries like NumPy and Pandas
* Please note that the majority of these libraries are backend libraries meaning that there's not a ton of frontend code to make it pretty

## Javascript Libraries
* [List of JS libraries](https://www.javascripting.com/)
* Javascript libraries are primarily front end heavy and make your website easier to use. The most popular library/framework used today is React and React Native. Instagram and Facebook are written in this framework.
* Take a look through [D3](https://d3js.org/), [Animate](https://daneden.github.io/animate.css/), and [ThreeJS](https://threejs.org/examples/)

## Debugging (Python's `embed`)
* Sometimes, you are running code and just want to pause in the middle of a loop and see what's going on around you. Up to this point, we haven't been able to do that, but with a Python library, we'll be able to stop our code at any point 
* First, we install IPython: `pip install ipython` and create our file we want to write out Python code in. Copy and paste the code below:
```python
from IPython import embed

def say_hello(first_name):
    embed()
    print(f"Hello there, {first_name}!")

say_hello('Jon')
```
* If you run `python filename.py`, you will see `In [1]: `. This is the `embed` portion of the `IPython` library stopping your code where you tell it to with `embed()`. At this point, you can view your variables, including `first_name`.
* The same can be done with loops:
```python
age = 12
while age < 21:
    embed()
    print(f"You are not old enough yet - you are only {age} years old! Come back when you are older.")
    age += 1
```
* The code above will run and stop when it hits `embed()`. You can see what `age` is. Ultimately, you want to use this when you hit issues and need help debugging your code.

### Challenges
* [Caesar Cipher](https://github.com/codeplatoon/caesar-cipher) in JS/Python
* [Pig Latin](https://github.com/codeplatoon/pig-latin) in JS/Python
* [Bubble Sort](https://github.com/codeplatoon/bubble-sort) in JS/python

### Homework
* Study up on object orientation
