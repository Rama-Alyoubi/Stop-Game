#NAMES
#Rama Mohammed Alyoubi - 2110112
#Rimas Alshehri – 2110240
#Ramah Alharbi - 2110173
#Asmaa mahdi - 2111900
#the game board: three rocks for player 'M' and three for bot 'W'
board={1:'M',2:'M',3:'M',
      4:' ',5:' ',6:' ',
      7:'W',8:'W',9:'W'}
#to reset the board for another round
def setBoard(board):
    board={1:'M',2:'M',3:'M',
      4:' ',5:' ',6:' ',
      7:'W',8:'W',9:'W'}
    return board
#to display the board to the user every time an entry happend
def printBoard(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-+-+-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-+-+-')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('\n')
#to check if there is a space to play for the position sent in board 
def spaceIsFree(position):
    if (board[position]==' '):
        return True
    else:
        return False
#to ckeck if the player wins the round   
def doesPlayerWin():
    if (board[4]==board[5] and board[4]==board[6] and board[4] =='M'):
        return True
    elif (board[7]==board[8] and board[7]==board[9] and board[7] =='M'):
        return True
    elif (board[1]==board[5] and board[1]==board[9] and board[1] =='M'):
        return True
    elif (board[3]==board[5] and board[3]==board[7] and board[3] =='M'):
        return True
    elif (board[1]==board[4] and board[1]==board[7] and board[1] =='M'):
        return True
    elif (board[2]==board[5] and board[2]==board[8] and board[2] =='M'):
        return True
    elif (board[3]==board[6] and board[3]==board[9] and board[3] =='M'):
        return True
    else:
        return False
#to check if bot wins the round
def doesBotWin():
    if (board[1]==board[2] and board[1]==board[3] and board[1] =='W'):
        return True
    elif (board[4]==board[5] and board[4]==board[6] and board[4] =='W'):
        return True
    elif (board[1]==board[5] and board[1]==board[9] and board[1] =='W'):
        return True
    elif (board[3]==board[5] and board[3]==board[7] and board[3] =='W'):
        return True
    elif (board[1]==board[4] and board[1]==board[7] and board[1] =='W'):
        return True
    elif (board[2]==board[5] and board[2]==board[8] and board[2] =='W'):
        return True
    elif (board[3]==board[6] and board[3]==board[9] and board[3] =='W'):
        return True
    else:
        return False
#to check who wins the round by passing the letter
def chkMarkForWin(mark):

    if ((board[1]==board[2] and board[1]==board[3] and board[1] == mark)and mark!='M'):
        #Not acceptable for the player to win in their initial position.
        return True
    elif (board[4]==board[5] and board[4]==board[6] and board[4] == mark):
        return True
    elif ((board[7]==board[8] and board[7]==board[9] and board[7] == mark)and mark!='W'):
        #Not acceptable for the bot to win in their initial position.
        return True
    elif (board[1]==board[5] and board[1]==board[9] and board[1] == mark):
        return True
    elif (board[3]==board[5] and board[3]==board[7] and board[3] == mark):
        return True
    elif (board[1]==board[4] and board[1]==board[7] and board[1] == mark):
        return True
    elif (board[2]==board[5] and board[2]==board[8] and board[2] == mark):
        return True
    elif (board[3]==board[6] and board[3]==board[9] and board[3] == mark):
        return True
    else:
        return False
#to check if the movement of the rock can be done in on step with near positins only not at random positions
def isPossible(init_position,position):
    if(init_position==1 and position==2):
        return True
    elif(init_position==1 and position==4):
        return True
    elif(init_position==2 and position==1):
        return True
    elif(init_position==2 and position==5):
        return True
    elif(init_position==2 and position==3):
        return True
    elif(init_position==3 and position==2):
        return True
    elif(init_position==3 and position==6):
        return True
    elif(init_position==4 and position==1):
        return True
    elif(init_position==4 and position==5):
        return True
    elif(init_position==4 and position==7):
        return True
    elif(init_position==5and position==2):
        return True
    elif(init_position==5and position==4):
        return True
    elif(init_position==5and position==6):
        return True
    elif(init_position==5and position==8):
        return True
    elif(init_position==6and position==3):
        return True
    elif(init_position==6and position==5):
        return True
    elif(init_position==6and position==9):
        return True
    elif(init_position==7and position==4):
        return True
    elif(init_position==7and position==8):
        return True
    elif(init_position==8and position==5):
        return True
    elif(init_position==8and position==7):
        return True
    elif(init_position==8and position==9):
        return True
    elif(init_position==9and position==6):
        return True
    elif(init_position==9and position==8):
        return True
    else:
        return False
#to find the previous position for the bot new position 
#previous position for the player was given by the user what about the bot? and therefore this method did the job
def possibleIndex(board,position):
    if(position==1):
        if(board[2]=='W'):
            return 2
        elif(board[4]=='W'):
            return 4
    elif(position==2):
        if(board[1]=='W'):
            return 1
        elif(board[3]=='W'):
            return 3
        elif(board[5]=='W'):
            return 5
        
    elif(position==3):
        if(board[2]=='W'):
            return 2
        elif(board[6]=='W'):
            return 6
        
    elif(position==4):
        if(board[1]=='W'):
            return 1
        elif(board[5]=='W'):
            return 5
        elif(board[7]=='W'):
            return 7
        
    elif(position==5):
        if(board[2]=='W'):
            return 2
        elif(board[4]=='W'):
            return 4
        elif(board[6]=='W'):
            return 6
        elif(board[8]=='W'):
            return 8

    elif(position==6):
        if(board[3]=='W'):
            return 3
        elif(board[5]=='W'):
            return 5
        elif(board[9]=='W'):
            return 9

    elif(position==7):
        if(board[4]=='W'):
            return 4
        elif(board[8]=='W'):
            return 8
        
    elif(position==8):
        if(board[5]=='W'):
            return 5
        elif(board[7]=='W'):
            return 7
        elif(board[9]=='W'):
            return 9
        
    elif(position==9):
        if(board[6]=='W'):
            return 6
        elif(board[8]=='W'):
            return 8
    else:
        return -1
#for easy insert with validation steps 
def insertLetter(letter,init_position,position):
    #to make sure to insert in an empty position, the postion you choose can be possible to insert and the new position does not match the pre one
    if (spaceIsFree(position)and isPossible(init_position,position)and (init_position!=position)):
        while(letter!=board[init_position]):#to make sure if the previous position matchs the letter 
            print('Position taken, please pick a different position.')
            #to make sure the user inters an integer between 1 and 9
            while True:
                    try:
                        init_position=int(input('Enter current position: '))
                        position=int(input('Enter new position: '))
                    except ValueError:
                        print("Please enter a valid integer 1-10")
                        continue
                    if (init_position >= 1 and init_position <= 9)and (position >= 1 and position <= 9)and (init_position!=position):
                        break
                    else:
                        print('Invalid input, please choose number between 1-9')

        #previous positin need to be empty first for the letter to become one step only
        board[init_position]=' '
        board[position]=letter 
        printBoard(board) 

        #check if there is a winner in current round
        if (chkMarkForWin(letter)): 
            if (letter=='M'): 
                print('You win this round!') 
            else: 
                print('bot wins this round!') 
        return 

    else: 
        print('Invalid input, please try again')
        while True:
                try:
                    init_position=int(input('Enter current position: '))
                    position=int(input('Enter new position: '))
                except ValueError:
                    print("Please enter a valid integer 1-10")
                    continue
                if (init_position >= 1 and init_position <= 9)and (position >= 1 and position <= 9)and (init_position!=position):
                    break

                else:
                    print('Invalid input, please choose number between 1-9')

        insertLetter(letter,init_position,position) 
        return
player ='M' #user letter
bot ='W' #computer letter
#diplay messages for the user to play 
def playerMove():
        #validation loop
        while True:
                try:
                    init_position=int(input('Enter current position: '))
                    position=int(input('Enter new position: '))
                except ValueError:
                    print("Please enter a valid integer 1-10")
                    continue
                if init_position >= 1 and init_position <= 9:
                    break
                if position >= 1 and position <= 9:
                    break
                else:
                    print('Invalid input, please choose number between 1-9')

        insertLetter(player,init_position,position) 
#method for the the computer to play
def compMove():
    bestScore=-1000
    bestMove=0
    x=-1
    #take a copy version of the board
    board2=board.copy()
    for key in board2.keys():
        #i represent the pre postion of the key which could be the bot move 
        i=possibleIndex(board,key)
        if(spaceIsFree(key) and isPossible(i,key)):
            if(i!=-1):
                board[key]=bot
                board[i]=' '
                score=minimax(board ,0, False)#calling the minmax method to find the move with the best score (here we minimize the player move)
                board[key]=' '
                board[i]=bot
                if(score > bestScore):
                    bestScore = score
                    bestMove = key
                    #x represent the pre postion of the assured bot move
                    x=possibleIndex(board,bestMove)
            
    insertLetter(bot,x,bestMove)                
    return
#a recursive minmax method helped the bot to take the most potentially step to win
def minimax(board, depth, isMaximizing): 
    if (chkMarkForWin(bot)):
         return 1 
    elif (chkMarkForWin(player)): 
        return -1  
    else:
        return 0
    #maximize the bot move
    if isMaximizing: 
        bestScore = -1000 

        for key in board.keys(): 
            i=possibleIndex(board,key)
            if(isPossible(i,key)):
                if (board [key]==' '): 
                    board [i]=' '
                    board [key]=bot
                    score = minimax(board, 0, False)#recursive step
                    #to return the board as it was 
                    board [key] =' '
                    board [i]=bot
                    if (score>bestScore): 
                        bestScore = score 
        return bestScore 
    #minimize the player move
    else: 
        bestScore = 1000
        
        for key in board.keys(): 
            i=possibleIndex(board,key)
            if(isPossible(i,key)):
                if (board[key]==' '): 
                    board[i]=' '
                    board[key]=player
                    score = minimax (board, 0, True)#recursive step
                    #to return the board as it was 
                    board [key]=' '
                    board [i]=player
                    if (score<bestScore): 
                        bestScore = score 
        return bestScore

#counter for each player to find out who is the winner in 3 round
countP=0
countB=0
#to stop the loop
flag=0
while (flag==0):
    printBoard(board)
    #loop until either player or bot win
    while not doesPlayerWin()and not doesBotWin():
        playerMove()
   
        if(not doesBotWin()and not doesPlayerWin()):
            compMove()
    if(doesPlayerWin()):
        countP+=1
    if(doesBotWin()):
        countB+=1
    board=setBoard(board)
    if(countP==3):
        print('You win the game!') 
        flag=1
    if(countB==3):
        print('bot wins the game!') 
        flag=1

