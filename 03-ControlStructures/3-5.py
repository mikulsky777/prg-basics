month = int(input('Enter month number (1..12): '))

if month==1 or month==3 or month==5 or month==7 or month==9 or month==11 :
    days = 31
elif month==4 or month==6 or month==8 or month==10 or month==12 :
    days = 30
elif month==2:
    days = 28
else:
    print('Wrong number')
    days = 0

print(f'Month {month} has {days} days')