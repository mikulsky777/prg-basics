amount = int(input('Enter amount of money: '))
pln_5 = 0
pln_2 = 0
pln_1 = 0

pln_5 = amount // 5
amount %= 5

pln_2 = amount // 2
amount %= 2

pln_1 = amount

print(f'5 PLN coins: {pln_5}')
print(f'2 PLN coins: {pln_2}')
print(f'1 PLN coins: {pln_1}')