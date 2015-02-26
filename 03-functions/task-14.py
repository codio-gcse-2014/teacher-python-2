# Task 14
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
##used in other languages
for each_list_item in my_list:
    each_list_item