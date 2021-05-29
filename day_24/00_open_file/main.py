with open("files.txt", "r+") as file:
    content = file.read()
    print(content)

    file.seek(0)
    file.truncate()

    new_content = int(content) + 1
    file.write(str(new_content))

    file.seek(0)
    print(file.read())
