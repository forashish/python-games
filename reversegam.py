import random
import sys
width = 8
height = 8

def enterPlayerTitle():
    title = ''
    while not (title == 'X' or title == 'O'):
        print('Do you want to become "X" or "O"')
        title = input().upper()
        if title == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def getNewBoard():
    board = []
    for i in range(width):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board

def isOnBoard(x, y):
    return (x >= 0 and x <= (width - 1)) or (y >= 0 and y <= (height -1)) 

def isValidMove(board, title, xstart, ystart):
    #Return False if the player's move on space xstart, ystart is invalid.
    #If it is a valid move, return a list of spaces that would become the player's if they made a move here.
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False

    if title == 'X':
        otherTitle = 'O'
    else:
        otherTitle = 'X'

    ## Code Incomplete 
    
    
def getValidMoves(board, title):
    #Return a list of [x,y] lists of valid moves for the given player
    validMoves = []
    for x in range(width):
        for y in range(height):
            if isValidMove(board, title, x, y) != False:
                validMoves.append([x, y])
    return validMoves

def playGame(playerTitle, computerTitle):
    showHints = False
    turn = whoGoesFirst()
    print(f'The {turn} will go first')

    board = getNewBoard()
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'

    while True:
        playerValidMoves = getValidMoves(board, playerTitle)
        computerValidMoves = getValidMoves(board, computerTitle)
    

print('*** R E V E R S E G A M ***')
playerTitle, computerTitle = enterPlayerTitle()

while True:
    finalBoard = playGame(playerTitle, computerTitle)
    break
    
