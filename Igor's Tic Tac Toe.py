#!/usr/bin/env python
# coding: utf-8


def display_board(board):
    print(f'   |   |   \n {board[7]} | {board[8]} | {board[9]} \n___|___|___\n   |   |   \n {board[4]} | {board[5]} | {board[6]} \n___|___|___\n   |   |   \n {board[1]} | {board[2]} | {board[3]} \n   |   |   ')


def askmove():
    move = int(input(f'{activeplayer}, please enter a number: '))
    if move < 1 or move > 9:
        print("Number out of range, try again.")
        askmove()
        
    elif board[move] != " ":
        print("This spot is taken, try again.")
        askmove()
    
    elif activeplayer == "Player One":
        board[move] = p1symbol
        
    elif activeplayer == "Player Two":
        board[move] = p2symbol
    


p1symbol = ''
board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
activeplayer = "Player One"
gameon = True  

while gameon == True:

    while p1symbol.lower() != 'o' and  p1symbol.lower() != 'x':
        p1symbol = input('Player One, which symbol do you want to play? X or O? ').lower()
        if p1symbol == 'o':
            print("Alright, so Player One plays O, Player Two plays X.")
            p2symbol = 'x'
        elif p1symbol == 'x':
            print("Alright, so Player One plays X, Player Two plays O.")
            p2symbol = 'o'




    askmove()

    if activeplayer == "Player One":
        activeplayer = "Player Two"
    elif activeplayer == "Player Two":
        activeplayer = "Player One"
    
    display_board(board)
    
    if p1symbol == board[1] == board[5] == board[9] or p1symbol == board[3] == board[5] == board[7] or p1symbol == board[3] == board[6] == board[9] or p1symbol == board[2] == board[5] == board[8] or p1symbol == board[1] == board[4] == board[7] or p1symbol == board[1] == board[2] == board[3] or p1symbol == board[4] == board[5] == board[6] or p1symbol == board[7] == board[8] == board[9]:
        print("Congratulations Player One, you won!")
        gameon = False
        
        
    if p2symbol == board[1] == board[5] == board[9] or p2symbol == board[3] == board[5] == board[7] or p2symbol == board[3] == board[6] == board[9] or p2symbol == board[2] == board[5] == board[8] or p2symbol == board[1] == board[4] == board[7] or p2symbol == board[1] == board[2] == board[3] or p2symbol == board[4] == board[5] == board[6] or p2symbol == board[7] == board[8] == board[9]:
        print("Congratulations Player Two, you won!")
        gameon = False
        
    
    if " " not in board:
        print('The game is tied!')
        gameon = False 
        