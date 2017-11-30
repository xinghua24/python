Intro
====================================================
**print()**<br>
print objects. print() is a build-in function. [print() reference](https://docs.python.org/3.6/library/functions.html#print)
```python
print("hello python")
print("hello", "python")
print(234.56)

# use **** as separator, separtor can be anything or empty string
print("hello", "python", "3", sep="****")   # hello****python****3
print("hello", "python", "3", sep="")    # hellopython3
print("hello", "python", "3", sep="\n")
```

**use type() to get object type**<br> 
type() is also a build-in function. [type() reference](https://docs.python.org/3/library/functions.html#type)
```python
type(123)    # <class 'int'>
type(123.45)    # <class 'float'>
type("foo")    # <class 'str'>
```

**Text sequence type - str**<br>
[str reference](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
```python
greeting = "Hello World"
greeting[0]    # 'H'
```


Referenc:
* [Python 3 for Beginners Video Tutorial](https://www.safaribooksonline.com/library/view/python-3-for/12071LTPPY17/)
* [Python ]