# Task 3
# Press the 'Run File' menu button to execute

#ask person's name, then state it's a nice name
#ask to borrow 50p
uName="" #this sets up a global variable - that all DEF subs can use

def askName():
    global uName # authorise this sub to change a global variable
    uName=input("What is your name?")

def tellUser():
    print(uName,"is a nice name, can I borrow 50p?")

def mainProgram():
    askName()
    tellUser()
    
mainProgram()
