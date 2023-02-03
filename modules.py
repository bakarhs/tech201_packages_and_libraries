# Modules
# difference between module and library:
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

# when you're building a program its very important to think about if you need to make a class/object yourslef or a function. You may not need to make a function yourself if if there is a module that does what you are looking for already.

# Built-in functions
# print()
# len()
# type()











