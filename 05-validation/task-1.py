# Task 1
# Press the 'Run File' menu button to execute

def get_op():
    print(fancy_banner("python calculator".upper()))
    print("Welcome to my calculator")
    u=input("Type \n1 to add, \n2 to subtract, 0 to quit \n>> ")
    try:
        validated_u=int(u)
    except:
        return 0
    else:
        return validated_u