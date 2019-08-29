Day 1
====================
### Video Resources (India Platoon)
- [Week 3 Videos](https://www.youtube.com/playlist?list=PLu0CiQ7bzwERYl9BQgqCObTzijFbd73Oe)

### Challenges
* [Apple Trees](https://github.com/codeplatoon/apple-trees)
* [Ice Cream and Freezers](https://github.com/codeplatoon/ice-cream-and-freezers)

### Lecture Topics
* Python Variables
* Instantiating objects with hashes

| Type             | Begins With        | Scope                                    |
|:----------------:|:------------------:|------------------------------------------|
|Local variable    | **a-z** *or* **_** | Available only within the immediate scope.
|Instance variable | **self.variable_name**              | Available to a specific instance of a class
|Class variable    | **a-z** *or* *_*             | Available anywhere in a specific class (including all instances)
|Global          | **global variable_name**       | Available everywhere, avoid!
|Constant          | **ALL_CAPS**       | Available in the scope of their definition


### Local Variable
- Local variables start with a lowercase letter or an underscore. Underscores are used to declare that a variable is available, but you are not using it
- Local variables are only available within the block of its initialization
- Local variables will raise an error if they are read before they're created
- Local variables are used the most often

```python
my_name = "<3 Jon!"
print(my_name) # <3 Jon!

def print_name(my_name):
  print(my_name)

print_name('Not Jon') # Not Jon
```
- You can also assign multiple variables at once. Simply separate them with commas. For example:

```python
a, b, c = 1, 2, 'John'
print(a) # 1
print(b) # 2
print(c) # John
```

### Instance Variables
- Instance variables begin with `self`
- Instance variables are available to the object of it's initialization
- Instance variables are also used very commonly

```python
class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = f"{first_name}.{last_name}@email.com".lower()
    
    def say_hello(self):
        print(f"My name is {self.first_name} {self.last_name}. I get paid ${self.pay} and my email address is {self.email}.")

e = Employee('Jon', 'Young', 50000)
e.say_hello()
```

### Class variables
- Class variables look the same as local variables but are declared at the top of a class
- Class variables are available to every instance of the class, not just a specific instance like an instance variable
- These have very specific use case so please use sparingly

```python
class Employee:
    number_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = f"{first_name}.{last_name}@email.com".lower()
        Employee.number_of_employees += 1 # This line will increase the class variable "number_of_employees" across all instances of the Employee class. Note that you are calling it on the Employee class (capital E)
    
    def say_hello(self):
        print(f"My name is {self.first_name} {self.last_name}. I get paid ${self.pay} and my email address is {self.email}.")

e1 = Employee('Jon', 'Young', 50000)
print(f"E1 Number of employees: {e1.number_of_employees}")

e2 = Employee('Josh', 'Alletto', 70000)
print(f"E2 Number of employees: {e2.number_of_employees}")
print(f"E1 Number of employees: {e1.number_of_employees}")

e3 = Employee('Rod', 'Levy', 90000)
print(f"E3 Number of employees: {e3.number_of_employees}")
print(f"E2 Number of employees: {e2.number_of_employees}")
print(f"E1 Number of employees: {e1.number_of_employees}")

```

### Global Variables
- Global variables take variables that are available within the global scope and bring them into function bodies by calling `global`, followed by the variable name
- You generally want to avoid using global variables because there's not many cases where you would want to have something available globally, but know that this is an option

```python
number = 101
print(number)

def some_function():
  global number
  print(number)

some_function()
```

### Instantiating objects with hashes
* A `Hash` is a great way to pass in arguments to the `init` method of a `Class`. Have a look at this Class:

```python
class Address:
    def __init__(self, first_name, last_name, street_one, street_two, city, state, country, postal_code):
        self.first_name  = first_name
        self.last_name   = last_name
        self.street_one  = street_one
        self.street_two  = street_two
        self.city        = city
        self.state       = state
        self.country     = country
        self.postal_code = postal_code
    
    def print_address_well(self):
        print(f"""
          {self.first_name} {self.last_name}
          {self.street_one}
          {self.street_two
          {self.city}, {self.state} {self.postal_code}
          {self.country}
        """)
        

address = Address("Jeremy", "Flores", "123 Fake St.", "Apt Yes", "Seattle", "WA", "USA", "98115")
address.print_address_well()
```

Let's ponder a few questions:
1. What if you mix up `street_one` and `street_two`?
2. What happens if you don't have a `street_two` attribute?
3. What if you mix up `city`, `state`, or `postal_code`?
4. What happens if you don't pass in the correct order of arguments every single time?

Let's try this again. This time, let's initialize using a `Hash`:

```python
class Address:
    def __init__(self, address_information):
        self.first_name  = address_information['first_name']
        self.last_name   = address_information['last_name']
        self.street_one  = address_information['street_one']
        self.street_two  = address_information['street_two']
        self.city        = address_information['city']
        self.state       = address_information['state']
        self.country     = address_information['country']
        self.postal_code = address_information['postal_code']
    
    def print_address_well(self):
        print(f"""
          {self.first_name} {self.last_name}
          {self.street_one}
          {self.street_two}
          {self.city}, {self.state} {self.postal_code}
          {self.country}
        """)
        
address_info = {
  'first_name': 'Jeremy',
  'last_name': 'Flores',
  'street_one': '123 Fake St.',
  'street_two': 'Apt Yes',
  'city': 'Seattle',
  'state': 'WA',
  'country': 'USA',
  'postal_code': '98115'
}

address = Address(address_info)
address.print_address_well()
```

Using a hash to provide parameters to an `initialize` method lets us omit parameters that may not exist for some instances. It also adds clarity to `class` instantiation by explicitely stating keys and values.

### Homework
* [Read this great article on CSV and python](https://www.pythonforbeginners.com/csv/using-the-csv-module-in-python) - Please note that they are using an older version of Python but it should overall be a good resource.
* Finish all problems from today
