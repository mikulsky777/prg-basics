def f(password):
    password = str(password)
    if len(password) < 6:
        return False
    
    seen_characters = set()

    for letter in password:
        if letter in seen_characters:
            return False
        seen_characters.add(letter)

    return True

print(f(""))