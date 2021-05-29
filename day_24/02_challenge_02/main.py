invited_names = []

with open("Names/invited_names.txt") as file:
    lines = file.readlines()
    for line in lines:
        invited_names.append(line.strip())

with open("Letters/starting_letter.txt") as file:
    content = file.read()

for name in invited_names:
    new_content = content.replace("[name]", name)

    file_name = f"invitation_{name}.txt"

    with open("ReadyToSend/" + file_name, "x") as file:
        file.write(new_content)
