###
# Reads from file, line by line
#
count = 1
with open('countries.txt', 'r') as file:
    for line in file:
        print( f'{count}. {line}', end="")
        count += 1