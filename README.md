# Intro

**print()**<br>
print objects. print() is a build-in function. [print() reference](https://docs.python.org/3.6/library/functions.html#print)
```py
print("hello python")
print("hello", "python")
print(234.56)

# use **** as separator, separtor can be anything or empty string
print("hello", "python", "3", sep="****")   # hello****python****3
print("hello", "python", "3", sep="")    # hellopython3
print("hello", "python", "3", sep="\n")
```
**Build-in Types**<br>
Python has 5 standard data types
* Numbers
* String
* List
* Tuple
* Dictionary

There are three distinct numeric types: integers, floating point numbers, and complex numbers.
list, tuple and range are sequence types.

**use type() to get object type**<br> 
type() is also a build-in function. [type() reference](https://docs.python.org/3/library/functions.html#type)
```py
type(123)    # <class 'int'>
type(123.45)    # <class 'float'>
type("foo")    # <class 'str'>
```

**String**<br>
[str reference](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
```py
greeting = "Hello World"
print(greeting[0])    #'H

# slicing
print(greeting[0:3])    # Hel

# String concat
print( "Hello" + " " + "World" )    # Hello World

# formatting
print("My name is %s and I am %d years old" % ("Mark", 42))    # My name is Mark and I am 42 years old

# len()
greetings = 'Hello Python'
print(len(greetings))

# .find()
print(greetings.find("Py"))


```

**List, Tuple and Dictionary**<br>
```py
# List - List are mutable
people = ["Mark", "Brett", "Kerri", "Joan", "Rick", "Rose"]
print(people[0])    # Mark
people[1] = "B-man"    # change list item value


# Tuple - tuple is like list.'tuple' object does not support item assignment
numbers = (45,47,265,13)

# Dictionary - like a Map
gpas = {"Name": "Mark", "GPA": 3.55}
print(gpas)
```

**Getting input**<br>
Use input([promp]) build-in function to get input. [input reference](https://docs.python.org/3/library/functions.html#input)
```py
# getting input
inputString = input("please enter a string")

# It is useful to keep window open after script complete execution
input("press close to exit")
```

## Function
Functions are defined using 'def'
```py
def printGreetings(name):
	print("Hello %s!" % (name))

printGreetings("Alice")    # Hello Alice!
```

## Control Statemen   t
If Statement
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

While Statement
```py
def countdown(n):
    while n > 0:
        print(n)
        n = n -1
    print('Blastoff!')

countdown(5)
```

Referenc:
* [Python 3 for Beginners Video Tutorial](https://www.safaribooksonline.com/library/view/python-3-for/12071LTPPY17/)
* [Tutorialpoint Python](https://www.tutorialspoint.com/python/index.htm)
