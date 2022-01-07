from typing import AnyStr


print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_num = input("Second number: ")
    if second_num == 'q':
        break
    try:
        answer = int(first_number) / int(second_num)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")