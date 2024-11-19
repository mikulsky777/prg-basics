def read_from_file(name):
   with open(name, 'r') as file:
      content = file.read()
   return content

file_content = read_from_file('car_park.txt')

file_lines = file_content.splitlines()

total = 0
for line in file_lines:
   total += int(line)

print('Total cars parked:', total)