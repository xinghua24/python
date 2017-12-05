Table Of Content

<!-- toc -->

- [Intro](#intro)
- [String](#string)
- [List, Tuple and Dictionary](#list-tuple-and-dictionary)
  * [List](#list)
  * [Tuplue](#tuplue)
  * [Dicutionary](#dicutionary)
- [Control Statement and Iterator](#control-statement-and-iterator)
  * [If Statement](#if-statement)
  * [While Statement](#while-statement)
  * [For loop](#for-loop)
- [Function](#function)
- [Files](#files)
- [Module](#module)
- [Subprocess](#subprocess)

<!-- tocstop -->

# Intro

**Comment**<br>
```py
""" Multiline strings can be written
    using three "s, and are often used
    as documentation.
"""
```

**print()**<br>
print objects. print() is a build-in function. [print() reference](https://docs.python.org/3.6/library/functions.html#print)
```py
print("hello python")
print("hello", "python")
print(234.56)

# use **** as separator, separtor can be anything or empty string
print("hello", "python", "3", sep="****")   # => hello****python****3
print("hello", "python", "3", sep="")    # => hellopython3
print("hello", "python", "3", sep="\n")
```


**Getting input**<br>
Use input([promp]) build-in function to get input. [input reference](https://docs.python.org/3/library/functions.html#input)
```py
# getting input
inputString = input("please enter a string")

# It is useful to keep window open after script complete execution
input("press close to exit")
```


**Build-in Types**<br>
Python has 5 standard data types
* Numbers(integers, floating point numbers, and complex numbers)
* Boolean(value are True or False)
* String
* sequence types(List, Tuple, Dictionary)


**use type() to get object type**<br> 
type() is also a build-in function. [type() reference](https://docs.python.org/3/library/functions.html#type)
```py
type(123)    # => <class 'int'>
type(123.45)    # => <class 'float'>
type("foo")    # => <class 'str'>
```



# String
[str reference](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
```py
greeting = "Hello World"
print(greeting[0])    # => 'H

# slicing
print(greeting[0:3])    # => Hel

# String concat
print( "Hello" + " " + "World" )    # Hello World

# formatting
print("My name is %s and I am %d years old" % ("Mark", 42))    # => My name is Mark and I am 42 years old

# len()
greetings = 'Hello Python'
print(len(greetings))

# .find()
print(greetings.find("Py"))

# format
"the Sum of 1 + 2 is {0}".format(1+2)    # => 'the Sum of 1 + 2 is 3'
```

# List, Tuple and Dictionary
## List
List - List are mutable
```py
people = ["Mark", "Brett", "Kerri", "Joan", "Rick", "Rose"]
print(people[0])    # => Mark
people[1] = "B-man"    # => change list item value
```

## Tuplue
Tuple - tuple is like a immutable list.
```py
numbers = (45,47,265,13)
print(numbers[0])
```

## Dicutionary
Dictionary - like a Map
```py
gpas = {"Name": "Mark", "GPA": 3.55}
print(gpas['GPA'])
```


# Control Statement and Iterator
## If Statement
```py
x = input("x:")
y = input("y:")
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')
```

## While Statement
```py
def countdown(n):
    while n > 0:
        print(n)
        n = n -1
    print('Blastoff!')

countdown(5)
```

## For loop
```py
# print 4 5 6 7
for i in range(4, 8):
    print(i)

```

# Function
Functions are defined using 'def'
```py
def printGreetings(name):
	print("Hello %s!" % (name))

printGreetings("Alice")    # => Hello Alice!
```

# Files
read file and write file
```py
# write file
myfile = open('output.txt', 'w')
myfile.write("ABC\n")
myfile.write("DEF\n")
myfile.close()

# read file
myfile = open('output.txt', 'r')
content = myfile.read()
print(content)
myfile.close()
```


**Read file line by line**<br>
```py
def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

print(linecount('linecount.py'))
```


# Module

**Importing a Module**<br>
```py
# import a module
import math
print(math.sqrt(16))

# import specific functions from a module
from math import ceil, floor
print(ceil(3.7))   # => 4.0
print(floor(3.7))  # => 3.0

# import all, not recommended
from math import *
print(sqrt(16))

# find out founctions and attributes defined in a module
import math
print(dir(math))
```


Any file that contains Python code can be imported as a module. importing a module will execute the code in that file.
```py
import linecount
```

# Class
You can assign attributes to an Object. functions defined in an class should have a 'self' 
reference to the instance by convention. It can be named differently but not recommended.
```py
class Time:
    """Represents the time of day.
    """
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))
time = Time()
time.hour = 11
time.minute = 59
time.second = 30

time.print_time()  # => 11:59:30
```


**init method**<br>
the init method is __init__(two underscore characters, followed by init, and then two more underscores)
```py
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

# calling initializer
time = Time(5,30,0)
```

# Subprocess
The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. 
```py
import subprocess

subprocess.call(['ls', '-l'], shell=True)
```
[subprocess reference](https://docs.python.org/3/library/subprocess.html#module-subprocess)


Referenc:
* [Python 3 for Beginners Video Tutorial](https://www.safaribooksonline.com/library/view/python-3-for/12071LTPPY17/)
* [Tutorialpoint Python](https://www.tutorialspoint.com/python/index.htm)
* [Learn x in y minutes - python](https://learnxinyminutes.com/docs/python3/)
* [Python 语法速览与实战清单](https://segmentfault.com/a/1190000012129654)
