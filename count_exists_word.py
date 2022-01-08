filename = 'alice.txt'

with open(filename, 'r') as file_obj:
    lines = file_obj.readlines()

contents = ''
for line in lines:
    contents += line

print(contents.lower().count('the '))