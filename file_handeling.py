
dictionary = {}

with open("scores.txt", "r") as file:
    for line in file:
        key, value = line.strip().split(",")
        dictionary[key] = int(value)

print(dictionary)