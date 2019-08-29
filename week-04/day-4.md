Day 4
======================
### Video Resources (India Platoon)
- [Week 4 Videos](https://www.youtube.com/playlist?list=PLu0CiQ7bzwERcfp8HWFYBFLUdP5gP0lRM)

# Postgres and Python
We have spent the past 3 days learning about SQL and have used the Postgres flavor in our challenges. We've learned how to create/read/update/destroy databases/database columns/database rows. This is the foundation of all programming. It doesn't matter if you're doing development on the frontend, backend, server, mobile, desktop, etc., everything comes down to data persistence. A solid understanding of SQL will pay off huge dividends over the course of your career, so go back and ensure that you understand as much as you can!

We will often use SQL within the context of other programming languages and today, we are going to connect Python and Postgres together. The Python library that allows us to connect to our database is called [Psycop](http://initd.org/psycopg/). We're going to write Python code that can execute SQL commands. Let's test this out.

Let's create a database that holds the records of everyone in our class and connect to it using Python. Let's create a folder to mess around in called `psycop-example/` and within there, create `psycop-example/class_roster.py`. We first need to install `psycop` by running:

```sh
$ pip install psycopg2
```

Next, let's create the database that we are going to connect to:

```sh
$ createdb class_roster
```

Inside `class_roster.py`, let's import the Python library and start executing SQL commands:

```python
import psycopg2
import os

# Let's connect to our database
connection = psycopg2.connect(f"dbname=class_roster user={os.getlogin()}")

# Once a connection has been opened, we are going to open a cursor to run our SQL queries
cursor = connection.cursor()

# Let's create a query to create a students table and execute it
student_table_creation_query = "CREATE TABLE students (id serial PRIMARY KEY, name varchar, favorite_food varchar);"
cursor.execute(student_table_creation_query)
connection.commit()
connection.close()
```

Let's execute this by running:
```sh
$ python class_roster.py
$ psql class_roster

psql (11.1)
Type "help" for help.

class_roster=# \d students
```
You should see your students table with the columns you created. Continuing on, let's try to add a few records and query the database in `class_roster.py`:

```python
import psycopg2
import os

# Let's connect to our database
connection = psycopg2.connect(f"dbname=class_roster user={os.getlogin()}")

# Once a connection has been opened, we are going to open a cursor to run our SQL queries
cursor = connection.cursor()

# Let's create a query to create a students table and execute it. Note that we want to pass in values as %s rather than formatted strings to get away from SQL injection
student_table_creation_query = "CREATE TABLE students (id serial PRIMARY KEY, name varchar, favorite_food varchar);"
cursor.execute(student_table_creation_query)
cursor.execute("INSERT INTO students (name, favorite_food) VALUES (%s, %s)", ('Jon', "Sushi"))
cursor.execute("INSERT INTO students (name, favorite_food) VALUES (%s, %s)", ('Josh', "Hipster Food"))

# This is how we'd query the database for the two students I created. Since nothing is going to get printed out, we've commented it out:
# cursor.execute("SELECT * FROM students;")

# Commit these changes to the database
connection.commit()

# Close communication with the database
cursor.close()
connection.close()
```
Query the database for these records and see that they're in there. Once you're ready, let's move onto something more challenging.

## CSV and Databases
Whether you love or hate it, CSV will be around forever. Business people all love Excel and as we've seen, CSV is nothing more than Excel without fanciness. Oftentimes, you'll have to work with CSV and databases together. Let's grab real estate transactions from City of Sacramento and put that information into a database. Click [here](lecture_materials/sacramento_re_transactions.csv) to get the dataset.

Let's create a database, read the CSV file, clean some data, and insert the rows into the database together.

First, let's create a database:
```sh
$ createdb sacramento_real_estate
```
Next, let's create a file called `csv_example.py` and read into the CSV file and clean it up:
```python
import csv
import psycopg2
from IPython import embed

with open('lecture_materials/sacramento_re_transactions.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        embed()
```

Now, if we run `python csv_example.py`, we stop where `embed()` is called. If we enter `row`, we get an OrderedDict that we can access like a dictionary:
```
In [3]: row
Out[3]: 
OrderedDict([('street', '3526 HIGH ST'),
             ('city', 'SACRAMENTO'),
             ('zip', '95838'),
             ('state', 'CA'),
             ('beds', '2'),
             ('baths', '1'),
             ('sq__ft', '836'),
             ('type', 'Residential'),
             ('sale_date', 'Wed May 21 00:00:00 EDT 2008'),
             ('price', '59222'),
             ('latitude', '38.631913'),
             ('longitude', '-121.434879')])

In [4]: row['state']                                                     
Out[4]: 'CA'
```

Notice that CSV reads everything in as a string. That's problematic for us if we want SQL to do any calculations. It applies to most fields. Let's clean it together and then save it into the database:

```python
import csv
import psycopg2
import os

from IPython import embed
from decimal import Decimal
from datetime import datetime

def table_creation_query():
    return "CREATE TABLE properties (id serial PRIMARY KEY, street_address varchar, city varchar, zip_code varchar, state varchar, number_of_beds integer, number_of_baths integer, square_feet integer, property_type varchar, sale_date timestamp, sale_price integer, latitude decimal, longitude decimal);"

def clean_data(csv_row):
    cleaned = {}
    cleaned['street_address'] = csv_row['street']
    cleaned['city'] = csv_row['city']
    cleaned['zip_code'] = csv_row['zip']
    cleaned['state'] = csv_row['state']
    cleaned['number_of_beds'] = int(csv_row['beds'])
    cleaned['number_of_baths'] = int(csv_row['baths'])
    cleaned['square_feet'] = int(csv_row['sq__ft'])
    cleaned['property_type'] = csv_row['type']
    cleaned['sale_date'] = datetime.strptime(csv_row['sale_date'], '%m/%d/%y')
    cleaned['sale_price'] = csv_row['price']
    cleaned['latitude'] = Decimal(csv_row['latitude'])
    cleaned['longitude'] = Decimal(csv_row['longitude'])
    return cleaned

connection = psycopg2.connect(f"dbname=sacramento_real_estate user={os.getlogin()}")
cursor = connection.cursor()
cursor.execute(table_creation_query())

with open('lecture_materials/sacramento_re_transactions.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        cleaned_data = clean_data(row)
        cursor.execute("INSERT INTO properties (street_address, city, zip_code, state, number_of_beds, number_of_baths, square_feet, property_type, sale_date, sale_price, latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (cleaned_data['street_address'], cleaned_data['city'], cleaned_data['zip_code'], cleaned_data['state'], cleaned_data['number_of_beds'], cleaned_data['number_of_baths'], cleaned_data['square_feet'], cleaned_data['property_type'], cleaned_data['sale_date'], cleaned_data['sale_price'], cleaned_data['latitude'], cleaned_data['longitude']))

connection.commit()
connection.close()
```

With this data out of the CSV and in the database, you can query it and get some great insights into it. You can answer questions like:
- Are single family homes or condos more expensive on average?
- What's the most expensive house and condo sold? What's the cost per square foot?
- How much does each bedroom cost for a house in Sacramento? What if you wanted to get one more bedroom? What if you wanted one fewer?
- Same as above, but for bathrooms

Create queries in SQL and execute them to get a Python object back. Using those results and your knowledge of Python, answer the questions above.

### Resources/Challenges
* [Official Documentation](http://initd.org/psycopg/docs/usage.html)
* [Chicago Salaries](https://github.com/codeplatoon/city-of-chicago)