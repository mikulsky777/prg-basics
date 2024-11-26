def f(product_code):
    characters = list(product_code)
    int_characters = list(map(int, characters))

    code = int_characters[0]+int_characters[1]+int_characters[2]
    if code % 7 == int_characters[3]:
        return True
    else:
        return False

print(f("7071"))