number = int(input('Enter your number: '))

if number > 0:
    print(f'Your number {number} is positive')
elif number == 0:
    print(f'Your number {number} is zero')
elif number < 0:
    print(f'Your number {number} is negative')
else:
    print(f'You entered wrong number')