import random
computer = random.randint(1,6)
you = int(input('Enter a number between 1 and 6: '))
same = computer == you
print(f'You won: {same}')
print(f'The number was: {computer}')