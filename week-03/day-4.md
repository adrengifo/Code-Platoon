Day 4
======================
### Video Resources (India Platoon)
- [Week 3 Videos](https://www.youtube.com/playlist?list=PLu0CiQ7bzwERYl9BQgqCObTzijFbd73Oe)

### Challenges
* [School Interface Three](https://github.com/codeplatoon/school-interface-three)
* [Bank Accounts](https://github.com/codeplatoon/bank-accounts)

### Lecture Topics
* Python Modules 
* Intro to SQL
  * [Slides](https://docs.google.com/a/natedelage.com/presentation/d/1834tfN6g9gvl2t0JDQY2RPMCIAnvN08Wrd-bO-usruQ/edit?usp=sharing)

### Python Modules
Using modules in Python allow for you as the author to organize your code and group it together for ease of use. To put it very simply, a module is a file of Python code that you bring into other files. Let's take a look at an example:
```python
# file1.py
def say_hello():
    print('Hey there')


# file2.py
import file1
import file1 as anything
anything.say_hello()
```
We just created two files: `file1.py` and `file2.py`. `file1.py` has a `say_hello` function. `file2.py` has nothing in it, but imports that file in as the name of the file and we can use all the methods in that file. We can also rewrite it as `import file1 as anything` and call `anything.say_hello()`. You can `import` anything into your file by providing the correct relative path to the file. More on that can be found [here](https://www.tutorialspoint.com/python/python_modules.htm)

### Homework
* Finish Bank Accounts
* Read [Functional vs. OOP](https://www.codenewbie.org/blogs/object-oriented-programming-vs-functional-programming)
