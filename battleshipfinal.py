import os
from datetime import datetime
start_game = input("""
                                           |_
                                       ---/ |
                                       ___\_|__
                                      /| o  o |
                       ___           / |______|\          ___
                  ====/___\  ,------,--|------|--.       /___\====
    _________________,|- -|,/---------------------\.____,|- -|,______________
    \                       \. . . . . . . . . . . ./                       /     , 
 ,  \   o           o           o           o           o           o     /    ,   )',    ,     ,(
=)'===\___________________________________________________________________/==="('=='""=='"(=='-'  ',
                            Welcome To Battleship
               <------------------------------------------------->
                Rules:
                The classic battleship game with two phases:
                1. Placement phase: Place your ships on the board.
                First decide the orientation of your ship, then input
                the coordinates.
                The ships can't overlap with eachother.
                There are 5 ships in total:
                1. Carrier: 5 grid
                2. Battleship: 4 grid
                3. Cruiser: 3 grid
                4. Submarine: 3 grid
                5. Destroyer: 2 grid
                --------------------------------------
                2. War phase: The second player will guess the row
                and the column where the ship was placed, 
                if it is a hit, then the player will gain 1 point. 
                The second player got 30 cannonballs.
                If you shoot all of them, then the game is over.
               <-------------------------------------------------> 
                           Press Enter to Continue
""")
def highscore_read():
    with open ("Highscore.txt", "r") as file_handle:
        lines=file_handle.readlines()
        lines="\n".join(lines)
        print(lines)
def highscore_file():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    with open ("Highscore.txt", "a+") as file_handle:
        file_handle.write("\n{0}: \nPlayer      Shots     Score\n{3:<8}     {1:^3}      {2:>3} \n{4:<8}     {5:^3}      {6:>3}\n".format(dt_string,shot1,success1,player1,player2,shot2,success2))
        file_handle.write("--------------------------")
def player_name(player1,player2):
    while True:
        player1=input("player1 type in your name!(Max 8 characters): ")
        if len(player1)>8:
            continue
        else:
            break

    while True:
        player2=input("player2 type in your name!(Max 8 characters): ")
        if len(player2)>8:
            continue
        else:
            break
    return player1,player2
        

def score_board():
    print("----------------------")
    print("|Player    |Shots|Hits|")
    print("|---------------------|")
    print("|{2:<8}  | {0:^3} | {1:>3}| ".format( shot1, success1,player1))
    print("|{2:<8}  | {0:^3} | {1:>3}| ".format( shot2, success2,player2))
    print("-----------------------")


def print_board(board):
    print("     1   2   3   4   5   6   7   8   9   10")
    print("   -----------------------------------------")
    i=1
    for row in board:
        rw=" | ".join(row)
        print(" {0:<2}|".format(i), end="")
        print(" {0} |".format(rw.replace('0',' ')))
        print("   -----------------------------------------")
        i+=1

def shipcheck_u(board,ship1,ship2,n):
    for i in range(1,n+1):
        if  board[ship1-i][ship2-1] == "1":
            print("You can't put your ship here!")
            return 0
        elif board[ship1-(i)][ship2-1] == "1" and i == n:
            print("You can't put your ship here!")
            return 0
        elif board[ship1-(i)][ship2-1] == "0" and i == n:
            return 1
        elif  board[ship1-(i)][ship2-1] == "0":
            continue  

def shipcheck_d(board,ship1,ship2,n):
    for i in range(2,2+n):
        if  board[(ship1-1)+(i-2)][ship2-1] == "1":
            print("You can't put your ship here!")
            return 0
        elif board[(ship1-1)+(i-2)][ship2-1] == "1" and i == n:
            print("You can't put your ship here!")
            return 0
        elif board[(ship1-1)+(i-2)][ship2-1] == "0" and i == n:
            return 1
        elif  board[(ship1-1)+(i-2)][ship2-1] == "0":
            continue

def shipcheck_l(board,ship1,ship2,n):
    for i in range(1,n+1):
        if  board[ship1-1][ship2-i] == "1":
            print("You can't put your ship here!")
            return 0
        elif board[ship1-(1)][ship2-i] == "1" and i == n:
            print("You can't put your ship here!")
            return 0
        elif board[ship1-(1)][ship2-i] == "0" and i == n:
            return 1
        elif  board[ship1-(1)][ship2-i] == "0":
            continue  
            
def shipcheck_r(board,ship1,ship2,n):
    for i in range(2,2+n):
        if  board[ship1-1][(ship2-1)+(i-2)] == "1":
            print("You can't put your ship here!")
            return 0
        elif board[ship1-1][(ship2-1)+(i-2)] == "1" and i == n:
            print("You can't put your ship here!")
            return 0
        elif board[ship1-1][(ship2-1)+(i-2)] == "0" and i == n:
            return 1
        elif  board[ship1-1][(ship2-1)+(i-2)] == "0":
            continue
        
def shipsize(board,ship1,ship2,n,a):
    for i in range(n):
        if a=="d":
            board[ship1-1][ship2-1]="1"
            ship1+=1
        elif a=="u":
            board[ship1-1][ship2-1]="1"
            ship1-=1
        elif a=="l":
            board[ship1-1][ship2-1]="1"
            ship2-=1
        elif a=="r":
            board[ship1-1][ship2-1]="1"
            ship2+=1
    os.system("clear")
    print_board(board)
        

def inputship(player,board,n):
    a=""
    while a is not "u" and a is not "d" and a is not "l" and a is not "r":
        os.system("clear")
        print("{0} is deploying the ships.\n".format(player))
        print_board(board)
        print("The current ship size is:{0}".format(n))
        a=str(input('Which way would you like to deploy your ship?\n up="u" down="d" left="l" right="r" \n(or press "x" to quit): '))
        if a=="x":
            os.system("clear")
            quit()
    
    shipcheck=0
    ship1=-1  
    ship2=-1
    while True:
        try:
            if a=="u":
                while shipcheck==0:
                    ship1=-1
                    ship1=(int(input("Row coordinate: ")))
                    ship2=-1
                    ship2=(int(input("Column coordinate: ")))
                    shipcheck=0
                    if ship1>=n and ship1<=10 and ship2<=10 and ship2>0 :
                        shipcheck=shipcheck_u(board,ship1,ship2,n)
                        if shipcheck==0:
                            continue
                        elif shipcheck==1:
                            break
                break     
            elif a=="d":
                while shipcheck==0:
                    ship1=-1
                    ship1=(int(input("Row coordinate: ")))
                    ship2=-1
                    ship2=(int(input("Column coordinate: ")))
                    shipcheck=0
                    if ship1+n<=11 and ship1>0 and ship2<=10 and ship2>0 :
                        shipcheck=shipcheck_d(board,ship1,ship2,n)
                        if shipcheck==0:
                            continue
                        elif shipcheck==1:
                            break
                break     
            elif a=="l" :
                while shipcheck==0:
                    ship1=-1
                    ship1=(int(input("Row coordinate: ")))
                    ship2=-1
                    ship2=(int(input("Column coordinate: ")))
                    shipcheck=0
                    if ship1<=10 and ship1>0 and ship2>=n and ship2<=10 :
                        shipcheck=shipcheck_l(board,ship1,ship2,n)
                        if shipcheck==0:
                            continue
                        elif shipcheck==1:
                            break
                break     
            elif a=="r":
                while shipcheck==0:
                    ship1=-1
                    ship1=(int(input("Row coordinate: ")))
                    ship2=-1
                    ship2=(int(input("Column coordinate: ")))
                    shipcheck=0
                    if ship1>0 and ship1<=10 and ship2+n<=11 and ship2>0 :
                        shipcheck=shipcheck_r(board,ship1,ship2,n)
                        if shipcheck==0:
                            continue
                        elif shipcheck==1:
                            break
                break     
        except ValueError:
            print("Wrong input! Try again!")
    shipsize(board,ship1,ship2,n,a)
    return board
    
                        #BATTLE PHASE
def battle_phase(shootboard,board,success,shot):

    while True:
        try:
            guess_column = 0
            guess_row = 0
            while guess_row > 10 or guess_row <= 0 :
                guess_row = input("Which row you wanna' shoot?('x'=quit): ")
                if guess_row=="x":
                    os.system("clear")
                    quit()
                else:
                    guess_row = int(guess_row)
                    
            while guess_column > 10 or guess_column <= 0 :
                guess_column = input("Which column you wanna' shoot?('x'=quit): ")
                if guess_column=="x":
                    os.system("clear")
                    quit()
                else:
                    guess_column=int(guess_column)
            if shootboard[guess_row-1][guess_column-1]=="x" or shootboard[guess_row-1][guess_column-1]=="#":
                print("You already shot there!")
                continue
            else:
                break
                


            break
        except (ValueError):
            print("Wrong input!")
    os.system("clear")
    if (board[guess_row-1][guess_column-1] == "1"):
        success=success+1
        shot=shot+1
        board[guess_row-1][guess_column-1] = "x"
        shootboard[guess_row-1][guess_column-1]= "#"
        print_board(shootboard)
        print("Nice shot!")
        input("Press enter to advance!")
        os.system("clear")
        
    else: 
        shot +=1
        shootboard[guess_row-1][guess_column-1]= "x"
        print_board(shootboard)
        print("You missed it!")
        input("Press enter to advance!")
        os.system("clear")
    
    return success, shot

while True:
    os.system("clear")
    board1=[]
    for i in range(10):
        board1.append(["0"]*10)
    ship1=-1  
    ship2=-1
    player1=""
    player2=""
    player1,player2=player_name(player1,player2)
    inputship(player1,board1,5)
    inputship(player1,board1,4)
    for i in range(2):
        inputship(player1,board1,3)
    inputship(player1,board1, 2)
    cont = input("Press a button to advance.")
    os.system("clear")
    #Second player prep phase
    board2=[]
    for i in range(10):
        board2.append(["0"]*10)
    inputship(player2,board2,5)
    inputship(player2,board2,4)
    for i in range(2):
        inputship(player2,board2,3)
    inputship(player2,board2, 2)
    cont_battle = input("Press a button to advance.")
    os.system("clear")
    #Battlephase 
    shootboard1=[]
    for i in range(10):
        shootboard1.append(["0"]*10)
    shootboard2=[]
    for i in range(10):
        shootboard2.append(["0"]*10)
    success1=0
    shot1=0
    success2=0
    shot2=0
    while  True: 
        print_board(shootboard1)
        print("{0} is attacking:".format(player1))
        (success1, shot1) = battle_phase(shootboard1,board2,success1,shot1)
        if success1==1:
            break
        else:
            pass
        print_board(shootboard2)
        print("{0} is attacking: ".format(player2))
        (success2, shot2) = battle_phase(shootboard2,board1,success2,shot2)
        if success2==1:
            break
        else:
            pass
    if success1==1:
        print("{0} won the game.".format(player1))
        highscore_file()
        score_board()
    elif success2==1:
        print("{0} won the game.".format(player2))
        highscore_file()
        score_board()
    hs = input("Do you want to see the match history? y/n")
    if hs == "y" or hs == "Y":
        highscore_read()
    else:
        continue
    
    playagain=""
    while playagain!="y" or playagain!="Y" or playagain!="n" or playagain!="N":
        playagain = input("Do you want to play again?  y/n:")
        if playagain == "y" or playagain == "Y":
            break
        elif playagain == "n" or playagain == "N" :
            os.system("clear")
            quit()