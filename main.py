from random import choice

Game = ['R', 'P', 'S']
wins = 0
Tie = 0
count={'PLAYER':wins, 'CPU':wins}

def Playerwin():
  global wins
  wins +=1
  grader={'PLAYER':wins}
  count.update(grader)
  print(count)

def Cpuwin():
  global wins
  wins +=1
  grader={ 'CPU':wins}
  count.update(grader)
  print(count)

def gametie():
 global Tie
 Tie +=1
 print ('Tie', Tie)
 

def Begin():
    GameRules()

def GameRules():
    #PRINTS THE NECCESSARY GAME DETAILS 
    print('PLAY EITHER \n \'R FOR ROCK,\' \n \'S FOR SCISSOR,\' \n \'P FOR PAPER\' ')
    GameMoves()

def GameMoves():
    #PRINTS MOVES 
    PLAYER = input('PICK AN OPTION \"R\", \"P\", \"S\"  \n').upper()
    CPU = choice(Game)
    print('PLAYER {} : CPU {} \n'.format(PLAYER, CPU))
    Gamechecker(PLAYER, CPU)

def Gamechecker(PLAYER, CPU):
    #CHECKS IF THEREv iS A WINNER
    if PLAYER==CPU:
      print('GAME TIE')
      gametie()
      GameMoves()
      

    elif (PLAYER == 'P' and CPU== 'S'):
      print('SCISSOR beats PAPER')
      Cpuwin()
      print('CPU WINS')
      
    elif (PLAYER == 'S' and CPU== 'P'):
      print('SCISSOR beats PAPER')
      Playerwin()
      print('PLAYER WINS')
      

    elif (PLAYER == 'S' and CPU== 'R'):
      print('ROCK beats SCISSOR')
      Cpuwin()
      print('CPU WINS')
      
    elif (PLAYER == 'R' and CPU == 'S'):
      print('ROCK beats SCISSORS')
      Playerwin()
      print('PLAYER WINS')
      
    elif (PLAYER == 'P' and CPU== 'R'):
      print('PAPER beats ROCK')
      Playerwin()
      print('PLAYER WINS')
      
    elif (PLAYER == 'R' and CPU== 'P'):
      print('PAPER beats ROCK')
      Cpuwin()
      
      print('CPU WINS')
      
try:
  print('\n ********** WELCOME 2 (ROCK, PAPER, SCISSORS) GAME **********')
  x= input('START GAME? [YES|NO] \n').upper()
  if x == 'Y' or x =='YES':
      Begin()
  else:
    print('######### Game Ended ######### \n')
    print('TOTAL SCORE:', count)
 
      
except:
  print('invalid input ')
finally:
  pass

