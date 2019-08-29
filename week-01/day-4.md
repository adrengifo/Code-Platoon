Day 4
======================
### Video Resources
- [Week 1 Videos](https://www.youtube.com/playlist?list=PLu0CiQ7bzwEQbhg6rzm8h41r4c08KNij0)

## Test-Driven Development
Test-driven development (TDD) is the process of writing tests before you write any code. It's an important part of Agile software development and leads to better software for a number of reasons. The two that are most prominent:
1. As a developer, you are forced to think through what your program is supposed to do before you start writing code. It guarantees that whatever you write does what you want and accounts for edge cases.
2. It ensures that the code that you write integrates well into your overall program so that it doesn't break everything.

Each language has its own testing framework. As developers, you'll be required to primarily write Unit Tests. Unit Tests are pieces of software that call methods/functions you write and see if they work as you expect. When you write a method, you want to test it to ensure that it does what you expect. You are essentially testing a single **unit** of code in isolation and making sure it gives you what you want. Python ships with [Unit Test](https://docs.python.org/3/library/unittest.html) built into the library. We'll use that today to test and write code.

## Testing with Fizzbuzz
**_Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”._**

Before we begin writing code, we want to write tests. To get started, let's create a file called `fizzbuzz_spec.py` and put this code in there:

```python
import unittest
from fizzbuzz import fizzbuzz

class FizzbuzzTestCase(unittest.TestCase):
    """Tests for `fizzbuzz.py`."""

    # Your tests will go here

if __name__ == '__main__':
    unittest.main()
```

What do we know about our method and our desired output? We know that it:
1. Should return a list
2. Should return a list of 100 elements
3. The elements in the list should look like:
  [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "Fizzbuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "Fizzbuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "Fizzbuzz", 46, 47, "Fizz", 49, "Buzz", "Fizz", 52, 53, "Fizz", "Buzz", 56, "Fizz", 58, 59, "Fizzbuzz", 61, 62, "Fizz", 64, "Buzz", "Fizz", 67, 68, "Fizz", "Buzz", 71, "Fizz", 73, 74, "Fizzbuzz", 76, 77, "Fizz", 79, "Buzz","Fizz", 82, 83, "Fizz", "Buzz", 86, "Fizz", 88, 89, "Fizzbuzz", 91, 92, "Fizz", 94, "Buzz", "Fizz", 97, 98, "Fizz", "Buzz"]

With those 3 things, we can begin to write our tests. Let's start with our first requirement: `fizzbuzz()` should return a list.

```python
import unittest # imports the Unit Test library
from fizzbuzz import fizzbuzz  # import the fizzbuzz method from fizzbuzz.py

class FizzbuzzTestCase(unittest.TestCase):
    """Tests for `fizzbuzz.py`."""

    def test_returns_an_array(self):
        """When you call fizzbuzz(), you should get an array back"""
        self.assertEqual(type(fizzbuzz()), list)

if __name__ == '__main__':
    unittest.main()
```

Each test you write should be its own method with a descriptive message on what that method does. In our case, our method is appropriately named `test_returns_an_array` and the descriptive message is `When you call fizzbuzz(), you should get an array back`. Finally, we've got the meat of the method: `self.assertEqual(type(fizzbuzz()), list)`. 

The `assertEqual` is one of many assertion statements that the Python Unit Test library gives you. You can find more [here](https://docs.python.org/3/library/unittest.html#assert-methods). Most of these assertion statements are as obvious as their name implies - you are comparing that when you do A, you get B. In our case, we expect when we call `type(fizzbuzz())`, we get a list back. Hence, `self.assertEqual(type(fizzbuzz()), list)`.

If you were to run the spec file (`python fizzbuzz_spec.py`), you'd see that you get an error because we haven't writen the `fizzbuzz.py` file / any code yet. That's to be expected. We want to write tests first and code second.

Next, let's ensure that the list we actually get back returns 100 items. Let's tackle that together:

```python
import unittest # imports the Unit Test library
from fizzbuzz import fizzbuzz  # import the fizzbuzz method from fizzbuzz.py

class FizzbuzzTestCase(unittest.TestCase):
    """Tests for `fizzbuzz.py`."""

    def test_returns_an_array(self):
        """When you call fizzbuzz(), you should get an array back"""
        self.assertEqual(type(fizzbuzz()), list)

    def test_returns_an_array_of_100_items(self):
        """When you call fizzbuzz(), you should get 100 items back"""
        self.assertEqual(len(fizzbuzz()), 100)

if __name__ == '__main__':
    unittest.main()
```

Pretty simple. Let's go to the final test: ensuring that the list we get back have the correct elements at the correct indexes:

```python
import unittest # imports the Unit Test library
from fizzbuzz import fizzbuzz  # import the fizzbuzz method from fizzbuzz.py

class FizzbuzzTestCase(unittest.TestCase):
    """Tests for `fizzbuzz.py`."""

    def test_returns_an_array(self):
        """When you call fizzbuzz(), you should get an array back"""
        self.assertEqual(type(fizzbuzz()), list)

    def test_returns_an_array_of_100_items(self):
        """When you call fizzbuzz(), you should get 100 items back"""
        self.assertEqual(len(fizzbuzz()), 100)

    def test_returns_the_correct_array(self):
        """When you call fizzbuzz(), you should get the correct things back"""
        self.assertEqual(fizzbuzz(), [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "Fizzbuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "Fizzbuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "Fizzbuzz", 46, 47, "Fizz", 49, "Buzz", "Fizz", 52, 53, "Fizz", "Buzz", 56, "Fizz", 58, 59, "Fizzbuzz", 61, 62, "Fizz", 64, "Buzz", "Fizz", 67, 68, "Fizz", "Buzz", 71, "Fizz", 73, 74, "Fizzbuzz", 76, 77, "Fizz", 79, "Buzz","Fizz", 82, 83, "Fizz", "Buzz", 86, "Fizz", 88, 89, "Fizzbuzz", 91, 92, "Fizz", 94, "Buzz", "Fizz", 97, 98, "Fizz", "Buzz"])

if __name__ == '__main__':
    unittest.main()
```

Now that we've got the spec file finished, we can finally write our code! On your own, write your fizzbuzz method in `fizzbuzz.py` and see if it passes your tests.

### Other Lecture Topics
* [Python Fundamentals](https://github.com/codeplatoon/self-paced-curriculum/blob/master/week-01/lecture-materials/python_fundamentals.md)
* [JS Fundamentals](https://github.com/codeplatoon/self-paced-curriculum/blob/master/week-01/lecture-materials/javascript_control_flow.pdf) - control flow, if/else, loops, etc

### Challenges
We want you to solve today's challenges in Javascript and in Python. For the Python challenges, we want you to use test-driven development (TDD) in the testing framework we taught you today. Though spec files are included with `driver code` (code to help you `drive` your development), they aren't as robust as unit tests. For Javascript, we want you to use [JEST](https://jestjs.io/docs/en/getting-started.html) as it will translate into React testing later well.

* [Armstrong Numbers](https://github.com/codeplatoon/armstrong) in JS/Python
* [Sum Pairs](https://github.com/codeplatoon/sum-pairs) in JS/Python
* [Credit Check](https://github.com/codeplatoon/credit-check) in JS/Python
* [Anagrams](https://github.com/codeplatoon/anagrams) in JS and Python

### Additional Resources
* [Quick TDD Article](https://quickleft.com/blog/use-test-driven-development-tdd/)
* [TDD vs. BDD Part 1](https://www.toptal.com/freelance/your-boss-won-t-appreciate-tdd-try-bdd)
* [TDD vs. BDD Part 2](http://joshldavis.com/2013/05/27/difference-between-tdd-and-bdd/)


