first = input('Enter first letter: ')
first = str(first)
last = input('Enter second letter: ')
last = str(last)
first_letter_code = ord(first)
second_letter_code = ord(last)
number_of_letters = second_letter_code - first_letter_code - 1
print(f'Between {first} and {last} is {number_of_letters} letters')