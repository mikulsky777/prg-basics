def f(n):
    list = []
    for each in range(1, n+1):
        each = str(each)
        list.append(each)

    result = "".join(list)
    return result
print(f(4))