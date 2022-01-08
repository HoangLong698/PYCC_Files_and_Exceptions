files = ['cats.txt', 'dogs.txt']
for file in files:
    try:
        with open(file) as file_obj:
            contents = file_obj.read()
            print(contents)
    except FileNotFoundError as error:
        print(f"File {file} not found")