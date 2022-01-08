import json

def get_restored_fav_num():
    filename = 'favorite_num.json'
    try:
        with open(filename, 'r') as f:
            numbers = json.load(f)
    except FileNotFoundError:
        # print(f"File {filename} not found!!!")
        None
    else:
        return numbers

def get_new_fav_num():
    filename = 'favorite_num.json'
    numbers = input("Enter your favorite number separate by comma: ")
    numbers = numbers.replace(' ', '').split(',')
    with open(filename, 'w') as f:
        json.dump(numbers, f)
    return numbers

def print_fav_num():
    numbers = get_restored_fav_num()
    if numbers:
        print(f"I know your favorite number! It's {numbers}")
    else:
        numbers = get_new_fav_num()
        print(f"Your favorite is {numbers}. I'll store for you.")
    # pass
print_fav_num()