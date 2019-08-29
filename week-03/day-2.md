Day 2
=====================
### Video Resources (India Platoon)
- [Week 3 Videos](https://www.youtube.com/playlist?list=PLu0CiQ7bzwERYl9BQgqCObTzijFbd73Oe)

### Challenges
* [Word Guess CSV](https://github.com/codeplatoon/word-guess)
* [School Interface One](https://github.com/codeplatoon/school-interface-one)
* [Bowling](https://github.com/codeplatoon/bowling)

### What is a Database?
A _database_ is a system of storing and organizing information on a computer. We `query` the database using `SQL` (to be covered next week). In preparation for next week, we will be reading/writing to a _CSV_ file. In most cases a database can be thought of as a table or group of tables:

| ID | Team     | Wins  | Losses   |
|:---|:-------- |:------|:---------|
| 1  | Patriots | 10    | 2        |
| 2  | Bears    | 2     | 10       |
| 3  | Jets     | 5     | 5        |


### Reading from a CSV
Let's say that we have a `nfl_teams.csv` file with the following data:
```
id,team,wins,losses
1,Patriots,10,2
2,Bears,2,10
3,Jets,5,5
```

We're going to use Python's built in CSV library to read that information below. Check the [Python Docs](https://docs.python.org/3/library/csv.html) to figure out what's going on - if that's too much heavy reading, [this](https://realpython.com/python-csv/) is also a great resource.

```python
import csv
with open('nfl_teams.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
```

You should get an output of:
```
['id', 'team', 'wins', 'losses']
['1', 'Patriots', '10', '2']
['2', 'Bears', '2', '10']
['3', 'Jets', '5', '5']
```

A few things to note here: we have access to every row from the CSV file and every row is returned as an array of elements. If we wanted to read it back as a `dictionary` (technically, an ordered dictionary), we'd alter the code above as:

```python
import csv

with open('nfl_teams.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row)
```

Your output should look like:

```
OrderedDict([('id', '1'), ('team', 'Patriots'), ('wins', '10'), ('losses', '2')])
OrderedDict([('id', '2'), ('team', 'Bears'), ('wins', '2'), ('losses', '10')])
OrderedDict([('id', '3'), ('team', 'Jets'), ('wins', '5'), ('losses', '5')])
```

Here, we get back `OrderedDict` objects and we can access the values based off of the keys (i.e., `row['id']`, `row['losses']`). Since dictionaries inherently do not keep track of order, we need the `OrderedDict` object to keep track of order for us.

### Modes in CSV classes
You may have seen that in the previous example, we had a `mode` that we set equal to `r`. What is that cryptic code?

|Mode |  Meaning
|:---:|-----------------------------------------------------------|
|"r"  |  Read-only, starts at beginning of file  (default mode)   |
|"r+" |  Read-write, starts at beginning of file.                 |
|"w"  |  Write-only, truncates existing file to zero length       |
|"w+" |  Read-write, truncates existing file to zero length.      |
|"a"  |  Append write-only, starts at end of file if file exists. |
|"a+" |  Append read-write, starts at end of file if file exists. |
|"b"  |  Binary file mode                                         |
|"t"  |  Text file mode                                           |
### Writing to a CSV
Using that same NFL dataset above, let's write some data to the CSV file. Take a look at the code below:

```python
import csv

with open('nfl_teams.csv', mode='w') as nfl_file:
    nfl_writer = csv.writer(nfl_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    nfl_writer.writerow([])
    nfl_writer.writerow([4,'Giants',6,4])
    nfl_writer.writerow([5,'Lions',8,2])
```

Uh oh! We overwrote everything! Remember that the `w` mode overwrites everything. If we wanted to append to the end, we have to change the mode to `a`. Let's undo that change and try again. Did it append correctly?

You can also write to a CSV using a dictionary instead of an array, which I recommend as it's more precise:

```python
import csv

with open('nfl_teams.csv', mode='a') as csv_file:
    fieldnames = ['id', 'team', 'wins', 'losses']
    nfl_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    nfl_writer.writerow({'id': 4,'team': 'Giants', 'wins': 6, 'losses': 4})
    nfl_writer.writerow({'id': 5,'team':'Lions','wins': 8,'losses': 2})

```

### Lecture Topics
* CSV as a Database
* Object Oriented Programming

### Homework
* Tonight shoud primarily be used to absorb and finish everything thus far. [This](https://www.youtube.com/watch?v=q5uM4VKywbA) is a good video for you to watch to review everything.