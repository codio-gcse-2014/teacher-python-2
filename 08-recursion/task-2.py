# Task 2
# Press the 'Run File' menu button to execute

def cdown(t):
    if t==0:
        print('blast off')
    else:
        print(t)
        cdown(t-1)
cdown(10)