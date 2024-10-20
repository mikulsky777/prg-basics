import time
number = int(input('Enter your number: '))

while number > 0:
    if number > 5:
        print(number)
        time.sleep(1)
        number -= 1
    elif number == 5:
        print('five')
        time.sleep(1)
        number -= 1
    elif number == 4:
        print('four')
        time.sleep(1)
        number -= 1
    elif number == 3:
        print('three')
        time.sleep(1)
        number -= 1
    elif number == 2:
        print('two')
        time.sleep(1)
        number -= 1
    elif number == 1:
        print('one')
        break
    else:
        print('wrong number')