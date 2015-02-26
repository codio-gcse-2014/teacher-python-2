# Task 6
# Press the 'Run File' menu button to execute

a=[28, 45, 22, 33, 36, 9, 32, 46]
b=[36, 8, 17, 21, 30, 4, 13, 9]
c=[]
for x in a:   #iterate through all items in list a
    if x in b:   #check if any are in list b
        c.append(x) #add to summary list c
        print("found on both lists",x) #feedback
print(len(c)) #print count of items in c aka how many match