def read_from_file(name):
    with open(name, 'r') as file:
        content = file.read()
    return content

file_content = read_from_file('it_company.csv')

file_lines = file_content.splitlines()

for line in file_lines:
    if "Software Engineer" in line:
        print(line)