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
layout: ""
step: 02-procedures

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
title: Functions
files: []
layout: ""
step: 03-functions

---
So far, we only used subs. Functions are more flexible and more interactive. By returning a value they can influence how the rest of program will run, while subs wouldn’t do so as effectively. Let’s rewrite the sub as a function:

## Task 1

Click to open task file : [task-1.py](open_file "03-functions/task-1.py").

Run the program by pressing the 'Run File' button in the top menu.

You will hopefully see the message `Hello World`.

The return statement terminates the function (it will ignore any lines that follow it in its indented block but it also returns a value, a list, another function, etc. This also changes how we use functions. 

Rather than just calling them, we assign them – we can print them, change a variable’s value by it. 

Functions can be said to be used as “self-updating variables”.

## Task 2

Click to open task file : [task-2.py](open_file "03-functions/task-2.py").

Run the program by pressing the 'Run File' button in the top menu which should output


```python
5
72
31
```
- notice that every time we called the function it recalculated the random value

## Task 3

Click to open task file : [task-3.py](open_file "03-functions/task-3.py").

Run the program by pressing the 'Run File' button in the top menu.

You will hopefully see the message `Hello World` again

## Task 4

Click to open task file : [task-4.py](open_file "03-functions/task-4.py").

Run the program by pressing the 'Run File' button in the top menu and you will see the message `Hello World` again.

In Task 3 the function is “called” from a print, in Task 4 the function is assigned to a variable which is then in turn “called” by the print. 

## Task 5

Taking two parameter inputs into a sub

Click to open task file : [task-5.py](open_file "03-functions/task-5.py").

Run the program by pressing the 'Run File' button in the top menu

Here we are telling our function to expect two parameters, we then “pass in” the words which are then printed by the function and you see:

```python
Hello World
Two parameters walk into a sub…
```

## Task 6

Taking two parameter inputs into a function

The only difference between this and the previous task – we are using a function that return values, rather than a sub that does not.

Click to open task file : [task-6.py](open_file "03-functions/task-6.py").

Run the program by pressing the 'Run File' button in the top menu to see:
```python
Using a function with two parameters taken from
 global variables a, b
Monty Python
```
## Task 7

Using a function as an input: inserting two functions, each with two inputs, as an input into the third function of the same type

Since a function is a self-updating variable, it can be assigned to a variable, and even used as a parameter into a different function or sub. 

While this is not something done often, it does make for a good practice of sequencing and making pupils confident with parameter passing.

Click to open task file : [task-7.py](open_file "03-functions/task-7.py").

Run the program by pressing the 'Run File' button in the top menu to see
```python
Insert a function into another function? no problem
 here the function is inserted twice into itself
Monty Python Monty Python
```

## Task 8

Taking three input parameters into a function

Click to open task file : [task-8.py](open_file "03-functions/task-8.py").

Run the program by pressing the 'Run File' button in the top menu to see
```python
Taking more parameters
Hello new world
```

## Task 9

Taking an unlimited number of input parameters into a function using a wildcard (asterisk) 

Wildcard (asterisk) represents all possible inputs for when you don’t know how many user will input. 

The wildcard followed by an arbitrary name (here we used args) is “unpacked” into a list which contains all the elements sent to it. 

This is useful for the times when you don’t know how many inputs the user will provide. 

For example, calculating the average of a series of numbers, which might vary from case to case.


Click to open task file : [task-9.py](open_file "03-functions/task-9.py").

Run the program by pressing the 'Run File' button in the top menu to see
```python
Taking x parameters
('new', 'world')
Hello new world
```

## Task 10

This builds on Task 7.

We will re-use the function that takes two strings as inputs (inside its brackets) and joins them (inserting a space in between), returning one string out. 

We will create a list and insert each item of that list (there are only two, of course) as inputs into the function. 

This is not a good practice, Python programmers just pass the whole list and unpack it, as we will see later. 

However, this is a good opportunity to revise accessing list elements.

Click to open task file : [task-10.py](open_file "03-functions/task-10.py").

Run the program by pressing the 'Run File' button in the top menu to see
```python
getting input parameters off lists
Monty Python
```

## Task 11

Click to open task file : [task-11.py](open_file "03-functions/task-11.py").

This program takes the whole list as a parameter and computes its average. Read the comments that explain what is going on (# comment)

Run the program by pressing the 'Run File' button in the top menu to see
```python
3.5
```
- Note, that “sum” and “len” are built-in Python functions and come in very handy.



## Task 12 (optional task for advanced pupils only)

Click to open task file : [task-12.py](open_file "03-functions/task-12.py").

Finding out the rank of a number in a list. This is one of the standard pseudocode tasks that comes up in various exams at GCSE level. The pupils will be familiar with this concept from their GCSE. This and the next task, while optional, provide an example of Python working with lists that are passed as a parameter into a function.

The function in this program is to return a ranking of a provided value in a given list. This is a more traditional method, where we iterate through a list (passed in as “l”) and compare each item (“x”) to n. If it is larger, we increment our counter. In the end, we know how many items were larger than n which gives us n’s ranking.

Implement the following program. Create the pseudocode for it.

This demonstrates a couple of concepts:
- selection inside an iteration
- counter
- iterating through a list
- passing list as one of the parameters into a function.

```python
m=[3,5,7,1,8,12] # a list of numbers, e.g. pieces of litter picked up by respective pupils

def r1(mylist,n):
    c=1
    for x in mylist: 
    #iterate through every item in mylist
       if x>n: 
       #x acts as a wildcard in Scrabble, it assumes the values of all list items in turn, which is a very handy Python feature
           c+=1 
           #if the previous line is true (list item is > n) we increment the counter.
    return c 
    #functions stops and passes the return value to print

print(r1(m,2))
#check what would be the rank  (place to use sports terms) of 2 amongst the values in the list - we expect 6, as there are 5 numberson that list larger than 2 (5, 7, 8, and 12). So, a pupil who picked up only two pieces of litter will be ranked 6th in a litter picking competition.
print(r1(m,8))  
#check what would be the rank  (place to use sports terms) of 8 amongst the values in the list - we expect 2, as there is only 1 number  on that list larger than 8, which is 12, so 8 is in the second place. So, a pupil who picked up only two pieces of litter will be ranked 6th in a litter picking competition.
```

The output should be:
```python
6
2
```




## Task 13 (optional task for advanced pupils only)

Click to open task file : [task-13.py](open_file "03-functions/task-13.py").

Using Python’s built-in max function.

Implement the following program and create the pseudocode for it.

This function also returns a ranking of a provided value in a given list. 

However, it achieves the result differently – by using Python’s built-in features. 

It takes the value and the list as input parameters.

It works by utilising Python’s built-in “max” function. 

We are comparing the parameter “n” to each list max (the list is passed in as “l”). If the max is bigger than our n, we remove it and increment the counter, until n equals max. 

This way, we know how many numbers were larger than n – which is what a ranking is.

```python
m=[4,8,2,9] #prep a list
def r(l,n): #start a function definition
    ll=l[:] #create a local copy of a list m
    c=1 #default value for a counter
    while max(ll)!=n: #keep removing the largest number in list until #this list’s maximum number is not larger than our n
       ll.remove(max(ll))
       c+=1 #increment counter
    return c #function stops and passes the value out
print(r(m,2)) #output the rank of 2 in the list
print(r(m,8)) #output the rank of 8 in the list
```

The output should be:
```python
4
2
```
**Extension:** rerun the program but with values from the previous task. Did you get the same result? Would you say this method is better? [not better, just different, as code is not shorter or easier to read].


## Task 14 
Subs can be stored in lists. Run a string as a command through “exec”.

Click to open task file : [task-14.py](open_file "03-functions/task-14.py").

**Which 'previous exercise' is being referred to here**
```python
print("task 1x: subs can be assigned to list items")

print("mixed data lists are ok in Python")

my_list=[sub_hw_para("Bee's","knees"),sub_hw_para("I","Robot"),
         "sub_hw_para({},{})", 2,"Ronnies"]

my_list[0]
my_list[1]
exec(my_list[2].format('str(my_list[3])','my_list[4]')) 
#this will trigger those items in the list
#that are subs to run, the rest will be ignored
#this can be used instead of the switch statement
```

The SWITCH statement (otherwise known as CASE STATEMENT) is on the syllabus and is widely used in other languages, but not in Python. 

The SWITCH statement is a version of an IF ELSE IF ELSE structure. 

The main difference is that IF ELSE IF… allows for multiple values of multiple variables to be used, while the SWITCH statement usually looks at just one variable and based on various values of this variable, it will branch accordingly. 

The creator of Python thought it was not needed as IF is more universal and capable.





---
title: Combining functions and subs. Sharing data between them
files: []
layout: ""
step: 04-funcsubs

---
## Task 1
Click to open task file : [task-1.py](open_file "04-funcsubs/task-1.py").

Run the program by pressing the 'Run File' button in the top menu.

It should output:
```python
Enter distance in miles100
160.0 km
```

Note the use of the input parameter in the function. Indicate the line of code where this parameter acquires its value.

Implement extensions to this task: 
- convert line 3 into a function that returns whatever the user typed in; 
- replace 1.6 with a constant called FACTOR.

## Task 2
Click to open task file : [task-2.py](open_file "04-funcsubs/task-2.py").

Review this modification of the last line:
```python
print(miles2km(int(input("Enter distance in miles"))),"km")
```
and consider the advantages and disadvantages of it compared to the previous version.

We can freely combine subs and functions. 

However, then we have to plan out how they will share data between themselves, being semi-self-contained. 

We can use “global” variables for that. These variables are first used outside any procedure and are visible to all of them (but remain read-only unless specifically authorised by us to change their values). 

We can also use functions that return values to feed into another function or a sub.

This brings us to the concept of “variable scope”. 

Some variables are declared in the indented block of a function definition. 

They are only visible to the function they were placed in. 

Other parts of the program will not see them. 

Even worse, if we try to use them in other parts of the program, Python will create (it is dynamically typed, so it creates variables on as-needed basis) another variable with the SAME name but value of zero. 
This results in many mistakes. 

Alternatively, variables can be declared outside of function definitions in regular code and are accessible to the whole program, they are called global variables. 

However, functions can read the value of global variables but can’t write to them unless we “give the security clearance” to these functions to do so.

## Task 3
Click to open task file : [task-3.py](open_file "04-funcsubs/task-3.py").

Run the program by pressing the 'Run File' button in the top menu and the output should be something similar to:

```python
What is your name?Bob
Bob is a nice name, can I borrow 50p?
```
This program has 3 subs. Can you say the order in which these subs are executed?

## Task 4

An extension of this program illustrates how calling subs is ideal in iteration, such as a rudimental user interface here:

Click to open task file : [task-4.py](open_file "04-funcsubs/task-4.py").

Run the program by pressing the 'Run File' button in the top menu and the output should be something similar to:

```python
What is your name? or 'bye' to quitBob
Bob can I borrow 50p?
What is your name? or 'bye' to quitPeter
Peter can I borrow 50p?
What is your name? or 'bye' to quitbye
See you later, alligator
```
## Task 5

A further extension of this program:

Click to open task file : [task-5.py](open_file "04-funcsubs/task-5.py").

Run the program by pressing the 'Run File' button in the top menu and the output should be:
```python
********************
Press 
1 to add new user
2 to see customer balance
3 to adjust balance
4 to see customer list
5 to delete a customer
Any other key to quit
********************
 >> 2
Would ask for ID and show balance
********************
Press 
1 to add new user
2 to see customer balance
3 to adjust balance 
4 to see customer list
5 to delete a customer
Any other key to quit
********************
 >> 5
ID? 34
Delete user with id=34
********************
Press 
1 to add new user
2 to see customer balance
3 to adjust balance 
4 to see customer list
5 to delete a customer
Any other key to quit
********************
 >> 
bye!
```
- Note, it only does the interface, nothing else

## Task 6

Click to open task file : [task-6.py](open_file "04-funcsubs/task-6.py").

Run the program by pressing the 'Run File' button in the top menu and the output should be:
```python
* P * Y * T * H * O * N *   * C * A * L * C * U * L * A * T * O * R
Welcome to my calculator
Type 
1 to add, 
2 to subtract, 0 to quit 
>> 1
Enter first number >> 2
Enter second number >> 3
5.0
 * P * Y * T * H * O * N *   * C * A * L * C * U * L * A * T * O * R
Welcome to my calculator
Type 
1 to add, 
2 to subtract, 0 to quit 
>> 2
Enter first number >> 5
Enter second number >> 4
1.0
 * P * Y * T * H * O * N *   * C * A * L * C * U * L * A * T * O * R
Welcome to my calculator
Type 
1 to add, 
2 to subtract, 0 to quit 
>> 0
Quitting...
```

**Extension**: integrate with any of the previous tasks. For example, to do multiple unit conversion, not just miles to km or modify the previous task to say multiple things based on a user’s choice. 

## Task 7

Click to open task file : [task-7.py](open_file "04-funcsubs/task-7.py").

Extend the program to perform multiplication and division.
---
title: Validation
files: []
layout: ""
step: 05-validation

---
Functions are great for validation. The most basic validation method in Python (and many other languages) is the try: except: else: structure. 

This “try” structure will prevent a usual shell crash and allow our program to continue. It is triggered by an invalid operation.

Every time user input is required, we want to validate it. 

In this program we accept user input 3 times: choice of operator, number 1 and number 2. Python will accept anything from the user prompt. 

The crash would happen if user didn’t type anything or typed a word, and then when we try to convert this to an integer (in case of the operator choice) or float (the two numbers) it would crash. Here is validation for the choice of operation:

## Task 1
Click to open task file : [task-1.py](open_file "05-validation/task-1.py").

As you can see, we recognise the exact place where a program might crash if the user typed in something that wasn’t a number, the try structure is shown on bold. 

A sensible assumption in this case is to set it to zero if there was no valid input – this will allow the program to quit in a usual way. 

Otherwise (“else”), it will pass the function value as before. 

## Task 2
Click to open task file : [task-2.py](open_file "05-validation/task-2.py").

Run the program by pressing the 'Run File' button in the top menu.

It should output:
```python
0.625
The show must go on
```

## Task 3

We can further improve on this program by validating the other two inputs. How would you do it?

Click to open task file : [task-3.py](open_file "05-validation/task-3.py").

## Task 4

We can find out the length of a word through the len function. e.g.
```python
a=”monkey”
b=len(a)
print(b)
```

should give us 6 (for the 6 letters in “monkey”).

Design a presence check validation function with one input that returns True if the length of input is not zero, or False if its length is zero.

Click to open task file : [task-4.py](open_file "05-validation/task-4.py").

## Task 5

Integrate your function from Task 4 into Task 3. 

Assume the following order of validation: 
- Presence check, 
- Numeric check.

Click to open task file : [task-5.py](open_file "05-validation/task-5.py").