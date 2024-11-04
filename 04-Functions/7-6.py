def f(binary_number):
    counter = 0
    for each in binary_number:
        if each != "1" and each != "0":
            counter += 1
    if counter > 0:
        return False
    else:
        return True

print(f("101101"))