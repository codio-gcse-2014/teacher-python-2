# Task 7
# Press the 'Run File' menu button to execute

def fancy_banner(my_str): #start function definition
    temp_str=""   	#default variable value to empty string
    delimiter=" * " #set the delimiter to an asterisk
    for letter in my_str: #run through every letter in a string
        temp_str+=delimiter+letter ‘’’increment the destination string by each letter plucked from the source string (my_str) followed by an asterisk. Why do that? It will write any string passed into this function spaced with asterisks making it more visible.’’’
    return temp_str #function stops and passes the value on

def get_op(): #this function returns a menu of choices to user
    print(fancy_banner("python calculator".upper()))#call prev function
    print("Welcome to my calculator")
    u=input("Type \n1 to add, \n2 to subtract, 0 to quit \n>> ")
    return int(u)

def get_nums(): #get user data
    a=float(input("Enter first number >> "))
    b=float(input("Enter second number >> "))  
    return a,b #Yes, we can return 2 values from a Python function

def add_nums(): #this sub adds the numbers and outputs the result
    print(a+b)

def sub_nums():#this sub subtracts the numbers and outputs the result
    print(a-b)

#main program begins
op=1

while op in range(1,3): #restrict the range of user choice to the ones specified in the program, will disallow any choice other than 1 and 2
    op=get_op() #get user input via another function
    if op==1:
        a,b=get_nums()#the function returns two values, they are “unpacked” to local variables a and b.
        add_nums() #perform the calculation
    elif op==2:
        a,b=get_nums()#the function returns two values, they are “unpacked” to local variables a and b.
        sub_nums()#perform the calculation
else:
    print("Quitting...")#if not 1 or 2 the program will exit
