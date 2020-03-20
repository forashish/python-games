import random

def inputPlayerLetter():
    print('Do you want to be X or O?')
    letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def drawBoard(board):
    print(f'{board[7]}|{board[8]}|{board[9]}')
    print('-+-+-')
    print(f'{board[4]}|{board[5]}|{board[6]}')
    print('-+-+-')
    print(f'{board[1]}|{board[2]}|{board[3]}')

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(board, letter):
    return((board[1] == letter and board[2] == letter and board[3] == letter) or
          (board[4] == letter and board[5] == letter and board[6] == letter) or
          (board[7] == letter and board[8] == letter and board[9] == letter) or
          (board[1] == letter and board[4] == letter and board[7] == letter) or
          (board[2] == letter and board[5] == letter and board[8] == letter) or
          (board[3] == letter and board[6] == letter and board[9] == letter) or
          (board[1] == letter and board[5] == letter and board[9] == letter) or
          (board[7] == letter and board[5] == letter and board[3] == letter))

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

def getBoardCopy(board):
    #Used by computer only. To examin winning cases of computer or player
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def chooseRandomMoveFromList(board, moveList):
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # First check if computer can win in next move
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i
            
    #Check if the player could win on their next move and block them       
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i
            
    #Try to take one of the corners, if they are free
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    #Try to take the center, if it is free
    if isSpaceFree(board, 5):
        return 5

    #Move on one of the sides
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


print('*** TIC-TAC-TOE ***')
print()
theBoard = [' '] * 10
playerLetter, computerLetter = inputPlayerLetter()
turn = whoGoesFirst()
print(f'The {turn} will go first')
gameIsPlaying = True

while gameIsPlaying:
    if turn == 'player':
        drawBoard(theBoard)  # Board is getting draw through this code
        move = getPlayerMove(theBoard)
        makeMove(theBoard, playerLetter, move)
        if isWinner(theBoard, playerLetter):
            drawBoard(theBoard)
            print('Hooray! You have won the game')
            gameIsPlaying = False
        else:
            if isBoardFull(theBoard):
                drawBoard(theBoard)
                print('the ganme is a tie')
                break
            else:                
                turn = 'computer'
    else:
        move = getComputerMove(theBoard, computerLetter)
        makeMove(theBoard, computerLetter, move)

        if isWinner(theBoard, computerLetter):
            drawBoard(theBoard)
            print('The computer has beaten you! You lose.')
            gameIsPlaying = False
        else:
            if isBoardFull(theBoard):
                drawBoard(theBoard)
                print('the ganme is a tie')
                break
            else:
                turn = 'player'

    #print('Do you want to play again?')
    #if not input().lower().startswith('y'):
    #    break
    
