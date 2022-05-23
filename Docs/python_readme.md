## Python notes:

Python is a dynamic object oriented program, this means it is built around organising software design around data/objects together with functions rather than keeping data and functions separate. These units of combined data elements are called a Class.

- A class has three elements:
  - The Properties 
  - The Operations
  - The Name

## Datatypes
- int - whole number
- float - decimal number
- string - text
- complex - a mix e.g. 45.j

## Strings:
- Slicing with [x:x]
- .strip() to remove white space on the outside of the string xyz.strip()
- Opposite of strip is TODO
- .count - return the amount of times text appears, example_text.count("ee")
- .lower - makes lower case 
- .upper - makes upper case 
- .replace replaces e.g example_text.replace("text", "new text")
- f strings for code in text e.g. print(f"hello {name}, you are {age} years old.)

## Booleans:
 - True != 0
 - False == 0
 - None == False (but none can be set to something)
 - NULL != NULL 
 - Can be used on strings print(example_text.isalpha())

## Constructors
These are a special kind of method which is the method used to make new instant of the class __init__(self):, self refers to the current object. Inside a constructor self means the object being created inside the class

## Method/Functions
- A chunk of code that performs some actions on some arguments. Defined by def, e.g. def cool_function(arg1, arg2):
- would be called by supplying the arguments e.g. cool_function("bob", 7)
- you can set default values when creating args for a function def function(value1="default", value2="default2")
- when defining a function you can tell it what values to expect to recive and output
  - def divide_two_values(a: int,b: int) -> float:
  - a function becomes a method if it's in a class


## Setter functions
Setter function/Set method
    TODO


## Lists
- list.append(value) - add value to end of list
- list.remove(value) - remove first instance of value
- \+ is used to join lists - can only be used with other lists, use [] to add a single element 
- When accessing elements of a list the index must be an int 
- lst.index(value) to find the index of a valu 
- .append to add to end of a list 
- del - remove from list by index, pop will remove and return 
- list slicing - Syntax: l=l[:index]+[‘new_value’]+l[index+1:]
- To access sublists put the indexs next to each other e.g. [1][3]
- When adding to a list with .append make sure to follow list formatting e.g
![image of adding to list](Docs/resources/list_adding_to.png))
- lists do not have .replace, you have to use slicing, .insert can be helpful too
- .sort() and sorted() are amazing, b = sorted(a, reverse=True)
- range() can make a list of integers


## Dictionaries
- Curley brackets
- key and value pairs
- key is like the index
- does not have an order, call on the key

## If functions
- sequential
- Don't forget failure states
- nested loops happen in order


## Class
- instantiation is creating an instant of a class
- initialising is creating values for an instant of a class
- dunder init, one "_" is warning, two is "_" you can't do it (in theory)
- setters and getters help up to be more neat and protect the code


## Syntax tips
- +=, put the + first


## Pycharm shortcuts:
- Comment out code:
  - Ctrl ?