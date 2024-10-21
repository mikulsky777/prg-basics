age = int(input('Enter your dogs age in human years: '))
real_age = 1

if age > 2:
    real_age = (10.5*2) + (age-2)*4
    print(f'The dogs age in dogs years is {real_age}')
elif age <= 2:
    real_age = (10.5*2)
    print(f'The dogs age in dogs years is {real_age}')