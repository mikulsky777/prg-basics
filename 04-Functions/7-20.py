def f(number1, number2, number3):
    smallest = min(number1, number2, number3)
    biggest = max(number1, number2, number3)

    diff = biggest - smallest
    return diff

print(f(2,12,8))