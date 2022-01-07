filename = 'd:\Python\Crash_course\Files_and_Exceptions\\text_files\\pi_million_digits.txt'

with open(filename) as file_obj:
    lines = file_obj.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()


# print(pi_string)
print(len(pi_string))

birthday = input("Enter you birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appear in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi!")