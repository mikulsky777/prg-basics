failed_attempts = 0
pin_code = 2345


while True:
    user_input = int(input("Enter the PIN code: "))
    if user_input != pin_code:
        print(f'Incorrect...')
        failed_attempts += 1
    if failed_attempts >= 3:
        print(f'Sorry, your payment card has been blocked')
        break
    if user_input == pin_code:
        print(f'Login correct')
        break