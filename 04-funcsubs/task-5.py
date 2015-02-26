# Task 5
# Press the 'Run File' menu button to execute

uChoice="1"
part1="*"*20+"\n"+"Press \n1 to add new user\n2"
part2=" to see customer balance\n3 to adjust balance"
part3=" \n4 to see customer list\n5 to delete a customer\nAny other key "
part4="to quit\n"+ "*"*20+"\n >> "
message2user=part1+part2+part3+part4

#main program
while uChoice in ["1","2","3","4","5"]:

    uChoice=input(message2user)
    if uChoice=="1":
       print("Would add a customer")
    elif uChoice=="2":
       print("Would ask for ID and show balance")
    elif uChoice=="3":
        w=int(input("ID? "))
        p=int(input("How much are you paying today?"))
        print("Would show an updated balance")
    elif uChoice=="4":
        for t in range(4):
           print(str(t)+" owes £"+str(t*45))

    elif uChoice=="5":
        w=int(input("ID? "))
        print("Delete user with id="+str(w))
print("bye!")
