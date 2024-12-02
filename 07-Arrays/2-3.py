monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
total = 0
for row in monthly_expenses:
    for each in row:
        total += each

food = 0
for each in monthly_expenses:
    food += each[0]

transport = 0
for each in monthly_expenses:
    transport += each[1]

utilities = 0
for each in monthly_expenses:
    utilities += each[2]

week1 = 0
for each in monthly_expenses[0]:
    week1 += each

week2 = 0
for each in monthly_expenses[1]:
    week2 += each

week3 = 0
for each in monthly_expenses[2]:
    week3 += each

week4 = 0
for each in monthly_expenses[3]:
    week4 += each

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',food)
print('Transport:',transport)
print('Utilities:',utilities)
print('Week 1:',week1)
print('Week 2:',week2)
print('Week 3:',week3)
print('Week 4:',week4)
print('---------------')
print('TOTAL', total)