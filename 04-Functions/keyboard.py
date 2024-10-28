def input_string(message):
    user_input = input(message)
    return str(user_input)

def input_integer(message):
    user_input = input(message)
    return int(user_input)

def input_real(message):
    user_input = input(message)
    return float(user_input)

def input_boolean(message):
    user_input = input(message)
    if user_input == 'y':
        user_input = True
    elif user_input == 'n':
        user_input = False
    return bool(user_input)