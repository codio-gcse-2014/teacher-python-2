# Task 3
# Press the 'Run File' menu button to execute

ef f(n):
    if n==0:
        return 0
    else:
        print("passing",n)
        return n+f(n-1) 
#functions calls itself but with an input one smaller. 
#This will go on until input is zero, in which case, the program #will retrace its steps and come back to the original function run.

print(f(3))