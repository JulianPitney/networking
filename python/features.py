import time 
import asyncio
import socket 



# list comprehension
l1 = [i for i in range(10) if i % 2 == 0]

# dict comprehension
d1 = {item:item+1 for item in l1 if item % 2 == 0}

#------------
# generator |
#------------
def count(max):
    number = 0
    while number <= max:
        yield number
        number += 1

for num in count(10):
    print(num)

# Note: calling a generator function returns a generator object, not the yielded value. 
# Generator objects are both an iterable and an iterator.

#-----------
# Iterable |
#-----------
# Any python class that implements __iter__()

#-----------
# Iterator |
#-----------
# An iterator is any object that:
# Implements __next__() (returns the next value).
# Implements __iter__() (returns itself).

#------------
# decorator |
#------------
# A function that takes another function as input, modifies that function in some way, and then returns the modified function.
def timer_decorator(func):
    def wrapper(x, y):
        start = time.time()
        func(x, y)
        stop = time.time()
        print(f"{func.__name__} took {stop - start}s to run.")
    return wrapper 

@timer_decorator
def some_arbitrary_function(x, y):
    for i in range(x):
        print (y*x*i)
    
some_arbitrary_function(1000, 45)


#------------------
# Context Manager |
#------------------
# Python object which implements the __enter__() and __exit__() methods. 
# Allows the object to be used with the "with" keyword.


#----------
# Packing |
#----------
# Packs any numbr of args into a tuple
def f1(*args):
    print(args)
f1(42, 'sky', 'aliens', 0.55425)
# Packs any number of key-word args into a dictionary
def f2(**kwargs):
    print(kwargs)
f2(aids=42, port=420, dog='goat')

# Note that both * and ** work for packing and unpacking. 

#------------
# Unpacking |
#------------
# Many builtin python containers have basic unpacking semantics where you can do the following:
obj1, obj2, obj3 = [1, 2, 3]
obj1, obj2, obj3 = ('a', 'b', 'c')
key1, key2, key3 = {'pig': 3, 'dog': 'c', 'giraffe': 42}

l1 = [1, 2, 3]
i1, i2, i3 = (l1)
d1 = {'v1': 1, 'v2': 2, "v3": 3}
def func(v1, v2, v3):
    print(f"{v1}{v2}{v3}")
func(**d1)

#-----------
# F-String | 
#-----------
pi = 3.1415926535
print(f"Pi to 2 decimal places: {pi:.2f}")

#---------------------
# Ternary Expression |
#---------------------
# value_if_true if condition else value_if_false
# Note that you can nest these but it's a terrible idea because it's super unreadable and you should just use normal multi-line if-else at that point. 
score = 51
test_result = 'Fail' if score <= 50 else 'Pass'
def check_pass_fail(score):
    return 'Fail' if score <= 50 else 'Pass'
print(check_pass_fail(score))


#------------------
# Walrus Operator |
#------------------
# It allows you to assign a value to a variable as part of an expression, instead of needing a separate assignment statement.
score1 = 50
if (var1 := score1 <= 50):
    print(var1)

with open("features.py") as f:
    while (line := f.readline()):
        print(line.strip())

#-------------
# Type Hints |
#-------------
def func2(param1: str) -> str:
    return f"Echoing {param1}"

# With assignment
age: int = 31
# Without assignment
name: str


#----------------------------------
# Equality vs Identity Comparison |
#----------------------------------

v1 = 1
v2 = 1
# true
if v1 == v2:
    print(f"{v1+v2}")

# Python interns small integers (-5 to 256) and some strings, so is can be True for some literals.
# Interning is a performance optimization where Python reuses immutable objects, rather than creating new ones every time.
# true
if v1 is v2:
    print(f"{v1+v2}")

a = [1, 2, 3]
b = a
# true
if id(a) == id(b):
    print("same object")


#-----------------
# Set Operations |
#-----------------
# Unordered collection of unique, hashable elements. 
set1 = {1, 2, 3, 4}
set2 = {2,4,6}

union = set1 | set2
intersection = set1 & set2
differnece = set1 - set2
symmetric_difference = set1 ^ set2

# All unique items in both sets
print(union)
# All unique items that are in both sets
print(intersection)
# s1 - s2 (All items in s1 that are not in s2)
print(differnece)
# s1 ^ s2 (In s1 AND not in s2)
print(symmetric_difference)


#---------------------
# Exception Handling |
#---------------------
def safe_integer_divide(int1, int2):
    try:
        int1 / int2
    except ZeroDivisionError:
        print(f"Error! Division by zero! {ZeroDivisionError}")
    else:
        print("Division Success!")
    finally:
        # Always runs.
        ...
safe_integer_divide(5, 0)

# Handle only the errors you expect and can deal with.
# Don't blanket-catch everything.
# Keep try/except scopes tight and clear.
# 

#-------------
# Coroutines (asyncio) |
#-------------

async def run_tasks():
    tasks = [asyncio.create_task(do_work(i, f"coro{i}"), name=f"coro{i}") for i in range(5)]
    output = await asyncio.gather(*tasks)
    print(output)

async def do_work(delay: int, text):
    print(f"Waiting {delay}s...")
    await asyncio.sleep(delay) 
    return text

asyncio.run(run_tasks())


# We say that an object is an awaitable object if it can be used in an await expression.
# There are three main types of awaitable objects: coroutines, Tasks, and Futures.
#
# Coroutine: Any function defined with the async keyword.
# Tasks: Wrappers around coroutines (via asyncio.create_task())
# Futures: A Future is a special low-level awaitable object that represents an eventual result of an asynchronous operation.
#
# Note: asyncio does not give prallelism within the python program. It gives concurrency.
# Think about it like this:
# While your Python code is "paused" (await), the outside world (network stack, database, OS) is doing real parallel work.
# You're efficiently letting the event loop manage many waiting coroutines without blocking the Python interpreter.
# asyncio is a good concurrency solution for io-bound programs. 

#-----------------
# Mutlithreading |
#-----------------
# Python supports threads, but the GIL prevents more than 1 thread at a time from executing bytecode in the python virtual machine.
# Threads in python are good for io-bound programs which use blocking libraries. If a library is compatible with asyncio (provides
# awaitable primitives in it's API) then asyncio is a better choice as it's even more lightweight than python threads. 


#------------------
# Multiprocessing |
#------------------
# Use this when you need true parallelism in Python or when your program is cpu-bound. 



#----------
# Logging |
#----------
import logging 

# Create a logger
logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)

# Create two handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("app.log")

# Create two formatters
console_formatter = logging.Formatter("%(levelname)s - %(message)s")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Attach formatters to handlers
console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)

# Attach handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("Debugging info")
logger.info("General information")
logger.warning("Something's not right")
logger.error("An error occurred")

# Note that the hierarchy goes like this
# logger -> handlers -> filters -> formatters -> output
# If there are multiple handlers then each will receive a copy of the log record.

# Q: What's the difference between logger level vs handler level?
# A: Logger can have a level, and so can each handler.

# Q: How would you log to both console and file?
# A: Two handlers attached to same logger.

# Q: How do you avoid configuring logging in every module?
# A: Set up logging centrally in your main entrypoint.



#--------------------
# Memory Management |
#--------------------

# id() function
obj1 = 1
obj2 = 1
obj3 = 2
# Remember that python interns some immutable objects (e.g the integer 1)
print(f"{id(obj1)}\n{id(obj2)}\n{id(obj3)}")

# Note: Remember that the assignment operator in python does not create a copy of the object
# being assigned. It just creates a reference to that object. 

import copy
# Shallow Copy:
# copy.copy(obj) creates a new object, but only copies references for nested/mutable elements.
# Top-level object is copied, but inner objects are still shared.
l1 = [[1,2],[3,4]]
l2 = copy.copy(l1)

# You'll see here that the outer objects are different because a new outer list was created.
print(f"Outer list IDs:\n{id(l1)}\n{id(l2)}")
# And you'll see here that the inner objects have the same ID because only references have been copied. 
print((f"Inner List Index 0 IDs:\n{id(l1[0])}\n{id(l2[0])}"))

# Deep Copy
# copy.deepcopy(obj) recursively copies everything.
# No shared references — completely independent.
l2 = copy.deepcopy(l1)
# You'll see here that every ID is different because the new list has new objects all the way down the nested object structure. 
print(f"Outer list IDs:\n{id(l1)}\n{id(l2)}")
print((f"Inner List Index 0 IDs:\n{id(l1[0])}\n{id(l2[0])}"))


#-----------------------
# Mutable vs Immutable |
#-----------------------------------------------
# Mutable                | Immutable           |
#-----------------------------------------------
# list                   | tuple
# dict                   | str
# set                    | int, float, complex
# bytearray              | bytes
# Custom class instances | frozenset

# Immutable Example
# When you "modify" an immutable object you're actually just creating a new object. 
b = "hello"
print(f"Old ID: {id(b)}")
b = b + " world"
print(f"New ID: {id(b)}")


#-----------
# Sequence |
#-----------
# A sequence is an ordered collection that supports indexing and slicing.
# Examples include list, tuple, str, bytes.  
# All sequences are iterables, but not all iterables are sequences.
# Formal definition: Anything that follows the collections.abc.Sequence protocol.

#------------
# Container |
#------------
# Holds references to other objects.
# Examples include list, tuple, dict, set, str.
# Support membership testing with in / not in.
# May or may not be ordered.
# Formal definition: Anything that follows the collections.abc.Container protocol.


#----------
# Slicing |
#----------
sequence = [0,1,2,3,4,5,6,7,8,9]
# Start index (inclusive)
start = 0
# Stop index (exclusive)
stop = 5
# Step 
step = 3
sub_sequence = sequence[start:stop:step]
print(sub_sequence)

# Start at index 0 and stop at 4.
sub_sequence = sequence[:5]
# Start at index 3 and go to end.
sub_sequence = sequence[3:]
# Every 2nd element
sub_sequence = sequence[::2]
# Negative step (reverse a list)
sub_sequence = sequence[::-1]
# Last 5 elements
sub_sequence = sequence[-5:]
# Arbitrary negative index slice
sub_sequence = sequence[-5:-2]
print(sub_sequence)


#------------------
# Lambda Function |
#------------------
# Short, anonymous functions.
sorted_list = sorted([(0,6), (25,-1),(0,355),(435,-24)], key=lambda x: x[0])
print(sorted_list)
