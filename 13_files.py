file_path = "test.txt" # шлях до файлу

file = open(file_path, '+a') # відкриття файлу в режими +a

file.close() # закриття файлу

with open(file_path, '+a') as f:
    print("File test.txt was created!")


file_path = './txt_files/demofile.txt' # . означає поточний каталог

with open(file_path, 'r') as f:
    file_text = f.read()
    print(file_text)

with open(file_path, 'r') as f:
    file_text = f.read(6)
    print(file_text)

with open(file_path, 'r') as f:
    line_1 = f.readline()
    print(line_1)
    line_2 = f.readline()
    print(line_2)

with open(file_path, 'r') as f:
    lines = f.readlines()
    print(lines)

with open(file_path, 'r') as f:
    for line in f:
        print(line)

with open("demofile.txt", "a") as f:
    f.write("Now the file has more content!")

with open("demofile.txt", 'w') as f:
    f.write("Woops! I have deleted the content!")


try:
    with open("demofile.txt", 'x'):
        print('File was successfully created!')
except FileExistsError:
    print('File already exists!')