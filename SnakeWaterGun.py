
from random import randint as ri

decision = [ #0-rock 1-paper 2-scissor
  [0,1,-1],
  [-1,0,1],
  [1,-1,0]
  #-1 > Lose, 0 > Draw, 1 > Win
]

score = 0

def line():
  print('-='*20+'-')

def clear():
  print('\n'*50)
  line()

def wait():
  input('Press ENTER to continue...')

def game():
  global score
  clear()
  comp = ri(0,2)
  print("Computer has guessed! Its Your Turn :")
  print('0 - Rock \n1 - Paper \n2 - Scissor')
  line()
  user = int(input('Enter your choice here : '))
  
  if user not in (0,1,2):
    line()
    print("The choice you entered is out of range! Please Try again")
    line(); wait(); game()

  result = decision[user][comp]

  clear()
  match result:
    case -1:
      print("You Lost!")
      score -= 2
    case 0:
      print("It's a Draw!")
    case 1:
      print("You Won!")
      score += 5
    case _:
      print("Something went Wrong!")

  print("Your Score is",score)
  line()

  again = input("Do you want to play again?(y/n) : ")
  if again.lower() == 'y': game()  
      
def viewLastScore():
  clear()
  print("Your Score is",score)
  line(); wait()

def menu():
  while True:
    clear()
    print('Experiment no. 10 \nPrince Mathukiya F-58 \n'+'-='*20+'-')
    print("<=-MAIN MENU-=>")
    print("1. Play")
    print("2. View Last Score")
    print("3. Quit Game")
    line()
    ch = int(input('Enter your choice from above : '))
    
    match ch:
      case 1: game()
      case 2: viewLastScore()
      case 3:
        line()
        print("Thank you for playing! Come back soon")
        break
      case _:
        line()
        print("The Entered choice is out of range! please Try again")
        line(); wait(); continue
menu()
