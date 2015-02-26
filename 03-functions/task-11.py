# Task 11
# Press the 'Run File' menu button to execute

a=[1,2,3,4,5,6] #create a list of integers called a

def avg(in_a): #start function definition
    return float(sum(in_a)/len(in_a)) 
#takes the sum of everything in a list (using a built-in Python sum of list function, 
#divides by the length (number of elements) of the same list – which is average, 
#forces it to be a real number (possibly, optional here, 
#but good practice to control the type of the data a function returns)

print(avg(a)) 
#functions are used just like variables. 
#(a) to the right of avg indicates that the list a will be sent to the function,
#and whatever this function returns will be printed.