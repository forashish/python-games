import random

print('Welcome to the number gussing game')
myName = input('Enter your name: ')
print(f'Hello {myName}. Let\'s play...')
print('Guess a numnumber between 1 to 10. You will be given only 5 attempts. All the best!')


num = random.randint(1, 10)

for i in range(5):
    guess = input('Enter your guess: ')
    guess = int(guess)

    if guess > num:
        print('Your guess is greater. Try again')

    if guess < num:
        print('Your guess is lower. Try again')

    if guess == num:
        print(f'Congratulations. You have guessed the right number is {i + 1} attempts')
        break

if guess != num:
    print(f'You lost. The correct number was {num}')

