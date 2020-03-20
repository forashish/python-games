import random

hangmanPics = ['''
    +---+
        |
        |
        |
       ===''','''
    +---+
    O   |
        |
        |
       ===''','''
    +---+
    O   |
    |   |
        |
       ===''','''
    +---+
    O   |
   /|   |
        |
       ===''','''
    +---+
    O   |
   /|\  |
        |
       ===''','''
    +---+
    O   |
   /|\  |
   /    |
       ===''','''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
    wordIndex = random.randint(0, (len(wordList)-1))
    randomWord = wordList[wordIndex]
    return randomWord

def displayBoard(missedLetters, correctLetters, secretWord):
    print(hangmanPics[len(missedLetters)])
    print()

    print('Missed letters: ', end = ' ')
    for letter in missedLetters:
        print(letter, end = ' ')
    print()
    blanks = '-' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for i in blanks:
        print(i, end = ' ')
    print()

def getGuess(alreadyGussed):
    while True:
        print('Guess a letter')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Enter a single letter')
        elif guess in alreadyGussed:
            print('You have already gussed this letter. Choose a different letter')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Guess a LETTER only!')
        else:
            return guess

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('*** H A N G M A N ***')
missedLetters = ''
correctLetters = ''
gameIsDone = False
secretWord = getRandomWord(words)
print(secretWord)

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print(f'Yes! The secret word is {secretWord}! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        print(f'lenght of missedLetters is {len(missedLetters)}')
        if len(missedLetters) == len(hangmanPics) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print(f'You have run out of gusses\nAfter {str(len(missedLetters))} missed gusses and {str(len(correctLetters))} correct gusses.\nThe word was {secretWord}')
            gameIsDone = True
        
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
            print(secretWord)
        else:
            break
