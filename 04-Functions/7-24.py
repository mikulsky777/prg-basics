def f(x, y):
    sum = 0
    for number in range(x, y+1):
        if number % 3 == 0 and number % 2 == 0 and number % 4 != 0:
            sum += number
    return sum

print(f(10,30))