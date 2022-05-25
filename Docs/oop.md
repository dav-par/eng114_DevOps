## object oriented programming
OOP languages are built around organising software design around data/objects together with functions rather than keeping data and functions separate. These units of combined data elements and operational elements are called a Class.

### Advantages:
- Data and functions combined 
- Modularity 
- Low coupling (Can take class from one program and move to another)
- Easier to re-use 
- Closely models the real world

## Disadvantages:
- Can become hard to read with a large code base
- Not scalable 

## The four pillars of OOPs

### Abstraction
Describing something in an abstract way, we have a shared understanding of the characteristics of an object(car, bag)  
- Objects may have shared functions we can do on them (rather than hard coding the function on the object) - DON'T REPEAT CODE.

<h3>Abstraction - the object contains the complexity of the task</h3>
    <p>Describing something in an abstract way, we have a shared understanding of the characteristics of an object(car, bag)
    Objects may have shared functions we can do on them (rather than hard coding the function on the object) - DON'T REPEAT CODE.</p>

### Encapsulation
TODO - 

<h3>Encapsulation</h3>
        <p>You don't need to know the detail of a function to use it e.g. find_meaning_of_life(person) --> 42. Data about the object is hidden, the user gets a simple interface and the answer.
            <br>
        Good for privacy use, convention is to use underscores to indicate that you should not use it directly, @property decorators in a class to prevent object change</p>


### Inheritance
TODO - 

<h3>Inheritance</h3>
        <p>Superclass passes down features to Subclasses (also Base class and Derived class)
            <br>
        Import the Superclass then when creating class use class subclass(importname.superclass)
        </p>

### Polymorphism
TODO - 
<h3>Polymorphism - get a message, do something</h3>
        <p>The situation in which something occurs in several different forms. e.g. lots of objects can be switched on and the respective object knows what to do. The object will present an interface.
            <br>
        e.g print() - python will go up the inheritance hierarchy 
        </p>
- Something changing depending on context is polymorphic such as + and print()

