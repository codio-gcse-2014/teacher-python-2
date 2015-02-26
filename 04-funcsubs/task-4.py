# Task 4
# Press the 'Run File' menu button to execute

EMPTY=""
uName=EMPTY
def interactWithUser():
    global uName #otherwise uName is read-only
    uName=input("What is your name? or 'bye' to quit")

    if uName==EMPTY:
        print("How rude not to say your name")
    elif uName=="Fred":
        print("How about that pound you borrowed last time?")
    elif uName=="Norma":
        print("You already asked me today!")
    elif uName=="bye":
        print("See you later, alligator")
    else:
        print(uName,"can I borrow 50p?")

def mainProgram():
    #need to interact with user 4 times to test
    #all of our selection options: Empty,Fred,Norma, 
    #everybody else
    while uName!="bye":
        interactWithUser() #same thing    
mainProgram()
