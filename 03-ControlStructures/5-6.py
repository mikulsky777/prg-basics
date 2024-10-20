N = 10
sum_even = 0
number = 1

while number <= N:
    if number % 2 == 0:
        sum_even += number
    number += 1


print(f"The sum of even numbers from 1 to {N} is: {sum_even}")