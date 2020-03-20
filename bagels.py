import random

numDigits = 3
maxGuess = 10

def getSecretNum():
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(numDigits):
        secretNum += str(numbers[i])
    return secretNum

def isOnlyDigits(num):
    if num == '':
        return False
    for i in num:
        if i not in '1 2 3 4 5 6 7 8 9'.split():
            return False
    return True

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Ferni')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        clues.append('Bagals')

    clues.sort()
    return ' '.join(clues)

print(f'I am thinking of a {numDigits} digit number. Try to guess what it is.')
print('The clues I give are...')
print('When I say: That means:')
print('    Bagels: None of the digits is correct.')
print('      Pico: One digit is correct but in the wrong position.')
print('     Fermi: One digit is correct and in the right position.')

while True:
    secretNum = getSecretNum()
    print(f'I have thought up a number. You have {maxGuess} guesses to get it.')

    guessTaken = 1
    while guessTaken <= maxGuess:
        guess = ''
        while len(guess) != numDigits or not isOnlyDigits(guess):
            print(f'Guess {guessTaken}')
            guess = input()

        print(getClues(guess, secretNum))
        guessTaken += 1

        if guessTaken == secretNum:
            break
        if guessTaken > maxGuess:
            print(f'You ran out of guesses. The answer was {secretNum}')

            

