def read_from_file(name):
   with open(name, 'r') as file:
      content = file.read()
   return content

file_content = read_from_file('pets.txt')

print(file_content)

total_words = file_content.split()

count = 0
for each in total_words:
   count += 1

print(count)
