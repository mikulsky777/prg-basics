def f(x, y):
    counter = 0

    start = min(x, y)
    end = max(x, y)
    

    for num in range(start, end + 1):
        if num < 0 and num % 2 == 0:
            counter += 1
    
    return counter

print(f(-7,8))