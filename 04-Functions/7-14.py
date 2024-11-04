def f(detector):
    counter = 0
    for each in detector:
        if each == '+':
            counter += 1
        elif each == "-":
            counter -= 1
        if counter >= 3:
            return True
    return False


print(f("+-++-++-+---"))