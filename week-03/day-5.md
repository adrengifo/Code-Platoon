Day 5
====================
### Video Resources (India Platoon)
- [Week 3 Videos](https://www.youtube.com/playlist?list=PLu0CiQ7bzwERYl9BQgqCObTzijFbd73Oe)

### Lecture Topics
* Big O Notation
  * [Slides](https://docs.google.com/presentation/d/1RNYAhAkNF3-UR9rzlBOaWJ0fyYundS0TAGXEYRv-Ybo/edit#slide=id.g22ef87eb09_0_23)
* More advanced Python collection methods

### Challenges
* [School Interface Four](https://github.com/codeplatoon/school-interface-four)
* [Big O Problems 1](https://github.com/codeplatoon/big-o)
* [Big O Problems 2](https://github.com/codeplatoon/big-o-2)

### Advanced Python Collection Methods
#### Lambda Functions
- Anonymous functions / one-liner functions that are written slightly differently from traditional functions but do the exact same thing
```python
def square_number(number):
    print(number ** 2)

# in lambda format
square_number = lambda number: number ** 2

def add_numbers(number_1, number_2):
    print(number_1 + number_2)

# in lambda format
add_numbers = lambda num1, num2: num1 + num2

# You can also pass in entire functions as arguments in a lambda
def my_function(some_function, num):
    return some_function(num)

my_function(lambda x: x + 2, 3) # in this case, the `some_function` parameter is `lambda x: x + 2`. The answer to this would be 5
```

#### Map
- This iterates over an array and does something to each of them
```python
# Let's start with creating a list between 0 and 9
map_list = [number for number in range(0, 10)] # or map_list = list(range(0,10))
print(map_list)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# If we wanted to cube everything, we could probably just do this to get started
cubed_list = []
for i in map_list:
    cubed_list.append(i**3)
print(cubed_list)
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# Another option below
[i**3 for i in mapList]
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# But we want to learn how to use `map` and `lambdas` together
cubed_list = list(map(lambda x: x**3, map_list))
# we set a variable called cubed_list equal to a new list created on the right side of the equals sign. `map` takes in two arguments: the function that you're going to run and the array you are going to iterate over. We will `map` over a collection (iterate over every single element of the array) and save it as `x`. From there, we'll raise that number `x` to the third power.
print(cubed_list)
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# Let's create a few functions below
def multiply_numbers_together(x):
    return x * x

def add_numbers_together(x):
    return x + x

def square_the_number(x):
    return x ** 2
    
def cube_the_number(x):
    return x ** 3

functions_to_apply = [multiply_numbers_together, add_numbers_together, square_the_number, cube_the_number]

for index in range(5): # iterate from 0 to 4, save `index` as that number
    value = list(map(lambda x: x(index), functions_to_apply))
    print(value)

# [0, 0, 0, 0] # index is 0
# [1, 2, 1, 1] # index is 1
# [4, 4, 4, 8] # index is 2
# [9, 6, 9, 27] # index is 3
# [16, 8, 16, 64] # index is 4
```

#### Filter
- Same thing as map, but instead of doing something over all of the elements of a list, you are only selecting (or `filter`-ing) the things that turn out to be true over the elements of the list
```python
filter_list = list(range(1, 51)) # create a list of numbers between 1-50
evenly_divisible_by_2 = list(filter(lambda number: number % 2 == 0, filter_list))
print(evenly_divisible_by_2)
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
```

### Weekend Homework
* Finish Assessment #2
* SQL Intro
  * [PG Exercises](https://pgexercises.com/)
  * [Read the Intro to Persistence](https://github.com/codeplatoon/self-paced-curriculum/blob/master/week-04/readings/persistence-intro.md)
