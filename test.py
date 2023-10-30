#return like a list []

names = []

with open("./input/Names/invited_names.txt", "r") as file:
    for line in file:
        names.append(line.strip())

print(names)

# replace

