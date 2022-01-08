print("Give me two numers, I'll addtion them for you.")
print("Enter 'q' to quit")

while True:
    try:

            first_num = input("Enter first number: ")
            if first_num == 'q':
                break
            second_num = input("Enter second number: ")
            if second_num == 'q':
                break
            result = int(first_num) + int(second_num)
    except ValueError:
        print("Enter number not character !!!")
    else:
        print(str(result))