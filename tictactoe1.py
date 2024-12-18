import random

def disp_board(board):
    # 'board' is a list of 10 strings representing the board 
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    
def inputPlayerLetter():
    #Let the player type which letter they want to be first
    #Returns a list with the player's choice and computer choice as 1st and 2nd
    
    letter=''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    
    # while (letter=='X' or letter == 'O'):
    #     print('What do you want to choose to play again ?')
    #     letter=input().upper()
        
    if letter == 'X':
        return ['X','O']
    else:
        return ['O','X']
    
def whoGoesFirst(playerLetter, computerLetter):
    # if random.randint(0,1) == 0:
    #     return 'computer'
    # else:
    #     return 'player'
    # print('Enter who wants to go first? (you or computer)')
    # turn = input().lower()
    
    if playerLetter == 'X' and computerLetter =='O':
        return 'player'
    else:
        return 'computer'

def playAgain():
    print('Do You want to play again? (yes or no)')
    return input().lower().startswith('y')  

def makeMove(board,letter,move):
    board[move] = letter

def isWinner(board,letter):
    # this returns true if the player has won
    return ((board[7]==letter and board[8]==letter and board[9]==letter) or
            (board[4]==letter and board[5]==letter and board[6]==letter) or
            (board[1]==letter and board[2]==letter and board[3]==letter) or
            (board[4]==letter and board[7]==letter and board[1]==letter) or 
            (board[8]==letter and board[5]==letter and board[2]==letter) or
            (board[9]==letter and board[3]==letter and board[6]==letter) or
            (board[7]==letter and board[5]==letter and board[3]==letter) or
            (board[9]==letter and board[5]==letter and board[1]==letter))


def getBoardCopy(board):
    dupeboard = []
    
    for i in board:
        dupeboard.append(i)
    
    return dupeboard

def isSpaceFree(board,move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,  int(move)):
        print('What is the next move ? (1-9)')
        move = input()
    return int(move)

def chooseRandomMove(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
        
    #Algorithm for tictoctoe AI
    #First we check if we can win in next win
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
            
    #Check if the player could win on their next move and block them
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
            
    # Try to take one of the corners, if they are free.
    move = chooseRandomMove(board, [1,3,7,9])
    if move!=None:
        return move
    
    #try to take the center
    if isSpaceFree(board, 5):
        return 5
    
    #Move on one of the sides
    return chooseRandomMove(board, [2,4,6,8])

def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board, i):
            return False
    return True

# driver code
def gamePlay():
    print('Welcome to Tic Tac Toe !!')
    while True:
        #reset the board
        theBoard = [' ']*10
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst(playerLetter, computerLetter)
        print('The ' + turn+' will go first.')
        gameIsPlaying = True
        
        while gameIsPlaying:
            if turn=='player':
                #player's turn
                disp_board(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)
                
                if isWinner(theBoard, playerLetter):
                    disp_board(theBoard)
                    print('Congratulations! You have won the game.:>')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        disp_board(theBoard)
                        print('The game is a tie')
                        break
                    else:
                        turn = 'computer'
                        
            else:
                # Computer's turn
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)
                
                if isWinner(theBoard, computerLetter):
                    disp_board(theBoard)
                    print('The Computer has beaten you ! You lose. :)')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        disp_board(theBoard)
                        print('The game is a tie')
                        break
                    else:
                        turn = 'player'
        if not playAgain():
            break
        

                    
gamePlay()
            