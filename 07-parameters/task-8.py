# Task 8
# Press the 'Run File' menu button to execute

row=["","",""] #blank row
board=[row[:], row[:], row[:]] #insert copies of a row as items in board, the nested list
n_turns=1
players=["0","x"]

def intro():
    print("Welcome to my python noughts and crosses".upper())
    print("play rows 0 to 2, columns 0 to 2".upper())
    print("playing occupied cell loses a turn".upper())
    print("entering invalid coordinates loses a game".upper())
    print("*"*20)
    
def show():
    for r in board:
        print(r)

def play(type):
    pos=input(pl.upper()+" enter row,col separated by comma, e.g. 1,2 >> ") .split(',')
    try:
        pr= int(pos[0])
        pc= int(pos[1])
    except:
        end_game(players[(n_turns+1)%2])
    else:
        if pr not in range(0,3) or pc not in range(0,3):
            end_game(players[(n_turns+1)%2])
        else:
            if board[pr][pc]=="":
                board[pr][pc]=type
            else:
                print("Position occupied, you miss a turn")

def g_over():
    r0= "" not in board[0]
    r1= "" not in board[1]
    r2 ="" not in board[2]
    return (r0 and r1 and r2)


def end_game(char):
    print(pl,"lost!")
    for rr in range(0,3):
        for cc in range(0,3):
            board[rr][cc]=char

#main part of the program
intro()
show()
while not g_over():
    pl=players[n_turns%2]
    play(pl)
    show()
    n_turns+=1

print('game over!'.upper())