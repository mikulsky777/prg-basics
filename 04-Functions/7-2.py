import months

choice = int(input('Enter month number: '))

month_name = months.months(choice)

months.months(choice)
print(f'The name of month {choice} is {month_name}')