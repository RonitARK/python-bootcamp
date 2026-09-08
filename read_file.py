
dictionary = {}

with open("sample.txt", "r") as file:
    content = file.read().lower().strip("@,.!?;:").split()

    for text in content:
        if text in dictionary:
            dictionary[text] += 1
        else:
            dictionary[text] = 1
    print(dictionary)
