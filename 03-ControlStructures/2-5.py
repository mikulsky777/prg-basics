month = int(input('Enter month number (1..12): '))

if month >= 10:
    quarter = 4
elif month >=7 and month <=9:
    quarter = 3
elif month >=4 and month <=6:
    quarter = 2
elif month >=1 and month <=3:
    quarter = 1

print(f'Month {month} is in quarter {quarter}')