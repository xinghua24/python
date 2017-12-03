Table Of Content

<!-- toc -->

- [Intro](#intro)
- [String](#string)
- [List, Tuple and Dictionary](#list-tuple-and-dictionary)
  * [List](#list)
  * [Tuplue](#tuplue)
  * [Dicutionary](#dicutionary)
- [Control Statement](#control-statement)
  * [If Statement](#if-statement)
  * [While Statement](#while-statement)
- [Function](#function)
- [Files](#files)

<!-- tocstop -->

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


**Getting input**<br>
Use input([promp]) build-in function to get input. [input reference](https://docs.python.org/3/library/functions.html#input)
```py
# getting input
inputString = input("please enter a string")

# It is useful to keep window open after script complete execution
input("press close to exit")
```

# String
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

# List, Tuple and Dictionary
## List
List - List are mutable
```py
people = ["Mark", "Brett", "Kerri", "Joan", "Rick", "Rose"]
print(people[0])    # Mark
people[1] = "B-man"    # change list item value
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


# Control Statement
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



# Function
Functions are defined using 'def'
```py
def printGreetings(name):
	print("Hello %s!" % (name))

printGreetings("Alice")    # Hello Alice!
```

# Files
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

Referenc:
* [Python 3 for Beginners Video Tutorial](https://www.safaribooksonline.com/library/view/python-3-for/12071LTPPY17/)
* [Tutorialpoint Python](https://www.tutorialspoint.com/python/index.htm)
* [Python 语法速览与实战清单](https://segmentfault.com/a/1190000012129654)
