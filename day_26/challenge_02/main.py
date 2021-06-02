file1 = []
with open("file1.txt") as file:
    while True:
        number = file.readline()
        if not number:
            break

        file1.append(int(number))

file2 = []
with open("file2.txt") as file:
    while True:
        number = file.readline()
        if not number:
            break

        file2.append(int(number))

common_file = [n for n in file1 if n in file2]
print(common_file)
