# Task 1
# Press the 'Run File' menu button to execute

s="monkey"
def r(n):
    if n==0:
        return (s[0])
    else:
        return s[n]+r(n-1)
        
print(r(5))