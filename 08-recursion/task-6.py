# Task 6
# Press the 'Run File' menu button to execute

c=[100,50,20,10,5,2,1]
pur=38
tnd=100

def change(chng):
    can=[]
    while chng>0:
        if chng>=50:
            print("checking over 50")
            print(chng)
            can.append(50)
            chng=chng-50
            
        elif chng>=20:
            print("checking over 20")
            print("checking "+str(chng))
            can.append(20)
            chng=chng-20
            
        elif chng>=10:
            print("checking over 10")
            print("checking "+str(chng))
            can.append(10)
            chng-=10
            
        elif chng>=5:
            print("checking over 5")
            print("checking "+str(chng))
            can.append (5)
            chng-=5
            
        elif chng>=2:
            print("checking over 2")
            print("checking "+str(chng))
            can.append(2)
            chng=chng-2
            
        elif chng>=1:
            print("checking over 1")
            print("checking "+str(chng))
            can.append(1)
            chng=chng-1
            
    else:
        print("checking "+str(chng))
    return can


import random
for j in range(0,2):
    testAmount=random.randint(1,99)
    print("new program run ************ ")
    print("change for",testAmount," is",change(testAmount)) 