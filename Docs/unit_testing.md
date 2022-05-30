## Unit testing

A unit test is a way of testing a unit - the smallest piece of code that can be logically isolated in a system. In most programming languages, that is a function, a subroutine, a method or property. The isolated part of the definition is important.  

In his book "Working Effectively with Legacy Code", author Michael Feathers states that such tests are not unit tests when they rely on external systems: “If it talks to the database, it talks across the network, it touches the file system, it requires system configuration, or it can't be run at the same time as any other test."

# Philosophy
- Write the smallest possible test case that matches what we need to program
- Run the test and watch it fail. This gets you into thinking how to write only the code that makes it pass
- Write some code with the goal of making the test pass
- Run your test suite, repeat he above until all test pass
- Go back and refactor your new code, making it as simple and clear as possible while keeping the test suite green


# TTD
- Fail, Refactor, Pass

# Convention
- write tests first
- looks for module with "test_"

# Building unit tests
- make new test file "test_"
- import file
- import unittest
- 


# Opposition
- Agile - working code first


# Other
- pytest is nicer, works because you called it