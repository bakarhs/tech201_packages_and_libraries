# tech201_packages_and_libraries
tech201_packages_and_libraries

# Python Libraries
A library is a set of RELATED modules or packages bundled together.

Python libraries are collections of pre-written code that can be used to extend the functionality of the Python programming language. They are typically used to simplify complex tasks and to speed up development time. Python libraries are organized into modules, which contain functions and classes that can be used to perform specific tasks.

This is an example of using the random Library:
```python
import random

print(random.random()) # prints out a random float
```
You can also specify what you would like to take from a library by using `from` and specifying the library first.

Example:

```python
from random import random # importing a specific part of a library

print(random) # also prints out a random float
```
# Modules
## difference between module and library: 
A module is a collection of code or functions that uses the .py extension - allowing you to use that code/functions in your program A library is a set of RELATED modules or packages bundled together. Modules -> smaller, just code you can useLibraries -> larger/more complex compilations of resources.

```python
import os
import math, datetime, sys

working_directory = os.getcwd()
print(working_directory)

def return_user_id():
    print(os.getpid())

def return_user_name():
    print(os.uname())

print(datetime.date.today())

print((sys.path))

print(math.remainder(1, 5))
```
This code is using various modules to print out different information. The os module is used to get the current working directory and the process ID. The datetime module is used to print out the current date. The sys module is used to print out the system path. Finally, the math module is used to print out the remainder of 1 divided by 5.

when you're building a program it's very important to think about if you need to make a class/object yourself or a function. You may not need to make a function yourself if if there is a module that does what you are looking for already.

## Built-in functions
- print()
- len()
- type()

# pip and packages
pip is Python's package manager and installer
```python
import requests

requests_bbc = requests.get("https://www.bbc.co.uk")

print(requests_bbc.status_code)
print(requests_bbc.content)
```
This code uses the Python package manager and installer, pip, to import the requests package. The requests package is used to make HTTP requests, such as GET requests. In this example, the code is making a GET request to the BBC website and then printing out the status code and content of the response. The status code will indicate whether the request was successful or not, while the content will be the HTML of the page that was requested.
