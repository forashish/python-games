import random
import time

def displayIntro():
    print('''You are in a land full of dragons. In front of you,
    you see two caves. In one cave, the dragon is friendly
    and will share his treasure with you. The other dragon
    is greedy and hungry, and will eat you on sight.''')

print()
    
def chooseCave():
    chosenCave = input('Enter your chosen cave. Either 1 or 2: ')
    while True:
        if chosenCave == '1' or chosenCave == '2':
            break
        else:
            chosenCave = input('Wrong answer. Enter either 1 or 2:')
    return chosenCave
    
def processCave(cv):
    num = random.randint(1, 2)

    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)
    
    print(f'cv is {cv} and num is {num}')

    if int(cv) == num:
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')

playAgain = 'y'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    cave = chooseCave()
    processCave(cave)
    playAgain = input('Do you want yto play again? (yes/no)')
     
