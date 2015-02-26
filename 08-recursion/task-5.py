# Task 5
# Press the 'Run File' menu button to execute

def coins(a,c):
    #print(a,c)
    if a>=50:
        return " 50"+coins(a-50,c)
    elif a>=20:
        return " 20"+ coins(a-20,c)
    elif a>=10:
        return " 10"+ coins(a-10,c)
    elif a>=5:
        return " 5"+ coins(a-5,c)
    elif a>=2:
        return " 2"+ coins(a-2,c)
    elif a>=1:
        return " 1" +coins(a-1,c)
    else:
        return c
        
import random #will generate a few random amounts for testing
for j in range(1,10):
    testAmount=random.randint(1,99)
    print("change for",testAmount," is",coins(testAmount,""))