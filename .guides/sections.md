---
title: Introduction
files: []
layout: 2-panels-tree

---
## Subroutines: Procedures and Functions 
It is possible to write a whole program as one big block but where possible we want to break it down into subroutines. There are several advantages to this: 

- The program becomes easier to read. 
- The program uses less memory at any given time.

Once a procedure finished running its variables get unloaded from memory (“garbage collected” is the industry term) freeing up memory for new tasks.

- The program becomes easier to test.


If you have tested a subroutine you don’t have to worry about it when you subsequently use it. 

- Subroutines can often be reused meaning code does not need to be rewritten.

Subroutines take control away from the main program, execute their “local” (smaller) task and then return control to the main program. Functions return control and a value, e.g. a result of a calculation, while procedures or “subs” just execute a series of commands. 

In Python, all subroutines are functions (which is not the same for Visual Basic, for example). 

It is just that “subs” are “sterile” functions that return no value (like worker bees in nature). 

In languages like Java we would put the word “void” into function definition if it is a sub, to make sure the programmer didn’t just forget to return a value.

---
title: Subs
files: []
layout: ""
step: 01-subs

---
We create a function or a sub with the `def` keyword. We supply a name and a set of round brackets for an optional list of parameters. Functions do their work and return control to the main program with the return keyword. Let’s make and call the simplest possible function:

## Task 1
Click to open task file : [task-1.py](open_file "01-subs/task-1.py").

Run the program by pressing the 'Run File' button in the top menu.

You will hopefully see the message `Hello World`.

This program prints out “Hello World”. 

- Beginning programmers often forget to separate words with spaces, and so we explicitly put `“ “` (space inside the speech marks), to remind that we need a space. The code that is indented after the `def` is the body of the function, which we later use (no indentation when using).

This program is analogous to:
```python
print(“Hello World”)
```

However, at a level, the nature of tasks can get quite complicated, so the skill of breaking even a simple part of a program into even smaller parts is very useful. 

Here, we even break down `Hello World` into `Hello` followed by a space `“ “`, followed by `World`. We separate the creation of `Hello World` from its usage by first defining a sub-program/function and then triggering it.

The body of the function is indicated by indentation. 

The first line of code that is not indented is a sign to Python that the procedure definition is over. 

The same principle applies to selection and iteration statements (if else and loops).

Functions and subs can be assigned to variables, as variables act as pointers to an area in memory that can hold data or an instruction to do something - a subroutine.

## Task 2
Click to open task file : [task-2.py](open_file "01-subs/task-2.py").

Run the program by pressing the 'Run File' button in the top menu.

The last line of the program is just `v`, which Python decodes to `sub_hw()` and then it knows it is a sub and launches it. 
However, this is a bad practice, as it is hard to follow for other programmers. Just because it can be done, doesn’t mean it’s right!

We can use subs in selection statements:

## Task 3
Click to open task file : [task-3.py](open_file "01-subs/task-3.py").

Run the program by pressing the 'Run File' button in the top menu.

Which should output something along these lines:
```python
Do I know you? (y/n)y
Nice to see you again
```
or 
```python
Do I know you? (y/n)n
Nice to meet you
```

We can say that calling a sub (you just have to type its name with round brackets) is like a wizard casting a spell by saying a special magic word. 

A function name is shorthand for a few lines of code, saving us time (assuming that we will have to execute these lines repeatedly).

## Task 4
Click to open task file : [task-4.py](open_file "01-subs/task-4.py").

Run the program by pressing the 'Run File' button in the top menu.

Which should output
```python
Thunder!
```
## Task 5
Click to open task file : [task-5.py](open_file "01-subs/task-5.py").

Run the program by pressing the 'Run File' button in the top menu.

Which should output
```python
Thunder!
Lightning!
Locusts!
Raining frogs!
```

### It’s magic!

Like a magic spell, packed lunch, or a school DT project, a function needs to be “prepared” first or “defined”, then it can be called. 

That means that we can define (“prepare”) functions and subroutines in the order that is different from the order of usage. 

Just like in a movie, the final scene of which can be shot first when filming and then edited to its proper place, function definitions can be done in a different order than their usage.

## Task 6
Click to open task file : [task-6.py](open_file "01-subs/task-6.py").

Run the program by pressing the 'Run File' button in the top menu.

Which should output
```python
Ready!
Steady!
Go!
```
## Challenge Exercise
Click to open the challenge file : [challenge-1.py](open_file "01-subs/challenge-1.py").

Modify the program to print out, on respective lines: 

```python
Going once, 
Going twice, 
Sold!
```
---
title: Procedural programming
files: []

---
We can make this even more proper by packaging the three sub calls into one main sub and then only calling that sub. This is useful for the future when you might want to trigger a lot of subs with just one button press in GUI.

## Task 1

Introducing the “main” function – the foundation of imperative programming paradigm

Click to open task file : [task-1.py](open_file "02-procedures/task-1.py").

Run the program by pressing the 'Run File' button in the top menu.

The advantage of using “main” which calls other subs – it makes the code more efficient by not having to type multiple subs, as long as they are triggered in the same order.

## Task 2

Input parameters – the brackets next to a function/sub’s name don’t have to be empty.  It’s like the tongue-and-groove in woodwork – we can chain functions/subs together and the brackets will “pipe” the data between them.

Click to open task file : [task-2.py](open_file "02-procedures/task-2.py").

Run the program by pressing the 'Run File' button in the top menu which should output


```python
160.0
hello there
some more tasks
subs are good for triggering many lines with one
```

## Task 3

Click to open task file : [task-3.py](open_file "02-procedures/task-3.py").

Write a program that asks a user for a distance in miles and returns the equivalent in km.

As a reminder, in Python we can ask a user for information by using the input() function, e.g.
```python
Distance=input(“Enter distance”)
```

When the data we need is numeric (will be used in calculations), we need to convert (aka “cast”) it to a numeric data type. 
e.g.
```python
int(input(“Enter a whole number”))
```
will result in a integer value
```python
float(input(“Enter a whole number”)) 
```
will result in a real value (number with decimals)

You can use this conversion factor: 1 mile=1.6 km.

It should output:
```python
Enter distance in miles: 100
160.0
```

## Challenge Exercise

Click to open task file : [challenge-1.py](open_file "02-procedures/challenge-1.py").

“Hacking” Python – modifying its built-in commands.

A pupil can’t be bothered to type out the print command and wants it shortened to 
```python
p
``` 
e.g. instead of 
```python
print(“test”)
```
she just wants to type `p(“test”)`. Can Python oblige?
---
title: Example section 4
editable: true

---
Some **awesome** content 4
