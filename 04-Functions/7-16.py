def f(palindrome):
    backwards = palindrome[::-1]
    if backwards == palindrome:
        return True
    else:
        return False
print(f("book"))