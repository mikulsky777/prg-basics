import math
circumreference = int(input('Enter tree circumference in cm: '))

diameter = circumreference / math.pi
can_cut = diameter > 50
print(f'Tree can be cut down: {can_cut}')