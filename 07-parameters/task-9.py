# Task 9
# Press the 'Run File' menu button to execute

import random

def r_n():
    return random.randint(1,50)

def lottery_t():
    n=0
    lucky=[]
    while len(lucky)<8:
        n=r_n()
        if n not in lucky:
            lucky.append(n)
    return lucky

def generate_tickets(n):
    all_tickets=[]
    for j in range(n):
        all_tickets.append(lottery_t())
    return all_tickets

def main():
    print("Welcome to Station Rd Corner Store. Next draw tomorrow.")
    num_of_t=int(input("How many lottery tickets are you buying today? >> "))
    print("Here are your tickets, that will be £{}.".format(num_of_t*2))
    my_tickets=generate_tickets(num_of_t)
    for ticket in my_tickets:
        print(ticket)

main()
