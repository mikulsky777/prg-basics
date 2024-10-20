balance = 5000
pin = 1234
login = False

entered_pin = input('To log in, enter your PIN: ')

if entered_pin.isdigit():
    if int(entered_pin) == pin:
        login = True
        print("Login successful!")
    else:
        print('Wrong PIN.')
else:
    print('The PIN must contain only digits.')

while login:
    interaction = input('What do you want to do: deposit(d), withdraw(w), check balance(cb), check pin(cp), change pin(cngp) or exit(e): ')
    
    if interaction == 'd':
        add = int(input('How much money do you want to deposit: '))
        balance += add
        print(f'Added {add} money to your account. Your new balance is {balance}.')
    
    elif interaction == 'w':
        minus = int(input('How much money do you want to withdraw: '))
        if minus > balance:
            print('You don’t have that much money.')
        elif minus > 0:
            balance -= minus
            print(f'Withdrawn {minus} money from your account. Your new balance is {balance}.')
        else:
            print('Invalid amount entered.')
    
    elif interaction == 'cb':
        print(f'Your current balance is {balance}.')
    
    elif interaction == 'e':
        print('Exiting the program. Goodbye!')
        break

    elif interaction == 'cp':
        print(f'Your PIN is {pin}')

    elif interaction =='cngp':
        newpin = int(input('Enter your new PIN: '))
        newpin = pin
    
    else:
        print('Invalid input, please try again.')
