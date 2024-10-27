decimal = int(input("Enter a decimal number: "))
remainders = []

while decimal > 0:
    remainder = decimal % 2
    remainders.append(remainder)
    decimal //= 2

remainders.reverse()
remainders = ''.join(map(str,remainders))
print(remainders)