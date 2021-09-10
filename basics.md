# Python Basics
## Introduction
Welcome to the tutorial! This is going to be an overview of the Python programming language, going over things such as syntax, datatypes, and functions.

- If you've never programmed before, start from the beginning of this project and work your way down
- If you have programming experience and just need the python syntax walkthrough, go through `First Steps`, find the syntax section, and feel free to skip the rest.

This project is designed to be more of a guide than a tutorial, so create a blank python file (ending in `.py`) and have fun with it! Copy the examples from the guide, but if you want to get the most out of this I recommend that you see what else you can do with these tools!

One more thing before we begin, the code block seen will be formatted to display what they should output when ran. To differentiate this, any lines run will begin with `>>>`, while anything outputted will not.

## First Steps
To start us off, we're going to create a simple "Hello, World!" program. This will introduce us to some important concepts, namely built-in functions and strings. We'll get more into strings later, but for now all we need to know is that they're essentially a way to store text.

##### Basics Basics
> If you have no prior experience at all, a function is basically a premade block of code that you can call to do something. These functions (almost) always end with parentheses, and depending on the function you can pass data into the function using something called an argument. In our case, we're going to pass the string we want to print to the `print()` function.

To print in python, we're going to use the built-in function `print()`. Let's do this now, passing in our "Hello, World!" string:

```python
>>> print("Hello, World!")
Hello, World!
```

Congratulations! You've just created your first python program! If you'd like, take some time and mess around with `print()`.

We're going to cover one more built-in function for now, as we'll use it later: type `type()` function. This function, when passed a variable, will return the type of the variable.
```python
>>> print(type(my_var))
<class 'Datatype'>
```

## Syntax
Perhaps one of the most important parts of programming, syntax is the way in which the code is structued. Common examples of syntax are parentheses, semicolons, and brackets. Python, however, uses spaces/tabs, colons, and pounds.
### Pounds
The pound key (`#`) is python's form of comment. For example, if I have some code:
```python
somelib.somefn(var1, var2)
```
and I'm worried I'll forget what it does, I can add a comment on it in a few ways:
```python
somelib.somefn(var1, var2) # This does x, y, z
```
```python
# this does x, y, z
somelib.somefn(var1, var2)
```
### Tabs / Spaces & Colons
While in other programming languages spacing is mostly used to make the code easier to read, in python it accounts for the structure of the code. If I have a loop of some kind, any code that's inside the loop should be tabbed inside the loop. While we're on the topic of loops, the colon (`:`) is used to denote the start of some section of code (function, loop, etc.). Let's see an example of this now:
```python
for item in list:
    print(item)
```
The loops themselves will be covered in a bit, but just know the way your code is laid out is important.

## Variables and Datatypes

Variables and datatypes are the basis for moving things around in most programming languages, as if everything was set from the beginning our code would do the same thin every time! One important difference of python compared to other languages is dynamic typing. This means that variables can change datatypes, so be careful! Python has many datatypes, but we're going to go over the basic ones here:

### Boolean (Common names: bool)
A boolean is just a binary value, and is most commonly set to either `True` or `False`. This is the most simple datatype, as it can only be one of two values. A note for python, `True` and `False` are case-sensitive (as are most variable names), so make sure they're capitalized!

```python
>>> my_boolean = True
>>> print(my_boolean)
True

>>> my_boolean = False
>>> print(my_boolean)
False

>>> print(type(my_boolean))
<class 'bool'>
```

### Integer (Common names: int)
An integer is the base for numbers in python, it is a whole number. This isn't to be confused with a `float` (which we'll get to in a bit), which is any non-whole number.

```python
>>> my_integer = 100
>>> print(my_integer)
100

>>> print(type(my_integer))
<class 'int'>
```

### Float (Common Names: float)
A float is essentially the same thing as an integer with the major difference being decimals. Floats are always decimals, even if set to a whole number.

```python
>>> my_float = 19.99
>>> print(my_float)
19.99

>>> my_float = 10
>>> print(my_float)
10.0

>>> print(type(my_float))
<class 'float'>
```

### String (Common Names: str)
A string is simply a string of characters. We saw how they can be used earlier, but we can also define them as variables like we've been doing:

```python
>>> my_string = "test test"
>>> print(my_string)
test test

>>> print(type(my_string))
<class 'str'>
```

### List (Common Names: Array, arr)
A list is basically what it sounds like, a list of other items. The items in this list can be any datatpe, as well as functions (in some cases).

```python
>>> my_list = ["item one", "item two"]
>>> print(my_list)
["item one", "item two"]

>>> print(type(my_list))
<class 'list'>
```

Lists have special methods for getting specific items from them. When doing this, there's one important detail to keep in mind: Lists start at zero!

```python
>>> my_list = ["first item", "second item"]
>>> print(my_list[0])
first item

>>> my_list[0] = "new first item"
>>> print(my_list)
["new first item", "second item"]
```

## Dictionaries (Common Names: dict, hash)
Dictionaries are similar to lists with the difference being in the way items are placed. As we saw from lists, items are indexed by their position in the list. Dictionaries are indexed using keys, or strings that can be set equal to a value.

```python
>>> my_dict = {"key_one": "value_one", "key_two": "value two"}
>>> print(my_dict["key_one"])
value_one
```

## Operators
Now that we've covered the basics of variables and datatypes in python, let's move on to operators. These are pretty self-explanatory, so look through the code block and you should be able to see what's going on:

```python
>>> print(1 + 2)
3

>>> print(2 - 1)
1

>>> print(3 * 4)
12

>>> print(12 / 3)
4

# exponents
>>> print(3 ** 2)
9

# remainder
>>> print(9 % 2)
1
```

Besides basic operations, we also need to have comparison logic. These are operations that return a boolean, depending on if the comparison was true or not

```python
>>> print(1 == 2)
False

>>> print(1 == 1)
True

>>> print(2 > 1)
True

>>> print(2 >= 2)
True

# not equal to
>>> print(1 != 1)
False
```

## Imports
Imports are essential to python if you want to have time to code what you love, instead of the things needed to code what you love. Imports are a way to get use code that someone else has written (a library). For example, if I want to get the current time, without imports I would have to find a way to hook into the system and get the time. With imports, I can do:

```python
>>> import datetime
>>> print(datetime.datetime.now())
```

Imports also make it easy to only get what you need and how you need it! For example, if I want the `sleep()` function from the `time` library, but I want to call is as `nap()`, I can do:

```python
>>> from time import sleep as nap
>>> nap(1)
```
The `from` keyword will select items from a library to import, while the `as` keyword will change it's name.

### Libraries to mess with
- [Time](https://docs.python.org/3/library/time.html)
- [TermColor](https://pypi.org/project/termcolor/)
- [Requests](https://docs.python-requests.org/en/master/)

If python can't find a library (ModuleNotFoundError), it is more than likely not installed. To install libraries, run one of the following depending on yourt installation: <br>
`pip3 install <library>` / `py -3 -m pip instal <library>`

## Functions
Aside from importing libraries, sometimes we have a chunk of code that we use many times. Instead of typing the same lines over and over again, we can create a function. Like the other functions, we've learned about, custom functions can take arguments in, perform actions, and return values. To return data from a function, use the `return` keyword (seen below).

Let's take the sets of numbers (2, 3) and (4, 5) and multiply them together, and then raise the result to the power of the first number.

- Without a function
```python
# 2, 3
num1 = 2
num2 = 3
value1 = value ** num1 # Gets the answer
# 4, 5
num1 = 4
num2 = 5
value = num1 + num2
value2 = value ** num1 # Gets the answer
```
- With a function
```python
def my_function(num1, num2):
    value = num1 + num2
    return value ** num1
value1 = my_function(2, 3) # Gets the answer
value2 = my_function(4, 5) # Gets the answer
```

As you can see, using a function even for something small like this example can drastically cut down on the size of your code. Now that we see the advantages, let's examine the function that we made

The `def` keyword lets your computer know we're defining a function named `my_function`, and this function takes the arguments `num1` and `num2`. When we call our function, we're supplying the values for `num1` and `num2` inside the parentheses.

## Loops
Sometimes we need to iterate over items in a list, or repeat a certain action a number of times. Instead of typing the same lines multiple times to accomplish this, we can use loops instead.

There are two major types of loops in python, `while` loops and `for` loops.

### `while` Loops
These loops are useful when it comes to waiting. For example, if I want to count up to 10, I could use a while loop like this:
```python
>>> num = 0
>>> while num < 10:
>>>     print(num)
>>>     num += 1
1
2
...
10
```

### `for` Loops
These loops are useful for iterating over a set of items, particularly lists. If we wanted to print all values in a list seperately, we could do this:
```python
>>> my_list = ["item one", "item two", "item three"]
>>> for item in my_list:
>>>     print(item)
item one
item two
item three
```
Note that we're storing the value of whatever item we're on in the temporary variable `item`

## Conclusion
By this point you should have a pretty clear understanding of how python works! We learned how to make functions, use operators on data, how to import libraries, and how variables work. I now encourage you to have fun with these tool and create some really cool projects! If you'd like a starting point, check out the covid_tutorial project in this repo.

Happy coding!
