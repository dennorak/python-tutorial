# Beyond the Basics
This document has a list of fun things to do with python that weren't covered in the main basics guide. Explore it and maybe you'll find something useful to you!

## `input()`
The input function is used to get user input from the terminal and save it as a string.
```python
some_var = input("prompt for the user: ")
```

## `time.sleep()`
I included this mostly because it comes in handy pretty often, but it's pretty self-explanatory. The time interval is measured in seconds
```python
import time
# sleep for 10 seconds
time.sleep(10)
```

## `print()` (In-Depth)
Besides just printing strings or variables, we can print multiple things together!
```python
>>> my_int = 100
>>> print("my int is", my_int)
my int is 100
```
> Note that this would fail if using a `+` instead of a comma, as strings cant be concatenated with integers.

Print can also be used to add newlines (`\n`), or used without newlines:
```python
>>> print("one\ntwo")
one
two

>>> print("hello", end = ' ')
>>> print("world!")
hello world!
```
