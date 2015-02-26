# Task 4
# Press the 'Run File' menu button to execute

import random

def r_n():
    return random.randint(1,49)

def lottery_t():
    n=0
    lucky=[]
    while len(lucky)<8:
        n=r_n()
        if n not in lucky:
            lucky.append(n)
    return lucky

def main():
    print("Welcome to Station Rd Corner Store. Next draw tomorrow.")
    num_of_t=int(input("How many lottery tickets are you buying today? >> "))
    print("Here are your tickets, it will be £{}.".format(num_of_t*2))
    for j in range(num_of_t):
        print(lottery_t())

main()