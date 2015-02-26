# Task 2
# Press the 'Run File' menu button to execute

import random

def r_n():
    return random.randint(0,100)

print(r_n())   #print straight to the screen, can’t use again
print(r_n())

lucky=r_n() #assign to a variable, can reuse later in the program
print(lucky)