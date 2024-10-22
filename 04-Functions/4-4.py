def sum_digits(number):
    total = 0
    absolute = abs(number)
    int_str = str(absolute)
    for char in int_str:
        total += int(char)
    return total

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')